#include <WiFi.h>

const char* ssid = "TP-Link_9108";
const char* password = "12345678";
const char* host = "192.168.0.105";  // Например "192.168.1.100"
const int port = 12345;

WiFiClient client;

void setup() {
  Serial.begin(115200);
  
  // Подключение к Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nПодключено к Wi-Fi");

  // Подключение к серверу
  if (!client.connect(host, port)) {
    Serial.println("Ошибка подключения к серверу");
    return;
  }
  Serial.println("Подключено к серверу");

  // Отправка первого сообщения
  client.print("Привет от ESP32!");
}
int a = 0;
void loop() {
  // Чтение ответа от сервера
  // if (client.available()) {
  //   String response = client.readStringUntil('\n');
  //   Serial.print("Ответ от сервера: ");
  //   Serial.println(response);
  // }

  // Отправка новых сообщений каждые 5 секунд
  static unsigned long last_time = 0;
  if (millis() - last_time > 5000) {
    last_time = millis();
    client.print(a);
  }

  // "Время работы: " + String(millis()/1000) + " сек"
  if (!client.connected()) {
    Serial.println("Переподключение...");
    client.connect(host, port);
  }
}