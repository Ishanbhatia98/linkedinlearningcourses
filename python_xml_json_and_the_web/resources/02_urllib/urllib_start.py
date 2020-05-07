# using urllib to request data

# TODO: import the urllib request class
import urllib.request
from pprint import pprint


def main():
    # the URL to retrieve our sample data from
    url = "http://httpbin.org/xml"

    # TODO: open the URL and retrieve some data
    result = urllib.request.urlopen(url)
    # TODO: Print the result code from the request, should be 200 OK
    print(result.status)

    # TODO: print the returned data headers
    print("Headers: ----------------------")
    pprint(result.getheaders())

    # TODO: print the returned data itself
    print("Returned data: ----------------------")
    pprint(result.read().decode('utf-8'))


if __name__ == "__main__":
    main()
