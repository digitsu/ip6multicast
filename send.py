import socket

# Multicast group address and port
MCAST_GRP = 'ff3e::18db:2024'
MCAST_PORT = 12345

# Create a socket for IPv6 with UDP
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Set the time-to-live for messages directly as an integer
ttl = 1
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl)

# Specify the interface index for multicast traffic
# Replace 'your_interface_index' with the actual interface index
interface_index = socket.if_nametoindex('en0')  # Commonly 'en0' is for Wi-Fi or Ethernet on macOS
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_IF, interface_index)

message = 'Hello, Multicast!'
try:
    print(f"Sending message to the multicast group: {MCAST_GRP}")
    # Note: No need to change the sendto call
    sock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))
finally:
    print("Message sent")
    sock.close()
