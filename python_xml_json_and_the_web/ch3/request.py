import requests

def printresults(res):
    print('Respnse code: ', res.status_code)
    print('Headers: ', res.headers)
    #print('Content: ', res.content)
    print('Text: ', res.text)

#using get to generate standard HTTP response
url = 'http://httpbin.org/xml'

response = requests.get(url)
printresults(response)

#using get to send some data to the url
url = 'http://httpbin.org/get'

datavals = {
        'key1':'val1',
        'key2':'val2'
}

response = requests.get(url, params=datavals)
printresults(response)

#using post

url = 'http://httpbin.org/post'

response = requests.post(url, data=datavals)
printresults(response)

#sending header values via get

headervals = {
        'user': 'ishan',
        'country':'india',
        'degree':'engineering'
        }
url = 'http://httpbin.org/get'

response = requests.get(url, headers=headervals)
printresults(response)
