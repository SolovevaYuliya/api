import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}  
response = requests.get(url, headers=headers)
data = response.json()

print("Шутка:", data["joke"])

