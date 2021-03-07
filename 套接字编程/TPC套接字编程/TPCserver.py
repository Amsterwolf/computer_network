from socket import *

#ipv4,TPC协议
server_socket=socket(AF_INET,SOCK_STREAM)
#绑定端口
server_socket.bind(("",12580))
#最大连接数
server_socket.listen(1)
print("Ready")
while 1:
    #建立连接
    connection_socket,addr=server_socket.accept()
    meg=connection_socket.recv(2048)
    modified_meg=meg.decode().upper().encode()
    connection_socket.send(modified_meg)
    #断开连接
    connection_socket.close()