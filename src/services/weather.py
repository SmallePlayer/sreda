import requests
from typing import Dict, Union

from src.config.settings import WEATHER_API_KEY


def get_weather(city_name: str) -> Union[Dict[str, object], str]:
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': WEATHER_API_KEY,
        'q': city_name,
        'lang': 'ru'
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if 'error' not in data:
            return {
                'город': data['location']['name'],
                'страна': data['location']['country'],
                'температура': data['current']['temp_c'],
                'ощущается_как': data['current']['feelslike_c'],
                'условия': data['current']['condition']['text'],
                'влажность': data['current']['humidity'],
                'скорость_ветра': data['current']['wind_kph']
            }
        else:
            return f"Ошибка: {data['error']['message']}"
    except requests.exceptions.RequestException as exc:
        return f"Ошибка соединения: {exc}"

