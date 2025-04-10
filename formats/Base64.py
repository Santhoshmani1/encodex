import base64

from lib.EncodingFormat import EncodingFormat
from utils.banner import print_banner


class Base64(EncodingFormat):
    def encode(self, data: str, url_safe: bool = False) -> str:
        """Encodes the given data into Base64 format"""
        if url_safe:
            encoded_bytes = base64.urlsafe_b64encode(data.encode("utf-8"))
        else:
            encoded_bytes = base64.b64encode(data.encode("utf-8"))
        return encoded_bytes.decode("utf-8")

    def decode(self, data: str, url_safe: bool = False) -> str:
        """Decodes the given Base64 data"""
        if url_safe:
            decoded_bytes = base64.urlsafe_b64decode(data.encode("utf-8"))
        else:
            decoded_bytes = base64.b64decode(data.encode("utf-8"))
        return decoded_bytes.decode("utf-8")

    def info(self) -> str:
        print_banner()
        """Returns information about the Base64 encoding scheme"""
        description = """
The Base 64 encoding is designed to represent arbitrary sequences of
octets in a form that allows the use of both upper- and lowercase
letters but that need not be human readable.

Read more : https://datatracker.ietf.org/doc/html/rfc4648
        """

        return description
