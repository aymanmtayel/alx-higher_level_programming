#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
displays the value of the X-Request-Id variable found in
the header of the response."""

import sys
import urllib.request

URL = sys.argv[1]
with urllib.request.urlopen(URL) as response:
    VALUE = response.headers.get('X-Request-Id')

    print(VALUE)
