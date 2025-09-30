import socket
from threading import Thread
import os
import json

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.config.settings import TCP_HOST, TCP_PORT


def recv_message(conn: socket.socket, addr: str) -> str | None:
    data = socket.recv(1024).decode('utf-8').strip()
    print(f"Received : {data}")
        
    parsed_data = json.loads(data)
    
    name_id = parsed_data.get('name_id')
    temp = parsed_data.get('temp')
    humidity = parsed_data.get('humidity')

    # if name_id is None or temp is None or humidity is None:
    #     return None
    # return name_id, temp, humidity


def send_message(conn: socket.socket, message: str) -> None:
    conn.sendall(message.encode())


def main_loop() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_HOST, TCP_PORT))
        s.listen()
        print(f"Сервер запущен на порту {TCP_PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Подключено клиентом: {addr}")

                tread_client = Thread(target=recv_message, args=(conn, addr))
                tread_client.start()
                
                message = recv_message(conn)
                if message is None:
                    break
                print(f"Получено от ESP: {message}")


if __name__ == "__main__":
    main_loop()

