#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

from sys import argv
import requests

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    query = {"q": q}
    response = requests.post(URL, data=query)
    try:
        jsonr = response.json()
        if jsonr == {}:
            print("No result")
        else:
            print("[{}] {}".format(jsonr.get("id"), jsonr.get("name")))
    except ValueError:
        print("Not a valid JSON")
