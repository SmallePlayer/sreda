import socket
import base64
import cv2

HOST = "10.110.111.230"
PORT = 12532

def send_message():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect((HOST, PORT))
        print("Подключено к серверу")
        
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Камера не подключена")
            return
            
        print("Камера запущена")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Ошибка чтения кадра")
                continue
                
            # Кодируем кадр
            success, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            if not success:
                continue
                
            encoded_data = base64.b64encode(buffer)
            
            # Просто отправляем данные
            sock.send(encoded_data)
            
            # Показываем локально что отправляем
            # cv2.imshow("Local Camera", frame)
            
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
                
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        sock.close()
        cap.release()
        cv2.destroyAllWindows()
        print("Программа завершена")

if __name__ == "__main__":
    send_message()