#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a tcp client to HTTP GET www.baidu.com:80'

__author__ = 'Ethan Long'

from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

server_name = 'www.baidu.com'
server_port = 80

def make_http_massage(method):
	if method == 'GET':
		request = 'GET / HTTP/1.1\r\n'
		header = 'HOST: www.baidu.com\r\n'
		end = '\r\n'

		return request + header + end


http_message = make_http_massage('GET')

client_socket.connect((server_name, server_port))
client_socket.send(http_message.encode())

response = ''
buf = client_socket.recv(2048).decode()
response += buf
buf = client_socket.recv(2048).decode()
response += buf
buf = client_socket.recv(2048).decode()
response += buf
buf = client_socket.recv(2048).decode()
response += buf
buf = client_socket.recv(2048).decode()
response += buf
buf = client_socket.recv(2048).decode()
response += buf
buf = client_socket.recv(2048).decode()
response += buf
buf = client_socket.recv(2048).decode()
response += buf
buf = client_socket.recv(2048).decode()
response += buf

print(response.replace('\r', ''))

client_socket.close()