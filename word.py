import requests

word = input("Введите слово для поиска: ")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
response = requests.get(url)
data = response.json()

meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
example = data[0]["meanings"][0]["definitions"][0].get("example", "нет примера")

print("Определение:", meaning)
print("Пример:", example)
