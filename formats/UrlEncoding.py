import urllib.parse

from lib.EncodingFormat import EncodingFormat
from utils.banner import print_banner

class URLEncoding(EncodingFormat):
    def encode(self, data: str) -> str:
        """Encodes the given data into URL encoding format"""
        return urllib.parse.quote(data)

    def decode(self, data: str) -> str:
        """Decodes the given URL encoded data"""
        return urllib.parse.unquote(data)

    def info(self) -> str:
        print_banner()

        return """
        URL Encoding is the process of converting data into a valid URL format. 
        This encoding is used to convert data into a format that can be transmitted over the internet. 
        URL encoding replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits. 

        Read more: https://datatracker.ietf.org/doc/html/rfc3986#section-2.1
        """