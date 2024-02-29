import socket
import struct

# Multicast group address and port
MCAST_GRP = 'ff02::1'
MCAST_PORT = 12345

# Create a socket for IPv6 with UDP
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Set the time-to-live for messages to 1 so they do not go beyond the local network
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl)

message = 'Hello, Multicast!'
try:
    # Send message to the multicast group
    print(f"Sending message to the multicast group: {MCAST_GRP}")
    sock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))
finally:
    sock.close()

print("Message sent")
