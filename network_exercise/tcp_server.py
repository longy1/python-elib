#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a simple tcp server'

__author__ = 'Ethan Long'

from socket import *

server_port = 12000

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print('Server established.')

while True:
	connect_socket, addr = server_socket.accept()

	while True:
		message = connect_socket.recv(2048).decode()
		print(f'Recieve message: {message}')

		if message == 'EOF':
			connect_socket.send('CLOSE'.encode())
			break

		response = message.upper()
		connect_socket.send(response.encode())

	connect_socket.close()
