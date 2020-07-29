import requests

url = "https://superheroapi.com/api/4278325702207782/"

query = {
  "character-id": 1
}

response = requests.request("GET", url, params=query)

print(response.text)
