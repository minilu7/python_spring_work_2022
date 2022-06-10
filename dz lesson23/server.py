import socket
import base64
HOST = ''                 # Хост
PORT = 50008
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind((HOST, PORT))  # связываем сокет с портом, где он будет ожидать сообщения
sock.listen(1)  # указываем сколько может сокет принимать соединений
conn, addr = sock.accept()  # начинаем принимать соединения
print('Server is running, please, press ctrl+c to stop')
while True:
    data = conn.recv(102400)  # принимаем данные от клиента, по 1024 байт
    print(data)
    if not data:
        break
    conn.sendall(data)
    with open('ava.jpg', 'wb') as f:
        f.write(data)
conn.close()  # закрываем соединение
print(data)