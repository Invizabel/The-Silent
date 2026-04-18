import random
import socket
import struct
import threading
import time
import uuid

class Classic:
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
        out = (Classic(0, self.x, self.y, self.t).algo() + Classic(0, self.x + 1, self.y, self.t).algo() + Classic(0, self.x - 1, self.y, self.t).algo() + Classic(0, self.x, self.y + 1, self.t).algo() + Classic(0, self.x, self.y - 1, self.t).algo()) // 12
        return out + self.t

    def gen_terrain(self):
        out = []
        t = 64
        c = 16
        for x in range(self.index*c,self.index*c+c):
            temp = []
            for y in range(self.index*c,self.index*c+c):
                temp.append(Classic(0,x,y,t).smooth())
            out.append(temp)
        return out
    
class Minecraft4K:
    def __init__(self,x=0,y=0,z=0,t=6):
        self.index = 0
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        
    def algo(self):
        a = 11
        b = 17
        c = 23
        out = ((self.x ^ a) + (self.y ^ b) + (self.z ^ c) + (self.x * self.y * self.z)) % self.t
        return out

    def gen_terrain(self):
        out = []
        t = 7
        c = 64
        AIR = 0
        STONE = 1
        GRASS = 2
        DIRT = 45
        OAK_LOGS = 17
        OAK_BRANCHES = 18
        BRICK = 45
        for x in range(self.index*c,self.index*c+c):
            temp1 = []
            for y in range(self.index*c,self.index*c+c):
                temp2 = []
                for z in range(self.index*c,self.index*c+c):
                    block_choice = Minecraft4K(x,y,z,t).algo()
                    if block_choice == 0:
                        temp2.append(AIR)
                    if block_choice == 1:
                        temp2.append(STONE)
                    if block_choice == 2:
                        temp2.append(GRASS)
                    if block_choice == 3:
                        temp2.append(DIRT)
                    if block_choice == 4:
                        temp2.append(OAK_LOGS)
                    if block_choice == 5:
                        temp2.append(OAK_BRANCHES)
                    if block_choice == 6:
                        temp2.append(BRICK)
                temp1.append(temp2)
            out.append(temp1)
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
        self.world = []
        self.lock = threading.RLock()

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
            with self.lock:
                end = time.time()
                if len(self.players) > 0 and (end - start) % 1 == 0:
                    keepalive_id = random.randint(1, 2**31-1)

                    packet_id = TheSilent(0x00).writeVarInt()
                    payload = TheSilent(keepalive_id).writeVarInt()

                    packet = packet_id + payload
                    response = TheSilent(len(packet)).writeVarInt() + packet
                    removal = []
                    for c, addr in self.players.items():
                        try:
                            c.send(response)

                        except:
                            print(f"{self.players[c]} has disconnected")
                            removal.append(c)
                            c.close()

                    for i in removal:
                        del self.players[i]

    def Play(self):
        while True:
            with self.lock:
                if self.players.items():
                    for c, addr in self.players.items():
                        try:
                            packet = TheSilent(c).recvall()
                            if packet[0] == 0x07 and packet[1] == 0x02:
                                pos = struct.unpack(">Q", packet[2:10])[0]
                                x = pos >> 38
                                y = (pos >> 26) & 0xFFF
                                z = pos & 0x3FFFFFF
                                if x >= 1 << 25:
                                    x -= 1 << 26
                                if z >= 1 << 25:
                                    z -= 1 << 26
                                print("block broken")
                                self.world[x][y][z] = 57
                        except:
                            pass

    def RunServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 25565))
        s.listen(10)

        self.world = Minecraft4K().gen_terrain()
        play_alive_thread = threading.Thread(target=self.Play)
        play_alive_thread.start()
        keep_alive_thread = threading.Thread(target=self.KeepAlive)
        keep_alive_thread.start()

        print(f"running server on port 25565")
        
        while True:
            c, addr = s.accept()
            with self.lock:
                try:
                    if c:
                        packet = TheSilent(c).recvall()
                        state = -1

                        if b'\xdd\x02' in packet:
                            state = 2

                        if state == 2 and addr[0] not in self.alive:
                            # handshake
                            packet = TheSilent(c).recvall()
                            username_length = TheSilent(bytes([packet[2]])).readVarInt()
                            username = packet[2:username_length+2].decode("utf8")
                            uid = str(uuid.uuid4())
                            packet = TheSilent(2).writeVarInt() + TheSilent(len(uid)).writeVarInt() + uid.encode("utf8") + TheSilent(len(username.encode("utf8"))).writeVarInt() + username.encode("utf8")
                            response = TheSilent(len(packet)).writeVarInt() + packet
                            c.send(response)
                        
                            # login success
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

                            # send terrain data
                            num_sections = 4

                            blocks = b''
                            for cx in range(64):
                                for cy in range(64):
                                    for cz in range(64):
                                        blocks += struct.pack("<H", (self.world[cx][cy][cz] << 4) | 0)

                            # join game
                            packet_id = TheSilent(0x08).writeVarInt()

                            x = 32
                            y = 64
                            z = 32
                            yaw = 0
                            pitch = 0

                            flags = bytes([0])

                            packet = packet_id + struct.pack(">ddd", x, y, z) + struct.pack(">ff", yaw, pitch) + flags
                            response = TheSilent(len(packet)).writeVarInt() + packet

                            c.send(response)

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


                            self.alive.append(username)
                            self.players.update({c: username})
                            print(f"{username} is entering world")

                except:
                    pass
            
if __name__ == "__main__":
    TheSilent(None).RunServer()
    