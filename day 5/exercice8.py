import requests

url = "https://example.com/image.jpg"
response = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(response.content)