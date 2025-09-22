#!/usr/bin/env python3
"""
Главный файл для запуска приложения
"""
import sys
import os

# Добавляем корневую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.app.voice_assistant import run_voice_assistant

if __name__ == "__main__":
    run_voice_assistant()
