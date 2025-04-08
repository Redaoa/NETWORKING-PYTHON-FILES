import re

# Open the text file in read mode
with open('url.txt', 'r') as file:
    text = file.read()

# Regular expression to match URLs
url_pattern = r'https?://\S+'
urls = re.findall(url_pattern, text)

# Print or save the URLs
print("Extracted URLs:")
for url in urls:
    print(url)