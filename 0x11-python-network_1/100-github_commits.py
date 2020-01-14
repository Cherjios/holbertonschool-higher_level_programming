#!/usr/bin/python3
"""
 script that list 10 commits from the most recent to oldest
"""

from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    l = r.json()
    try:
        for i in range(10):
            print(l[i].get('sha'), l[i].get('commit')
                  .get('author').get('name'), sep=": ")
    except:
        pass
