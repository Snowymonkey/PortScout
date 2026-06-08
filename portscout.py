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

parser.add_argument(
    "-op",
    "--open_ports",
    action="store_true",
    help="Only returns ports that are open."
)

args = parser.parse_args()

if args.lookup:
    print(f"IP : {lookup(args.target)}")

elif args.port:
    result = connect(args.target, args.port)
    if args.open_ports and "open" in result:
        print(result)
    elif not args.open_ports:
        print(result)


elif args.port_range:
    if "-" in args.port_range:
        try:
            lowerPort = int(args.port_range.split("-")[0])
            upperPort = int(args.port_range.split("-")[1])
            ports = list(range(lowerPort, upperPort+1))

            with ThreadPoolExecutor(max_workers=200) as executor:
                results = executor.map(lambda p: connect(args.target, p), ports)

            for result in results:
                if args.open_ports and "open" in result:
                    print(result)
                elif not args.open_ports:
                    print(result)

        except:
            print("Invalid port range")
        
    else:
        print("Invalid port range. Must be in format LowerPort-UpperPort")