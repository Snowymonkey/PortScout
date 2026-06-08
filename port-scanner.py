import sys
import socket
import threading

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)

address = "45.33.32.156"
website = "nmap.scanme.org"

def lookup(website):
    try:
        ip = socket.getaddrinfo(website, 0)[3][4][0]
        return ip
    except:
        print("Error, no IP found")

def connect(website, port):
    try:
        socket.create_connection((website, port), 5)
        print(f"Port {port} is open")
    except:
        print(f"Port {port} is closed")


connect("instagram.com", 22)