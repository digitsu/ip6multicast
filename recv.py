import socket
import struct

# Multicast group address and port
MCAST_GRP = 'ff02::1'
MCAST_PORT = 12345

# Create a socket for IPv6 with UDP
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Allow multiple sockets to use the same PORT number
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the port that we know will receive multicast data
sock.bind(('::', MCAST_PORT))

# Inform the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_pton(socket.AF_INET6, MCAST_GRP) + struct.pack('=I', 0)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, group)

print(f"Listening for messages on {MCAST_GRP}:{MCAST_PORT}")
while True:
    data, _ = sock.recvfrom(10240)
    print(f"Received message: {data.decode()}")
