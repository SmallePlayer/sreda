import socket
import pickle
import struct
import cv2

# Настройки сервера
host = '0.0.0.0'
port = 5000

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Сервер запущен на {host}:{port}")

# Принятие подключения
client_socket, addr = server_socket.accept()
print(f"Подключился клиент: {addr}")

data = b""
payload_size = struct.calcsize("L")

while True:
    # Получение размера кадра
    while len(data) < payload_size:
        data += client_socket.recv(4096)
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    # Получение данных кадра
    while len(data) < msg_size:
        data += client_socket.recv(4096)
    
    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Десериализация кадра
    frame = pickle.loads(frame_data)
    
    # Отображение кадра
    cv2.imshow('Video Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()
cv2.destroyAllWindows()
