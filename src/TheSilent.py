import random
import socket
import struct
import threading
import time
import uuid

class World:
    def __init__(self,index,x=0,y=0,t=0):
        self.index = index
        self.x = x
        self.y = y
        self.t = t
        
    def algo(self):
        a = 11
        b = 17
        out = ((self.x ^ a) + (self.y ^ b) + (self.x * self.y)) % self.t
        return out

    def smooth(self):
        out = (World(0, self.x, self.y, self.t).algo() + World(0, self.x + 1, self.y, self.t).algo() + World(0, self.x - 1, self.y, self.t).algo() + World(0, self.x, self.y + 1, self.t).algo() + World(0, self.x, self.y - 1, self.t).algo()) // 12
        return out + self.t

    def gen_terrain(self):
        out = []
        t = 64
        c = 16
        for x in range(self.index*c,self.index*c+c):
            temp = []
            for y in range(self.index*c,self.index*c+c):
                temp.append(World(0,x,y,t).smooth())
            out.append(temp)
        return out
    
class TheSilent:
    def __init__(self,data,version="1.8.9",protocol=47):
        self.data = data
        self.protocol = protocol
        self.version = version
        self.SEGMENT_BITS = 0x7F
        self.CONTINUE_BIT = 0x80
        self.idx = 0
        self.players = {}
        self.alive = []

    def readVarInt(self):
        value = 0
        position = 0
        index = 0

        while True:
            currentByte = self.data[index]
            value |= (currentByte & self.SEGMENT_BITS) << position

            if currentByte & self.CONTINUE_BIT == 0:
                break

            position += 7
            index += 1

            if position >= 32:
                return -2

        return value
    
    def writeVarInt(self):
        out = b''
        value = self.data
        while True:
            if (value & ~self.SEGMENT_BITS) == 0:
                out += bytes([value])
                return out

            out += bytes([(value & self.SEGMENT_BITS) | self.CONTINUE_BIT])
            value >>= 7

    def recvall(self):
        content = b''
        length = TheSilent(self.data.recv(1)).readVarInt()
        while len(content) < length:
            request = self.data.recv(1)
            if not request:
                break
            content += request

        return content
    
    def KeepAlive(self):
        # keep alive sequence
        start = time.time()

        while True:
                end = time.time()
                if len(self.alive) > 0 and (end - start) % 15 == 0:
                    keepalive_id = random.randint(1, 2**31-1)

                    packet_id = TheSilent(0x00).writeVarInt()
                    payload = TheSilent(keepalive_id).writeVarInt()

                    packet = packet_id + payload
                    response = TheSilent(len(packet)).writeVarInt() + packet
                    for addr,c in self.players.items():
                        try:
                            c.send(response)

                        except:
                            print(f"{addr} has disconnected")
                            self.alive.remove(addr)
                            c.close()

    def RunServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 25565))
        s.listen(5)

        #world_spawn = World(self.idx).gen_terrain()
        keep_alive_thread = threading.Thread(target=self.KeepAlive)
        keep_alive_thread.start()

        while True:
            try:
                connection, address = s.accept()
                self.players.update({address[0]: connection})
                if self.players:
                    for addr, c in self.players.items():
                        packet = TheSilent(c).recvall()
                        state = -1

                        if b'\xdd\x02' in packet:
                            state = 2

                        if state == 2 and addr[0] not in self.alive:
                            # begin login
                            packet = TheSilent(c).recvall()
                            print(f"{addr} is requesting to login")
                            username_length = TheSilent(bytes([packet[2]])).readVarInt()
                            username = packet[2:username_length+2].decode("utf8")
                            uid = str(uuid.uuid4())
                            print(f"{addr} is {username}")
                            packet = TheSilent(2).writeVarInt() + TheSilent(len(uid)).writeVarInt() + uid.encode("utf8") + TheSilent(len(username.encode("utf8"))).writeVarInt() + username.encode("utf8")
                            response = TheSilent(len(packet)).writeVarInt() + packet
                            c.send(response)
                        
                            # start joining
                            print(f"{addr} is entering world")

                            packet_id = TheSilent(0x01).writeVarInt()
                            entity_id = struct.pack(">i", 1)
                            gamemode = struct.pack(">B", 0)
                            dimension = struct.pack(">b", 0)
                            difficulty = struct.pack(">B", 0)         # unsigned byte
                            max_players = struct.pack(">B", 20)       # unsigned byte
                            level_type = "default".encode("utf8")
                            level_type = TheSilent(len(level_type)).writeVarInt() + level_type
                            reduced_debug = struct.pack(">?", False)
                            
                            packet = packet_id + entity_id + gamemode + dimension + difficulty + max_players + level_type + reduced_debug
                            response = TheSilent(len(packet)).writeVarInt() + packet
                            c.send(response)

                            # send player position (1.8.9 correct packet id = 0x08)
                            print(f"{addr} is spawning")
                            packet_id = TheSilent(0x08).writeVarInt()

                            x = 32
                            y = 66
                            z = 32
                            yaw = 0
                            pitch = 0

                            flags = bytes([0])

                            packet = packet_id + struct.pack(">ddd", x, y, z) + struct.pack(">ff", yaw, pitch) + flags
                            response = TheSilent(len(packet)).writeVarInt() + packet

                            c.send(response)
                            self.alive.append(addr)

                            # send terrain data
                            GRASS = 2
                            num_sections = 4

                            blocks = b''
                            for _ in range(4096 * num_sections):
                                blocks += struct.pack("<H", (GRASS << 4) | 0)

                            block_light = bytes([0xFF] * (2048 * num_sections))
                            sky_light = bytes([0xFF] * (2048 * num_sections))
                            biomes = bytes([1] * 256)

                            section_data = blocks + block_light + sky_light + biomes
                            primary_bitmap = (1 << num_sections) - 1
                            data_length = TheSilent(len(section_data)).writeVarInt()

                            for cx in range(4):
                                for cz in range(4):
                                    packet = TheSilent(0x21).writeVarInt() + struct.pack(">i", cx) + struct.pack(">i", cz) + struct.pack(">?", True) + struct.pack(">H", primary_bitmap) + data_length + section_data
                                    c.send(TheSilent(len(packet)).writeVarInt() + packet)

            except:
                pass
            
if __name__ == "__main__":
    TheSilent(None).RunServer()
    
