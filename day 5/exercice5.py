import requests
def get_robots_txt(url):
    if not url.startswith('http'):
        url = 'http://' + url
    robots_url = url.rstrip('/') + '/robots.txt'
    response = requests.get(robots_url)
    if response.status_code == 200:
        return response.text
    else:
        return "robots.txt not found"

# Example usage
print(get_robots_txt('example.com'))