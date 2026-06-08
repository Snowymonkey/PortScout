import argparse
from concurrent.futures import ThreadPoolExecutor
from network_utilities import lookup, connect

parser = argparse.ArgumentParser(
    prog='PortScout',
    description='Simple port scanning and IP lookup tool',
    epilog='Use --help to view all arguments'
)

group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument("target", help="Host to add or website to lookup")

group.add_argument(
    "-p",
    "--port",
    help = "Port to try connection with."
)

group.add_argument(
    "-pr",
    "--port_range",
    help = "Sets range of ports to try connections with inclusively. Must be in format LowerPort-UpperPort."
)

group.add_argument(
    "-l",
    "--lookup",
    action="store_true",
    help="Returns the IP of given website."
)

args = parser.parse_args()

if args.lookup:
    print(f"IP : {lookup(args.target)}")

elif args.port:
    connect(args.target, args.port)

elif args.port_range:
    if "-" in args.port_range:
        try:
            lowerPort = int(args.port_range.split("-")[0])
            upperPort = int(args.port_range.split("-")[1])
            ports = list(range(lowerPort, upperPort+1))

            with ThreadPoolExecutor(max_workers=100) as executor:
                results = executor.map(lambda p: connect(args.target, p), ports)

            for result in results:
                print(result)

        except:
            print("Invalid port range")
        
    else:
        print("Invalid port range. Must be in format LowerPort-UpperPort")