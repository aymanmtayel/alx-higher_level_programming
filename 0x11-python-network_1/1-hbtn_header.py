#!/usr/bin/python3
"""script that takes in a URL, and display the header of the response."""

import sys
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        VALUE = response.headers.get('X-Request-Id')
        print(VALUE)
