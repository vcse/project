import socket
# SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 8001))
print('Bind UDP on 8001')
while True:
    # 接受数据
    data, address = s.recvfrom(1024)
    print('Received from %s:%s' % address)
    s.sendto(b'Hello, %s' % data, address)
