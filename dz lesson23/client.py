import socket


HOST = '127.0.0.1'    # The remote host
PORT = 50008

with open('ava.JPG', 'rb') as f:
    ava = f.read()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('localhost', 55000))  # подключемся к серверному сокету
sock.send(bytes(ava))  # отправляем сообщение

data = sock.recv(102400)  # читаем ответ от серверного сокета
print('Received', repr(data))
sock.close()  # закрываем соединение
print(data)