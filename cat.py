import requests

url = "https://api.thecatapi.com/v1/images/search"
response = requests.get(url)
cat = response.json()

print("Ссылка на фото:", cat[0]["url"])