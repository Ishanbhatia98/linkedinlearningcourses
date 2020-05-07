
#urllib does not work??

from urllib.request import urlopen

url = 'http://httpbin.org/xml'

response = urllib.request.urlopen(url)
print(response)
