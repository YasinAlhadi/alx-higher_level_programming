#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL"""
import requests
import sys

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], params=payload)
    print(r.text)
