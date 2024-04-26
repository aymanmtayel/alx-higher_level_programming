#!/usr/bin/python3
"""script that takes in a URL, and display the header of the response."""

from sys import argv
from urllib import request


if __name__ == "__main__":
    URL = argv[1]
    with request.urlopen(URL) as response:
        VALUE = response.headers.get('X-Request-Id')
        print(VALUE)
