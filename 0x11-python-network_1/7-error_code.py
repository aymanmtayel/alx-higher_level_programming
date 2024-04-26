#!/usr/bin/python3
"""Python script that takes in a URL, displays the body of the response."""

from sys import argv
import requests

if __name__ == "__main__":
    URL = argv[1]
    response = requests.get(URL)
    status = response.status_code
    if status > 400:
        print("Error code:", status)
    else:
        print(response.text)
