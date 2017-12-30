import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'jack', b'lucy', b'sarah']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 8001))
    # 接受数据
    print(s.recv(1024).decode('utf-8'))
s.close()