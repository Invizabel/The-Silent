import re
import socket
import ssl
import time
import urllib.parse
import urllib.request
from TheSilent.return_user_agent import *

verify = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
verify.check_hostname = False
verify.verify_mode = ssl.CERT_NONE

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

fake_headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language":"en-US,en;q=0.5",
                "User-Agent":return_user_agent(),
                "UPGRADE-INSECURE-REQUESTS":"1"}

def getheaders(host,method="GET",data=b"",headers=fake_headers,timeout=10):
    simple_request = urllib.request.Request(host,data=urllib.parse.urlencode(data).encode(),method=method,unverifiable=True)
    for _,__ in headers.items():
        simple_request.add_header(_,__)
    simple_response = urllib.request.urlopen(simple_request,timeout=timeout)
    return simple_response.headers

def text(host,method="GET",data=b"",headers=fake_headers,timeout=10,raw=False):
    simple_request = urllib.request.Request(host,data=urllib.parse.urlencode(data).encode(),method=method,unverifiable=True)
    for _,__ in headers.items():
        simple_request.add_header(_,__)
    simple_response = urllib.request.urlopen(simple_request,timeout=timeout)
    if raw:
        return simple_response.read()
    else:
        return simple_response.read().decode("ascii",errors="ignore")

def url(host,method="GET",data=b"",headers=fake_headers,timeout=10):
    simple_request = urllib.request.Request(host,data=urllib.parse.urlencode(data).encode(),method=method,unverifiable=True)
    for _,__ in headers.items():
        simple_request.add_header(_,__)
    simple_response = urllib.request.urlopen(simple_request,timeout=timeout)
    return simple_response.url
