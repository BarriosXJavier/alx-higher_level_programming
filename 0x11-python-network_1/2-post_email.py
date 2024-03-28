#!/usr/bin/python3
"""Takes a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8).
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    data = urlencode({
        'email': argv[2]
    }).encode('ascii')
    req = Request(argv[1], data)

    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
