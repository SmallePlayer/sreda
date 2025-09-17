## SREDA – модульная архитектура

### Запуск
- Создайте и активируйте venv
- Установите зависимости: `pip install -r requirements.txt`
- Скопируйте `.env.example` в `.env` и заполните ключи
- Запуск ассистента: `python -m src.app.voice_assistant`
- Запуск TCP-сервера устройства: `python -m src.devices.esp_server`

### Структура
```
src/
  app/
    voice_assistant.py      # входная точка голосового ассистента
  core/
    llm.py                  # логика промптинга и разбор ответов
  devices/
    esp_server.py           # TCP сервер для устройства
  services/
    db.py                   # работа с SQLite
    weather.py              # запросы к Weather API
    weather_printer.py      # форматированный вывод погоды
  config/
    settings.py             # загрузка конфигурации из .env

models/
  big_model/                # существующие модели Vosk
  small_model/
```

### Переменные окружения (.env)
```
WEATHER_API_KEY=
VOSK_MODEL_DIR=models/small_model
OLLAMA_MODEL=qwen3:0.6b
```

### Заметки по миграции
- Старые файлы не удалены. Новые входные точки используют модули из `src/`.
- Импорты внутри новых модулей абсолютные, запускать через `python -m ...`.


