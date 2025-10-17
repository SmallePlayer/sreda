import socket 
import base64
import numpy as np
import cv2
import threading
from threading import Thread


HOST = "0.0.0.0"
PORT = 12532


def reciv_message(data):
    try:
        decoded_bytes = base64.b64decode(data)
        frame = cv2.imdecode(np.frombuffer(decoded_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
        return frame
    except Exception as e:
        print(f"Ошибка декодирования: {e}")
        return None

def handle_client(conn, addr):
    try:
        while True:
            data = conn.recv(65536)
            if not data:
                break
            
            frame = reciv_message(data)
            if frame is not None and frame.size > 0:
                cv2.imshow("frame", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except Exception as e:
        print(f"Ошибка с клиентом {addr}: {e}")
    finally:
        conn.close()
        

def loop():
    global client_counter
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Сервер запущен на {HOST}:{PORT}")
        print("Ожидание подключений...")
        
        while True:
            conn, addr = s.accept()
            
            print(f"Новое подключение: {addr}")
            
            # Запускаем отдельный поток для каждого клиента
            client_thread = Thread(target=handle_client, args=(conn, addr))
            client_thread.daemon = True
            client_thread.start()

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        print("\nСервер завершает работу...")
    finally:
        cv2.destroyAllWindows()