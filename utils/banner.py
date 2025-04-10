import pyfiglet


def print_banner():
    RED = "\033[31m"
    RESET = "\033[0m"
    name = "EncodeX"

    banner = pyfiglet.figlet_format(f"{name}")
    colored_banner = f"{RED}{banner}{RESET}"

    print(colored_banner)
