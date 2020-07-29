import requests

url = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/all.json"

response = requests.request("GET", url)

print(response.text)
