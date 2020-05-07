import xml.dom.minidom
import requests

url = 'http://httpbin.org/xml'

result = requests.get(url)

domtree = xml.dom.minidom.parseString(result.text)

rootnode = domtree.documentElement

print('The root element is: ', rootnode.nodeName)

print('Title: ', rootnode.getAttribute('title'))

items = domtree.getElementsByTagName('item')
print(f'There are {items.length} item tags')
