import socket 
from threading import Thread
import os
import base64
import numpy as np
import cv2

HOST ="0.0.0.0"
PORT = 12532


def reciv_message(data):
    try:
        decoded_bytes = base64.b64decode(data)
        frame = cv2.imdecode(np.frombuffer(decoded_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
        return frame
    except Exception as e:
        print(f"Ошибка декодирования: {e}")
        return None
    

def loop():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Сервер запущен")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Подключено клиентом: {addr}")
                data = conn.recv(65536)
                if not data:
                    break
                
                frame = reciv_message(data)
                
                if frame is not None and frame.size > 0:
                    cv2.imshow("Video Stream", frame)
                    
                if cv2.waitKey(1) == ord("q"):
                    break
                
if __name__ == "__main__":
    loop()
                
            
                

                