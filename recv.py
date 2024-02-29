import socket
import struct
#IPv6 multcast address and port
MCAST_GRP = 'ff02::1'
MCAST_PORT = 12345

# setup ipv6 socket
sock = socket.socket(socket.AF_INET6,
              socket.SOCK_DGRAM,
              socket.IPPROTO_UDP)

sock.bind(('::', MCAST_PORT))

# join multicast group
mreq = struct.pack("16si",
                   socket.inet_pton(socket.AF_INET6, MCAST_GRP),
                   socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

# Receive Data
while True:
    print(sock.recv(10240))

    