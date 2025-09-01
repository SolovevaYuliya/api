import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=0a3f5c4d738dd56a3590dfe4ad8396cc&units=metric&lang=ru"
response = requests.get(url)
data = response.json()

city = data["name"]
temp = data["main"]["temp"]
feels = data["main"]["feels_like"]
desc = data["weather"][0]["description"]

print(f"🌍 Город: {city}")
print(f"🌡 Температура: {temp}°C (ощущается как {feels}°C)")
print(f"☁ Погода: {desc}")
