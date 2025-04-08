import requests
def check_website(url):
    response = requests.get(url)
    if response.status_code <= 300:
        return True
    else:
       return False
url = 'https://www.example.com'
if check_website(url) == True:
    print(f"The website {url} is up.")
else:
    print(f"The website {url} is down.")