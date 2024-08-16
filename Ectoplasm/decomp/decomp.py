import zlib,socket

ip = "127.0.0.1"
port = 1717

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)

client_socket.sendto("ready".encode(), (ip, port))
data, (recv_ip, recv_port) = client_socket.recvfrom(40960)
(profile, meta) = data.decode().split(";")
client_socket.sendto(zlib.decompress(open(profile.encode(), "rb").read(), wbits=-15) + "~".encode() + zlib.decompress(open(meta.encode(), "rb").read(), wbits=-15), (ip, port))
