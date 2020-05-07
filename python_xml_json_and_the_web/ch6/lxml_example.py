import requests
from lxml import etree

url = 'http://httpbin.org/xml'
result = requests.get(url)

doc = etree.fromstring(result.content)
print(result.text)

print(doc.tag)
print(doc.attrib['title'])

for elem in doc.findall('slide'):
    print(elem.tag)

newSlide = etree.SubElement(doc, 'slide')
newSlide.text = 'This is a new slide!'

slideCount = len(doc.findall('slide'))
itemCount = len(doc.findall('.//item'))

print(f'There are {slideCount} slide elements')
print(f'There are {itemCount} item elements')
