#!/usr/bin/python3
"""Displays the X-Request-Id of the given url
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
