#!/usr/bin/python3
"""script that takes 2 arguments and print last 10 commits done by user
in github"""

from sys import argv
import requests

if __name__ == "__main__":
    URL = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(URL)
    all_commits = response.json()
    try:
        for commit in all_commits[:10]:
            sha = commit.get("sha")
            name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {name}")
    except IndexError:
        pass
