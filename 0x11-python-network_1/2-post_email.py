#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email}).encode('ascii')
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
