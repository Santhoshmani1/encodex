from formats.Ascii import ASCII
from formats.Base64 import Base64
from formats.HexEncoding import HexEncoding
from formats.HtmlEncoding import HTMLEncoding
from formats.UrlEncoding import URLEncoding

formats = {
    "base64": Base64,
    "ascii": ASCII,
    "url": URLEncoding,
    "hex": HexEncoding,
    "html": HTMLEncoding,
}
