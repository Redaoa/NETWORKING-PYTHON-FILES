import re 
import os
with open('C:\\Users\\otaku\\Desktop\\ip.txt') as fh: 
   fstring = fh.readlines() 

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 

# initializing the list object 
lst=[] 

# extracting the IP addresses 
for line in fstring: 
   lst.append(pattern.search(line)) 


print(lst) 