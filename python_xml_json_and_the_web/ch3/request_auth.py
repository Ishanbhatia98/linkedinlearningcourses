import requests
from requests.auth import HTTPBasicAuth as hba

url = 'http://httpbin.org/basic-auth/ishan/password'

credentials = hba('ishan', 'password')

response = requests.get(url, auth = credentials)

print(response.status_code)
print(response.headers)
print(response.content)
