import requests

url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
dog = response.json()

print("Ссылка на фото:", dog["message"])
