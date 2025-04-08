import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title tag
title = soup.title.string

print(f'Title of the web page: {title}')