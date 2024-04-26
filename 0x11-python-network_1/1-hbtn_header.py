#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
displays the value of the X-Request-Id variable found in
the header of the response."""

from sys import argv
from urllib import request

URL = argv[1]
with request.urlopen(URL) as response:
    VALUE = response.headers.get('X-Request-Id')

    print(VALUE)
