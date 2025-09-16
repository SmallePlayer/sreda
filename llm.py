import ollama
import re
from wether import get_weather


def generate_prompt(text):
    response = ollama.generate(
        model='qwen3:0.6b',
        prompt = f"""
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

        Вопрос пользователя: {text}

        Твой ответ:
        """
        
        
    )

    full_response = response['response']
    
    # Ищем текст после </think>
    match = re.search(r'</think>(.*)', full_response, re.DOTALL)
    
    if match:
        # Если нашли тег, выводим текст после него
        result = match.group(1).strip()
        print("------------start----------------")
        print(result)
        print("-------------end-----------------")
        process_response(result)
    else:
        print("----------------------------")
        print(f"{full_response}")
        print("----------------------------")
        
        
def process_response(response_text):
    pattern = r'\((\w+)\s*,\s*([^)]+)\)'
    matches = re.findall(pattern, response_text)
    
    if matches:
        for match in matches:
            function_name, argument = match
            argument = argument.strip()
            
            print(f"{function_name} _ {argument}")
            if function_name == "get_weather":
                weather = get_weather(argument)
                print(f"\nПогода в городе {weather['город']}, {weather['страна']}:")
                print(f"Температура: {weather['температура']}°C")
                print(f"Ощущается как: {weather['ощущается_как']}°C")
                print(f"Условия: {weather['условия']}")
                print(f"Влажность: {weather['влажность']}%")
                print(f"Скорость ветра: {weather['скорость_ветра']} км/ч")
            
            
            