import requests
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

response = requests.get(url)

print(response.content)
