import socket

def lookup(website):
    try:
        ip = socket.getaddrinfo(website, 0)[3][4][0]
        return ip
    except:
        print("Error, no IP found")

def connect(website, port):
    try:
        socket.create_connection((website, port), timeout=5.0)
        return f"Port {port} is open"
    except socket.gaierror:
        return "No website found"
    except socket.timeout:
        return f"{port} timed out"
    except:
        return f"Port {port} is closed"