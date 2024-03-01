import requests
url = "https://learn-co-curriculum.github.io/json-site-example/"
response = requests.get(url)
print(response.text)