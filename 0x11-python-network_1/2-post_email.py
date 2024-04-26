#!/usr/bin/python3
"""takes in a URL and an email,displays the body of the response."""

from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    URL = argv[1]
    email = argv[2]

    DATA_SENT = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(URL, data=DATA_SENT) as response:
        print(response.read().decode('utf-8'))
