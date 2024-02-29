import socket
import struct

# IPv6 multicast address, port, and scope ID
MCAST_GRP = 'ff02::1%en0'  # Adjust 'eth0' as necessary
MCAST_PORT = 12345

# Create a socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

# Set the time-to-live for messages to 1
ttl_bin = struct.pack('@i', 1)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl_bin)

# Resolve the address and scope ID
addrinfo = socket.getaddrinfo(MCAST_GRP.split('%')[0], None)[0]
send_addr = addrinfo[4][0], MCAST_PORT

# Message to be sent
message = 'Hello, Multicast!'.encode('utf-8')

try:
    # Send message to the multicast group
    print(f"Sending message to the multicast group: {MCAST_GRP} {send_addr}")
    sent = sock.sendto(message, send_addr)
finally:
    print("Closing the socket")
    sock.close()

print("Message sent")
