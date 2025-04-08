import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Extract the headline (assuming the headline is in <h1> tag)
headline = soup.find("h1").get_text()

print("Headline:", headline)