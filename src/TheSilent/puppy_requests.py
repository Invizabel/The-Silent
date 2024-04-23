import gzip
import http.cookiejar
import socket
import ssl
import urllib.parse
import urllib.request
import zlib
from urllib.error import HTTPError
from TheSilent.return_user_agent import *

ssl._create_default_https_context = ssl._create_unverified_context

fake_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": return_user_agent(),
                "UPGRADE-INSECURE-REQUESTS": "1"}

# create a cookie jar to store cookies
cookie_jar = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(cookie_handler)
urllib.request.install_opener(opener)

def getheaders(host,method="GET",data=b"",headers={},timeout=10):
    for i in range(3):
        try:
            socket.setdefaulttimeout(timeout)
            if data:
                simple_request = urllib.request.Request(host,data=urllib.parse.urlencode(data).encode(),method=method,unverifiable=True)   

            else:
                simple_request = urllib.request.Request(host,method=method,unverifiable=True)

            for key,value in fake_headers.items():
                simple_request.add_header(key,value)

            if headers:
                for key,value in headers.items():
                    simple_request.add_header(key,value)

            simple_response = opener.open(simple_request,timeout=timeout)

            return simple_response.headers

        except TimeoutError:
            pass

def status_code(host,method="GET",data=None,headers={},timeout=10):
    for i in range(3):
        try:
            socket.setdefaulttimeout(timeout)
            if data:
                simple_request = urllib.request.Request(host,data=urllib.parse.urlencode(data).encode(),method=method,unverifiable=True)   

            else:
                simple_request = urllib.request.Request(host,method=method,unverifiable=True)

            for key,value in fake_headers.items():
                simple_request.add_header(key,value)

            if headers:
                for key,value in headers.items():
                    simple_request.add_header(key,value)

            try:
                simple_response = opener.open(simple_request,timeout=timeout)
                status_value = int(simple_response.status)

            except HTTPError as error:
                status_value = int(error.code)

            return status_value

        except TimeoutError:
            pass

def text(host,method="GET",data=None,headers={},timeout=10,raw=False):
    for i in range(3):
        try:
            socket.setdefaulttimeout(timeout)
            if data:
                simple_request = urllib.request.Request(host,data=urllib.parse.urlencode(data).encode(),method=method,unverifiable=True)   

            else:
                simple_request = urllib.request.Request(host,method=method,unverifiable=True)

            for key,value in fake_headers.items():
                simple_request.add_header(key,value)

            if headers:
                for key,value in headers.items():
                    simple_request.add_header(key,value)

            simple_response = opener.open(simple_request,timeout=timeout)
            content_encoding = simple_response.headers.get("Content-Encoding", "")
            data = simple_response.read()

            if "gzip" in content_encoding:
                if raw:
                    return gzip.decompress(data)

                else:
                    return gzip.decompress(data).decode(errors="ignore")

            elif "deflate" in content_encoding:
                try:
                    if raw:
                        return zlib.decompress(data, -zlib.MAX_WBITS)

                    else:
                        return zlib.decompress(data, -zlib.MAX_WBITS).decode(errors="ignore")

                except zlib.error:
                    if raw:
                        return zlib.decompress(data)

                    else:
                        return zlib.decompress(data).decode(errors="ignore")

            else:
                if raw:
                    return data

                else:
                    return data.decode(errors="ignore")

        except TimeoutError:
            pass

def url(host,method="GET",data=None,headers={},timeout=10):
    for i in range(3):
        try:
            socket.setdefaulttimeout(timeout)
            if data:
                simple_request = urllib.request.Request(host,data=urllib.parse.urlencode(data).encode(),method=method,unverifiable=True)   

            else:
                simple_request = urllib.request.Request(host,method=method,unverifiable=True)

            for key,value in fake_headers.items():
                simple_request.add_header(key,value)

            if headers:
                for key,value in headers.items():
                    simple_request.add_header(key,value)

            simple_response = opener.open(simple_request,timeout=timeout)
            return str(simple_response.url)

        except TimeoutError:
            pass
