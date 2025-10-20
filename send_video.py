import socket
import pickle
import struct
import cv2

# Настройки подключения
host = 'localhost'  # Или IP-адрес сервера
port = 5000

# Подключение к серверу
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Захват видео с камеры
cap = cv2.VideoCapture(0)

try:
    while True:
        # Захват кадра
        ret, frame = cap.read()
        if not ret:
            break

        # Сериализация кадра
        data = pickle.dumps(frame)
        
        # Отправка размера данных и самих данных
        message = struct.pack("L", len(data)) + data
        client_socket.sendall(message)

        # Для просмотра своего видео на клиенте (опционально)
        cv2.imshow('Client Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    client_socket.close()
    cv2.destroyAllWindows()
