import requests


api_key = "3cca93a0a82645bb976135225251609"

def get_weather(city_name):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': city_name,
        'lang': 'ru'
    }
    
    try:
        response = requests.get(url, params=params)
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
            
    except requests.exceptions.RequestException as e:
        return f"Ошибка соединения: {e}"




