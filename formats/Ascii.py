from lib.EncodingFormat import EncodingFormat
from utils.banner import print_banner


class ASCII(EncodingFormat):
    def encode(self, data: str) -> str:
        """Encodes the given data into ASCII format"""
        return ''.join(str(ord(char)) for char in data)

    def decode(self, data: str) -> str:
        """Decodes the given ASCII data"""
        return ''.join(chr(int(num)) for num in data.split())

    def info(self) -> str:
        print_banner()
        return """
ASCII encoding represents text in computers. Each character is represented by a number between 0 and 127.
The ASCII encoding scheme is used to represent text in computers, communications equipment, and other devices that work with text.

Read more: https://datatracker.ietf.org/doc/html/rfc20
        """