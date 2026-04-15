import socket
import struct
import uuid

class World:
    def __init__(self,index,x,y,z):
        self.index = index
        self.x = x
        self.y = y
        self.z = z
    def algo(self):
        a = 11
        b = 17
        c = 23
        out = ((self.x ^ a) + (self.y ^ b) + (self.z ^ c) + (self.x + self.y + self.z)) % 8
        return out

    def gen_terrain(self):
        out = []
        c = 16
        for x in range(self.index*c,self.index*c+c):
            temp1 = []
            for y in range(self.index*64,self.index*64+c):
                temp2 = []
                for z in range(self.index*c,self.index*c+c):
                    temp2.append(World(0,x,y,z).algo())

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

    def RunServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 25565))
        s.listen(5)

        world = World(self.idx, 0, 0, 0).gen_terrain()

        while True:
            c, addr = s.accept()

            packet = TheSilent(c).recvall()
            print(packet)
            state = -1

            if b'\xdd\x02' in packet:
                state = 2

            if b'\xdd\x03' in packet:
                state = 2
            
            if state == 2:
                # begin login
                packet = TheSilent(c).recvall()
                print(f"{addr[0]} is requesting to login")
                username_length = TheSilent(bytes([packet[2]])).readVarInt()
                username = packet[2:username_length+2].decode("utf8")
                uid = str(uuid.uuid4())
                print(f"{addr[0]} is {username}")
                packet = TheSilent(2).writeVarInt() + TheSilent(len(uid)).writeVarInt() + uid.encode("utf8") + TheSilent(len(username.encode("utf8"))).writeVarInt() + username.encode("utf8")
                response = TheSilent(len(packet)).writeVarInt() + packet
                c.send(response)
            
                # start joining
                print(f"{addr[0]} is entering world")

                packet_id = TheSilent(0x01).writeVarInt()
                entity_id = struct.pack(">i", 1)
                gamemode = struct.pack(">B", 1)
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
                '''print(f"{addr[0]} is spawning")
                packet_id = TheSilent(0x08).writeVarInt()

                x = 0
                y = 64
                z = 0
                yaw = 0
                pitch = 0

                flags = bytes([0])

                packet = packet_id + struct.pack(">ddd", x, y, z) + struct.pack(">ff", yaw, pitch) + flags
                response = TheSilent(len(packet)).writeVarInt() + packet

                c.send(response)'''

            # handshake end

if __name__ == "__main__":
    TheSilent(None).RunServer()
    
