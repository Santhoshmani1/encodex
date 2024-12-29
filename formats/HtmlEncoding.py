import html

from lib.EncodingFormat import EncodingFormat
from utils.banner import print_banner


class HTMLEncoding(EncodingFormat):
    def encode(self, data: str) -> str:
        """Encodes the given data into HTML encoding format"""
        return html.escape(data)

    def decode(self, data: str) -> str:
        """Decodes the given HTML encoded data"""
        return html.unescape(data)

    def info(self) -> str:
        print_banner()

        return """
        HTML Encoding is a method used to encode special characters in HTML format.

        It works by encoding special characters into their respective HTML entities.

        For example, the character '<' is encoded as '&lt;' and the character '>' is encoded as '&gt;'.

        Read More : https://datatracker.ietf.org/doc/html/rfc1866      
        """        