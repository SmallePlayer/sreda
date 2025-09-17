import socket

HOST = '0.0.0.0'  # Слушать все интерфейсы
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Сервер запущен на порту {PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Подключено клиентом: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Получено от ESP: {data.decode()}")
            # Отправка ответа
            # response = input("Введите ответ для ESP: ")
            # conn.sendall(response.encode())