#!/usr/bin/python3
"""Python script that takes in a URL,displays the body of the response"""

from sys import argv
from urllib import request, error

if __name__ == "__main__":
    URL = argv[1]
    try:
        with request.urlopen(URL) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print("Error code:", e.code)
