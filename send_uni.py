import socket

# The receiver's IPv6 address and port
HOST = '240b:10:2f60:18ff:1c1f:eefb:9cbc:d2a6'  # Replace with the receiver's actual IPv6 address
PORT = 12345

# Create a socket for IPv6 with TCP
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    message = 'Hello, IPv6 World!'
    sock.sendall(message.encode())
    print(f"Sent message: {message}")
finally:
    sock.close()
