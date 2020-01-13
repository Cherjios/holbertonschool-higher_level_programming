#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8"""


import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url=argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as error:
        print('Error code:', error.code)
