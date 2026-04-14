import json
import socket

class TheSilent:
    def __init__(self,data,version="26.1.2",protocol=775):
        self.data = data
        self.protocol = protocol
        self.version = version
        self.SEGMENT_BITS = 0x7F
        self.CONTINUE_BIT = 0x80

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

    def handshake(self):
        status_response = json.dumps({"version": {"name": "26.1.2", "protocol": 775}, "description": {"text": "your mom"}}).encode("utf8")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 25565))
        s.listen(5)
       
        while True:
            c, addr = s.accept()
            print(f"Got connection from {addr}")
            
            init = c.recv(1)
            length_of_packet = TheSilent(init).readVarInt()
            packet = c.recv(length_of_packet)
            version = TheSilent(packet[1:]).readVarInt()
            
            if length_of_packet == -2 or version == -2:
                print(f"VarInt is too big")
                c.close()

            packet_data = TheSilent(0).writeVarInt() + TheSilent(len(status_response)).writeVarInt() + status_response
            packet = TheSilent(len(packet_data)).writeVarInt() + packet_data
            c.sendall(packet)
            temp = c.recv(4096)
            print(temp)

if __name__ == "__main__":
    TheSilent(None).handshake()