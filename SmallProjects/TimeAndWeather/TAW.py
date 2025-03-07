from datetime import datetime

import pytz
import requests
from configparser import ConfigParser
from timezonefinder import TimezoneFinder

# Словарь для перевода погодных условий на русский
weather_translation = {
    "Clear": "Ясно",
    "Clouds": "Облачно",
    "Rain": "Дождь",
    "Drizzle": "Морось",
    "Thunderstorm": "Гроза",
    "Snow": "Снег",
    "Mist": "Туман",
    "Smoke": "Дым",
    "Haze": "Мгла",
    "Dust": "Пыль",
    "Fog": "Туман",
    "Sand": "Песок",
    "Ash": "Пепел",
    "Squall": "Шквал",
    "Tornado": "Торнадо"
}


# Функция для получения погоды
def getweather(city, api_key_weather):
    result = requests.get(weather_url.format(city, api_key_weather))
    if result.status_code == 200:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather_eng = json['weather'][0]['main']  # Погода на английском
        weather_ru = weather_translation.get(weather_eng, weather_eng)  # Перевод на русский
        lat = json['coord']['lat']  # Широта
        lon = json['coord']['lon']  # Долгота
        final = [city, country, temp_kelvin, temp_celsius, weather_ru, lat, lon]
        return final
    else:
        print("\nОшибка: Город не найден.")
        return None


# Функция для получения временной зоны по координатам
def get_timezone(lat, lon):
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lat=lat, lng=lon)  # Определяем часовой пояс
    if timezone:
        return timezone
    else:
        print("\nНе удается определить часовой пояс.")
        return None


# Функция для получения текущего времени и даты в указанной часовом поясе
def get_local_time(timezone):
    try:
        tz = pytz.timezone(timezone)
        local_time = datetime.now(tz)
        return local_time.strftime('Время: %H:%M:%S, Дата: %d-%m-%Y')
    except pytz.exceptions.UnknownTimeZoneError:
        return "\nНеизвестный часовой пояс."


# Основной код
print("Погода и время")
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)

# Ключ API для OpenWeatherMap
api_key_weather = config['twa']['api']

# URL для OpenWeatherMap API
weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# Ввод города
city = input("\nВведите город: ")

# Получаем погоду
weather = getweather(city, api_key_weather)
if weather:
    print(f"\nПогода в городе ``{city}``, {weather[1]}: {weather[4]}, Температура: {weather[3]:.2f}°C")

    # Получаем временную зону по координатам города
    lat = weather[5]  # Широта
    lon = weather[6]  # Долгота
    timezone = get_timezone(lat, lon)
    if timezone:
        print(f"\nЧасовой пояс для города ``{city}``: {timezone}")

        # Получаем текущее время и дату для этой временной зоны
        local_time = get_local_time(timezone)
        print(f"\nМестное время в городе ``{city}``: {local_time}")
    else:
        print("\nНе удалось определить временную зону.")
else:
    print("\nНе удалось получить данные о погоде и времени.")
print()