import socket

from src.config.settings import TCP_HOST, TCP_PORT


def recv_message(conn: socket.socket) -> str | None:
    data = conn.recv(1024)
    if not data:
        return None
    return data.decode()


def send_message(conn: socket.socket, message: str) -> None:
    conn.sendall(message.encode())


def main_loop() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_HOST, TCP_PORT))
        s.listen()
        print(f"Сервер запущен на порту {TCP_PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Подключено клиентом: {addr}")
            while True:
                message = recv_message(conn)
                if message is None:
                    break
                print(f"Получено от ESP: {message}")


if __name__ == "__main__":
    main_loop()

