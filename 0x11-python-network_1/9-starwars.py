#!/usr/bin/python3
"""
Script that takes in a string and sends a search request
to the Star WarsAPI
"""


import requests
from sys import argv


if __name__ == "__main__":
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    try:
        r = requests.get('https://swapi.co/api/people/?search={}'.format(arg))
        j = r.json()
        if j:
            print('Number of results:', j['count'])
            for i in j.get('results'):
                print(i.get('name'))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
