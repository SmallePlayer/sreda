import socket

HOST = '0.0.0.0'  # Слушать все интерфейсы
PORT = 12345

     
def main_loop():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Сервер запущен на порту {PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Подключено клиентом: {addr}")
            while True:
                message = recv_message(conn)
                print(f"Получено от ESP: {message}")
                
                
def recv_message(conn):
    data = conn.recv(1024)
    if not data:
        return None
    return data.decode()

def send_message(conn, message):
    conn.sendall(message.encode())