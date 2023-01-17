#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    pswd = sys.argv[2]
    r = requests.get(url, auth=(user, pswd))
    try:
        print(r.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
