## SREDA – модульная архитектура

### Запуск
- Создайте и активируйте venv: `python -m venv venv && source venv/bin/activate`
- Установите зависимости: `pip install -r requirements.txt`
- Скачайте модель Vosk (см. раздел "Установка модели Vosk" ниже)
- Создайте файл `.env` и заполните ключи (см. раздел "Переменные окружения")
- Запуск ассистента: `python run_voice_assistant.py`
- Запуск TCP-сервера устройства: `python run_esp_server.py`

### Установка модели Vosk
Для работы голосового ассистента необходимо скачать модель Vosk:

1. Создайте папку `models` в корне проекта
2. Скачайте русскую модель (рекомендуется small):
   ```bash
   mkdir -p models
   cd models
   wget https://alphacep.com/vosk/models/vosk-model-small-ru-0.22.zip
   unzip vosk-model-small-ru-0.22.zip
   mv vosk-model-small-ru-0.22 small_model
   ```
3. Убедитесь, что в `.env` указан правильный путь: `VOSK_MODEL_DIR=models/small_model`

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


