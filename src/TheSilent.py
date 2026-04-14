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

        while True:
            currentByte = self.data
            value |= (currentByte & self.SEGMENT_BITS) << position

            if currentByte & self.CONTINUE_BIT == 0:
                break

            position += 7

            if position >= 32:
                raise Exception("VarInt is too big")

        return value
    
    def readVarLong(self):
        value = 0
        position = 0

        while True:
            currentByte = self.data
            value |= currentByte & self.SEGMENT_BITS << position

            if currentByte & self.CONTINUE_BIT == 0:
                break

            position += 7

            if (position >= 64):
                raise Exception("VarLong is too big")

        return value
    
    def writeVarInt(self):
        while True:
            if self.data & ~self.SEGMENT_BITS == 0:
                return self.data

            self.data = (self.data & self.SEGMENT_BITS) | self.CONTINUE_BIT
            self.data >>= 7

    def writeVarLong(self):
        while True:
            if self.data & ~self.SEGMENT_BITS == 0:
                return self.data

            self.data = (self.data & self.SEGMENT_BITS) | self.CONTINUE_BIT

            self.data  >>= 7

    def handshake(self):
        status_response = json.dumps({"version": {"name": self.version, "protocol": self.protocol}, "description": {"text": "your mom"}})
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 25565))
        s.listen(5)
        while True:
            c, addr = s.accept()
            print(f"Got connection from {addr}")
            c.send(status_response.encode()) 

if __name__ == "__main__":
    TheSilent(None).handshake()