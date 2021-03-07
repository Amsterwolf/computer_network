from socket import *

server_socket=socket(AF_INET,SOCK_DGRAM)
#绑定端口12580
server_socket.bind(("",12580))
print("Ready")
while 1:
    meg,client_addr=server_socket.recvfrom(2048)
    if meg!=None:
        print("recv meg:",meg)
    modified_meg=meg.decode().upper()
    server_socket.sendto(modified_meg.encode(),client_addr)
