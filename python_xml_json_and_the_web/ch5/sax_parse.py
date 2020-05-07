import requests
import xml.sax

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount  = 0
        self.isInTitle = False

    def startElement(self, tagName, attrs):
        if tagName == 'slideshow':
            print('Slideshow title: ', attrs['title'])
    
        elif tagName=='slide':
            self.slideCount+=1
        elif tagName=='item':
            self.itemCount+=1
        elif tagName=='title':
            self.isInTitle = True

    def endElement(self, tagName):
        if tagName=='title':
            self.isInTitle = False

    def characters(self, chars):
        if self.isInTitle:
            print("Title: ", chars)

    def startDocument(self):
        print('Starting up!')

    def endDocument(self):
        print('Finishing up!')


handler = MyContentHandler()

url = 'http://httpbin.org/xml'

response = requests.get(url)

xml.sax.parseString(response.text, handler)
#print(response.text)

print(f'There were {handler.slideCount} slide elements.')
print(f'There were {handler.itemCount} item elements.')
