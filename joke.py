import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}  # говорим серверу: "дай JSON"
response = requests.get(url, headers=headers)
data = response.json()

print("Шутка:", data["joke"])
