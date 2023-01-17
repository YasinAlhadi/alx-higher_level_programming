#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
url with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    payload = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    try:
        r = requests.post(url, data=payload).json()
        if r:
            print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
