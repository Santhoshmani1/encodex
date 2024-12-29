from lib.EncodingFormat import EncodingFormat
from utils.banner import print_banner

class HexEncoding(EncodingFormat):
    def encode(self, data: str) -> str:
        """Encodes the given data into Hex format"""
        if data.isdigit():
            return hex(int(data))[2:].upper()
        return data.encode("utf-8").hex().upper()

    def decode(self, data: str) -> str:
        """Decodes the given Hex data"""
        try:
            return str(int(data, 16))
        except ValueError:
            return bytes.fromhex(data).decode("utf-8")

    def info(self) -> str:
        print_banner()

        return """
Hex Encoding:
Hex encoding converts data into hexadecimal format. Each byte of data is converted into two hexadecimal characters.
Hex encoding is case-insensitive and is usually represented in uppercase.

Read More: https://datatracker.ietf.org/doc/html/rfc4648#section-8
        """

        