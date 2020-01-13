#!/usr/bin/python3
"""Scrips that Fetches https://intranet.hbtn.io/status"""


import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
