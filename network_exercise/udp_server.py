#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a simple udp server'

__author__ = 'Ethan Long'

from socket import *

server_port = 12001
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('server socket binded.')

while True:
	request_message, client_addr = server_socket.recvfrom(2048)
	response_message = request_message.decode().upper()
	print(f'Send repsone: {response_message}')
	server_socket.sendto(response_message.encode(), client_addr)