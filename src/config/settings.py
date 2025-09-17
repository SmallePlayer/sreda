import os
from dotenv import load_dotenv

load_dotenv()


WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '3cca93a0a82645bb976135225251609')
VOSK_MODEL_DIR = os.getenv('VOSK_MODEL_DIR', 'small_model')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'qwen3:0.6b')
TCP_HOST = os.getenv('TCP_HOST', '0.0.0.0')
TCP_PORT = int(os.getenv('TCP_PORT', '12345'))
SQLITE_PATH = os.getenv('SQLITE_PATH', 'device.db')

