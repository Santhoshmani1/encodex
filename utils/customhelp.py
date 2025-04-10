import argparse
from utils.banner import print_banner


class CustomHelpAction(argparse.Action):
    def __init__(
        self,
        option_strings,
        dest=argparse.SUPPRESS,
        default=argparse.SUPPRESS,
        help=None,
    ):
        super().__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        print_banner()
        parser.print_help()
        parser.exit()
