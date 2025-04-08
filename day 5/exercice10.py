import requests

def web_enumeration(base_url, wordlist):
    results = {}
    for word in wordlist:
        url = f"{base_url}/{word}"
        try:
            response = requests.get(url)
            results[url] = response.status_code
        except requests.RequestException as e:
            results[url] = f"Error: {e}"
    return results

if __name__ == "__main__":
    base_url = "http://example.com"  # Replace with correct URL
    wordlist = ["admin", "login", "dashboard", "test"]  # Replace with your wordlist

    results = web_enumeration(base_url, wordlist)
    for url, status in results.items():
        if not status == 404:
            print(f"{url}/ {status}")