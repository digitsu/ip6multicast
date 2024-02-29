import socket

# Standard IPv6 address and port to listen on
HOST = '::'  # Listening on all available interfaces
PORT = 12345

# Create a socket for IPv6 with TCP
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"Listening for connections on {HOST}:{PORT}")

conn, addr = sock.accept()
print(f"Connected by {addr}")
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Received message: {data.decode()}")
conn.close()
