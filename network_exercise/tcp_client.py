#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a simple tcp client'

__author__ = 'Ethan Long'

from socket import *
import time

server_name = '127.0.0.1'
server_port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

# message1 = 'A lower sentence 1.'
# message2 = 'A lower sentence 2.'

# client_socket.send(message1.encode())
# response1 = client_socket.recv(1024).decode()

# client_socket.send(message2.encode())
# response2 = client_socket.recv(1024).decode()

# print(f'response 1: {response1}')
# print(f'response 2: {response2}')

while True:
	message = input('Input message to send, input EOF to end: ')
	client_socket.send(message.encode())
	response = client_socket.recv(2048).decode()
	print(f'Recieve response: {response}')
	if response == 'CLOSE':
		break

client_socket.close()