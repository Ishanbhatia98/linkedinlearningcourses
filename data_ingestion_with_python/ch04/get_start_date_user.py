#Needs correction!!

import requests
from pprint import pprint as pp

user = 'tebeka'
#user = 'ishanbhatia1998'

link = requests.get('https://api.github.com/users/'+user)
'''
print(type(link))

pp(link.headers)
for k, v in link.headers.items():
    print(k, v)

'''
print(f"Joining date of {user} - {link.headers['last-modified']}")


