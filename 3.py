import requests

url = "https://en.wikipedia.org/api/rest_v1/page/summary/Python_(programming_language)"
response = requests.get(url)
data = response.json()

print("Заголовок:", data["title"])
print("Описание:", data["extract"])

