import socket
import struct
# ipv6 multcast address and port

MCAST_GRP = 'ff02::1'
MCAST_PORT = 12345

# create a socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

#set time to live for message to 1 so they do not go beyond the local network 
ttl_bin = struct.pack('@i', 1)
# '@i' denotes native order integer
sock.setsockopt(socket.IPPROTO_IPV6, socket .IPV6_MULTICAST_HOPS, ttl_bin)

# Message to be sent
message = 'Hello, Multicast!'.encode('utf-8')

try:
    #send message to the multacst group
    print(f"Sending message to the multcast group:
          {MCAST_GRP}")
    sent = sock.sendto(message, MCAST_GRP,MCAST_PORT))
finally:
    print("Closing the sockt")
    sock.close()

print("Message Sent")