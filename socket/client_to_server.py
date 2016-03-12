#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

#  创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   建立连接
s.connect(('www.sina.com', 80))
#  发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
	#接受1k字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data =  b' '.join(buffer)

# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print('******* 连接成功！ ********')
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)