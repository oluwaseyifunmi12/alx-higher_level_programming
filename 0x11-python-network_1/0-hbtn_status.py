#!/usr/bin/python3
"""A script to fetch a URL"""

if __name__ == "__main__":

    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as asw:
        html = asw.read()
        encoding = html.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(encoding))
