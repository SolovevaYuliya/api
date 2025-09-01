import requests
import textwrap

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = requests.get(url)
data = response.json()

print("Заголовок:", data["title"])
print("Фото планеты:", data["url"])
print("Дата фото:", data["date"])
print("Описание:")

wrapper = textwrap.TextWrapper(width=80)
wrapped_text = wrapper.fill(text=data["explanation"])
print(wrapped_text)
