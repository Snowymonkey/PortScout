import argparse

parser = argparse.ArgumentParser(
    prog='PortScout',
    description='Simple port scanning and IP lookup tool',
    epilog='Use --help to view all arguments'
)

group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument("target")

group.add_argument(
    "-p",
    "--port",
    help = "Port to try connection with."
)

group.add_argument(
    "-pr",
    "--port_range",
    help = "Sets range of ports to try connections with. Must be in format LowerPort-UpperPort."
)

group.add_argument(
    "-l",
    "--lookup",
    help="Returns IP of given website."
)


args = parser.parse_args()
