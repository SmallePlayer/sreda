from wether import get_weather


def print_wether(argument):
    weather = get_weather(argument)
    print(f"\nПогода в городе {weather['город']}, {weather['страна']}:")
    print(f"Температура: {weather['температура']}°C")
    print(f"Ощущается как: {weather['ощущается_как']}°C")
    print(f"Условия: {weather['условия']}")
    print(f"Влажность: {weather['влажность']}%")
    print(f"Скорость ветра: {weather['скорость_ветра']} км/ч")