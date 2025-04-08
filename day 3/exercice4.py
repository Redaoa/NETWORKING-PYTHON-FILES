import requests
import time
current_time = time.time()
request = requests.get("https://example.com") # Replace with the actual URL of your server
ending_time = time.time()
rtt = (ending_time - current_time) 
print (f"RTT: {rtt} seconds")