#!/usr/bin/python3
""" A script sends a POST request to the passed URL
    with the email as a parameter
    and displays the body of the response
    uing requests
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    r = requests.post(url, data=values)
    print(r.text)
