# -*- coding: utf-8 -*-
import socket
import os


def get_response(request):
	response_code = '200 OK'
	line = request.decode().split('\r')
	first_line = line[0].split()
	
	if (first_line[0] != 'GET'):  return "Incorrect responce, try again"
	
	if (first_line[1] == '/') :
		for i in line:
			if (i.find("User-Agent") != -1): return "Hello, Mister. You're: " + i + "\n" + response_code
		return '404 not found'

	elif (first_line[1] == '/media'): 
		files = os.listdir ("files")
		all_files = ''
		for fi in files:
			all_files = all_files + fi + '\n'
		return all_files + response_code
	
	elif (first_line[1].find('/media/') != -1) :
		try:
			index = first_line[1].rfind('/')
			file_name = first_line[1][index:len(first_line[1]):1]
			f = open ('files/' + file_name)
			return f.read() + "\n" + response_code
		
		except IOError: 
			return "File not found"	 
	
	elif (first_line[1] == '/test/') : 
		http_request = ''		
		for i in line:
			http_request = http_request + i
		return http_request

	return "Page not found"		

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #связываем наш сокет с данным хостом и портом
server_socket.listen(0)  #запускаем режим прослушивания для данного сокета

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #выводим подключенного клиента
        request_string = client_socket.recv(2048)  #получаем данные с сокета до 2048 бит
        client_socket.send(get_response(request_string))  #отправляем обработанный ответ
        client_socket.close()
    except KeyboardInterrupt:  #прерывание работы сервера с клавиатуры
        print 'Stopped'
        server_socket.close()  #закрываем сокет
        exit()
