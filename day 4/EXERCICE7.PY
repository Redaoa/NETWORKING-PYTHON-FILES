import os
os.system('python -m spf example.com > spf.txt')
with open('spf.txt', 'r') as file:
    print(file.read())