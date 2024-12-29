
# EncodeX CLI

EncodeX is a CLI tool that helps you encode and decode strings using various data formats.

## Overview
Encodex is a simple command-line interface (CLI) tool for encoding and decoding operations. It supports various encoding formats such as Base64, ASCII, URL, Hex, and HTML.

## Installation

```bash
git clone https://github.com/Santhoshmani1/encodex.git
```

## Usage

```bash
python3 encodex.py [options] [format] [string]
```

### Examples

#### Getting Help
```bash
python main.py --help
python main.py -h
```

```bash
 _____                     _     __  __
| ____|_ __   ___ ___   __| | ___\ \/ /
|  _| | '_ \ / __/ _ \ / _` |/ _ \\  / 
| |___| | | | (_| (_) | (_| |  __//  \ 
|_____|_| |_|\___\___/ \__,_|\___/_/\_\
                                       

usage: main.py [-h] {encode,decode,info,list} ...

EncodeX CLI - Encoding and Decoding Utility

positional arguments:
  {encode,decode,info,list}
                        Available commands
    encode              Encode data
    decode              Decode data
    info                Get info about encoding format
    list                List available encoding formats

options:
  -h, --help            Show this help message and exit
                                                                 
```

#### Listing available encoding formats

```bash
$ python main.py list
```
```
Available encoding formats:
  - base64
  - ascii
  - url
  - hex
  - html
```

#### Getting information about an encoding format

```bash
$ python main.py info base64
```

```bash
 _____                     _     __  __
| ____|_ __   ___ ___   __| | ___\ \/ /
|  _| | '_ \ / __/ _ \ / _` |/ _ \\  / 
| |___| | | | (_| (_) | (_| |  __//  \ 
|_____|_| |_|\___\___/ \__,_|\___/_/\_\
                                       


The Base 64 encoding is designed to represent arbitrary sequences of
octets in a form that allows the use of both upper- and lowercase
letters but that need not be human readable.

Read more : https://datatracker.ietf.org/doc/html/rfc4648
        
```


#### Encoding into a fomat

```bash
$ python main.py encode base64 "Hello, World!"
SGVsbG8sIFdvcmxkIQ==
```

#### Decoding into a format

```bash
$ python main.py decode base64 "SGVsbG8sIFdvcmxkIQ=="
Hello, World!
```

## License
MIT

