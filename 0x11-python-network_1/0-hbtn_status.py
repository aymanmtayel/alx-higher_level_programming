#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request

URL = "https://alx-intranet.hbtn.io/status"

with request.urlopen(URL) as response:
    body = response.read()
    decoded = body.decode("utf-8")
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", decoded)
