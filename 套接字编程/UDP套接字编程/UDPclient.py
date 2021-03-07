from socket import *
'''通过套接字，由UDP协议向服务器发送一串小写字符，服务器接收大写后返回'''

#遵守ipv4,UDP协议的套接字
client_socket=socket(AF_INET,SOCK_DGRAM)
meg=input("input lowercase sentence:")
print(meg)
client_socket.sendto(meg.encode(),("159.75.140.116",12580))
modefied_meg,server_addr=client_socket.recvfrom(2048)
print(modefied_meg.decode())
client_socket.close()
