from socket import *

client_socket=socket(AF_INET,SOCK_STREAM)
#连接至(ip,端口号)
client_socket.connect(("159.75.140.116",12580))
meg=input("input lowercase sentence:")
#发送meg
client_socket.send(meg.encode())
#接收modified_meg
modified_meg=client_socket.recv(2048)
print(modified_meg.decode())
#断开连接
client_socket.close()
