#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a simple udp client'

__author__ = 'Ethan Long'

from socket import *
#server_name = '106.55.243.139'
# server_port = 12000
server_name = '127.0.0.1'
server_port = 12001

# 实例化socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# 定义信息
message = 'A lowercase sentence.'

# 发送编码后的信息, 使用定义好的目标地址
client_socket.sendto(message.encode(), (server_name, server_port))

# recieve response
response_message, server_addr = client_socket.recvfrom(2048)

# print
print(f'Response: {response_message.decode()}')
print(f'Server: {server_addr}')

client_socket.close()