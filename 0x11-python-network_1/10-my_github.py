#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    URL = "https://api.github.com/user"
    user = argv[1]
    paswd = argv[2]
    login = HTTPBasicAuth(user, paswd)
    response = requests.get(URL, auth=login)
    print(response.json().get("id"))
