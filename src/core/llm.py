import re
import os
import sys
from typing import Callable

import ollama

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.config.settings import OLLAMA_MODEL
from src.services.weather import get_weather
from src.services.weather_printer import print_weather


def generate_prompt(user_text: str) -> None:
    response = ollama.generate(
        model=OLLAMA_MODEL,
        prompt=f"""
        Ты - голосовой ассистент. Твоя задача давать краткие и точные ответы.

        ВАЖНЫЕ ПРАВИЛА:
        1. Если пользователь спрашивает о погоде - ответ ДОЛЖЕН быть строго в формате: 
        (get_weather, [название города])

        2. Для всех остальных запросов отвечай обычным текстом

        3. Никаких дополнительных объяснений, только ответ в требуемом формате

        Примеры правильных ответов:
        • "Какая погода в Москве?" → (get_weather, Москва)
        • "Что по погоде в Лондоне?" → (get_weather, Лондон)
        • "Скажи погоду для Парижа" → (get_weather, Париж)

        Вопрос пользователя: {user_text}

        Твой ответ:
        """,
    )

    full_response = response['response']

    match = re.search(r'</think>(.*)', full_response, re.DOTALL)
    result_text = match.group(1).strip() if match else full_response.strip()

    print("------------start----------------")
    print(result_text)
    print("-------------end-----------------")
    process_response(result_text)


def process_response(response_text: str) -> None:
    pattern = r'\((\w+)\s*,\s*([^\)]+)\)'
    matches = re.findall(pattern, response_text)

    if not matches:
        return

    dispatch: dict[str, Callable[[str], None]] = {
        'get_weather': _handle_get_weather,
    }

    for function_name, argument in matches:
        argument = argument.strip()
        handler = dispatch.get(function_name)
        if handler:
            handler(argument)


def _handle_get_weather(city: str) -> None:
    weather = get_weather(city)
    print_weather(weather)

