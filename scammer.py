import requests

url = input("https://example.com ")

response = requests.get(url)

print(response.status_code)
