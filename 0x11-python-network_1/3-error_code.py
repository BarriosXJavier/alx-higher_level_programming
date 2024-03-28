#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response ( utf-8).

it also handles HTTPError exceptions to print
the HTTP Status Code if an error occurs.
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as ex:
        print('Error code:', ex.code)
