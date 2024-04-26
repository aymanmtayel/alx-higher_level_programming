#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    data = requests.get(URL)
    print("Body response:")
    print("\t- type:", type(data.text))
    print("\t- content:", data.text)
