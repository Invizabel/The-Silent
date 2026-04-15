import json
import socket
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
        out = ((self.x ^ a) + (self.y ^ b) + (self.z ^ c) + (self.x * self.y * self.z)) % 8
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
    def __init__(self,data,version="26.1.2",protocol=775):
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
        out = b""
        value = self.data
        while True:
            if (value & ~self.SEGMENT_BITS) == 0:
                out = bytes([value])
                return out

            out = bytes([(value & self.SEGMENT_BITS) | self.CONTINUE_BIT])
            value >>= 7

    def RunServer(self):
        status_response = json.dumps({"version": {"name": "26.1.2", "protocol": 775}, "description": {"text": "A Minecraft Server"}}).encode("utf8")
        disconnect_response = json.dumps({"text": "You were kicked for trying to swim in void!"}).encode("utf8")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 25565))
        s.listen(5)

        world = World(self.idx, 0, 0, 0).gen_terrain()
    
       
        while True:
            c, addr = s.accept()
            print(f"Got connection from {addr[0]}")

            init = c.recv(1)
            length_of_packet = TheSilent(init).readVarInt()
            packet = c.recv(length_of_packet)
            version = TheSilent(packet[1:]).readVarInt()
            state = TheSilent(bytes([packet[-1]])).readVarInt()
            
            if length_of_packet == -2 or version == -2:
                print(f"VarInt is too big")
                c.close()

            if state == 1:
                # get status
                print(f"{addr[0]} is requesting status")
                packet_data = TheSilent(0).writeVarInt() + TheSilent(len(status_response)).writeVarInt() + status_response
                packet = TheSilent(len(packet_data)).writeVarInt() + packet_data
                c.send(packet)
                c.close()
            
            if state == 2:
                # begin login
                print(f"{addr[0]} is requesting to login")
                init = c.recv(1)
                length = TheSilent(init).readVarInt()
                packet = c.recv(length)
                username_length = TheSilent(packet[1:]).readVarInt()
                username = packet[2:username_length+2].decode("utf8")
                uid = uuid.UUID(bytes=packet[username_length+2:username_length+2+16])
                print(f"{addr[0]} is {username}")
                packet = TheSilent(2).writeVarInt() + uid.bytes + TheSilent(len(username.encode("utf8"))).writeVarInt() + username.encode("utf8") + TheSilent(0).writeVarInt()
                response = TheSilent(len(packet)).writeVarInt() + packet
                c.send(response)

                packet = c.recv(1)
                length = TheSilent(packet).readVarInt()
                packet = c.recv(length)
                state = TheSilent(packet).readVarInt()
                

                if state == 3:
                    # start joining
                    print(f"{addr[0]} is joining server")

            # handshake end

if __name__ == "__main__":
    TheSilent(None).RunServer()
    
