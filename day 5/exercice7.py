import requests

url = 'http://example.com/api'
data = {'key':'value'}
response = requests.post(url, data=data)

print(response.text)