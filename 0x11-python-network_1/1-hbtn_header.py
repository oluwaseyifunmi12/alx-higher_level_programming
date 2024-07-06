#!/usr/bin/python3
""" A script to get X-request-id info from the header
    uses sys to get url from command line
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        resp = dict(response.headers).get("X-Request-Id")
        print(resp)
