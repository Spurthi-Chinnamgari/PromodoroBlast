import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Here's a joke for you:")
    print(f"{data['setup']}")
    print(f"{data['punchline']}")
else:
    print("Failed to fetch a joke!")
