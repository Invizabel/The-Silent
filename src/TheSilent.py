import argparse
import ftplib
import http.cookiejar
import socket
import urllib.request
from clear import clear

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

fake_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
                "UPGRADE-INSECURE-REQUESTS": "1"}

cookie_jar = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(cookie_handler)
urllib.request.install_opener(opener)

def TheSilent():
    clear()

    parser = argparse.ArgumentParser()
    parser.add_argument("-host", required = True)
    args = parser.parse_args()

    hits = []

    methods = ["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]

    print(f"{CYAN}checking: {args.host}")

    dns = socket.getfqdn(args.host)
    print(f"{RED}FQDN {dns}")
    
    try:
        ftp_client = ftplib.FTP(args.host, timeout = 10)
        ftp_client.login()
        ftp_client.quit()
        print(f"{RED}ANONYMOUS FTP ALLOWED")

    except:
        pass

    try:
        ftp_client = ftplib.FTP_TLS(args.host, timeout = 10)
        ftp_client.login()
        ftp_client.quit()
        print(f"{RED}ANONYMOUS FTP TLS ALLOWED")

    except:
        pass

    ssl_support = False
    try:
        simple_request = urllib.request.Request(f"https://{args.host}", headers = fake_headers, unverifiable = True, method = "GET")
        simple_response = opener.open(simple_request, timeout = 10)
        ssl_support = True

    except:
        pass

    if ssl_support:
        try:
            simple_request = urllib.request.Request(f"https://{args.host}", headers = fake_headers, unverifiable = True, method = "GET")
            simple_response = opener.open(simple_request, timeout = 10).headers
            banner = simple_response["server"]
            print(f"{RED}WEB BANNER {banner}")

        except:
            pass

    else:
        try:
            simple_request = urllib.request.Request(f"http://{args.host}", headers = fake_headers, unverifiable = True, method = "GET")
            simple_response = opener.open(simple_request, timeout = 10).headers
            banner = simple_response["server"]
            print(f"{RED}WEB BANNER {banner}")

        except:
            pass

    for i in methods:
        if ssl_support:
            try:
                simple_request = urllib.request.Request(f"https://{args.host}", headers = fake_headers, unverifiable = True, method = i)
                simple_response = opener.open(simple_request, timeout = 10)
                print(f"{RED}{i} METHOD ALLOWED")

            except:
                pass

        else:
            try:
                simple_request = urllib.request.Request(f"http://{args.host}", headers = fake_headers, unverifiable = True, method = i)
                simple_response = opener.open(simple_request, timeout = 10)
                print(f"{RED}{i} METHOD ALLOWED")
                
            except:
                pass

    if ssl_support:
        try:
            simple_request = urllib.request.Request(f"https://{args.host}", headers = fake_headers, unverifiable = True, method = "*")
            simple_response = opener.open(simple_request, timeout = 10)
            print(f"{RED}ANY METHOD ALLOWED")

        except:
            pass

    else:
        try:
            simple_request = urllib.request.Request(f"http://{args.host}", headers = fake_headers, unverifiable = True, method = "*")
            simple_response = opener.open(simple_request, timeout = 10)
            print(f"{RED}ANY METHOD ALLOWED")

        except:
            pass

if __name__ == "__main__":

    TheSilent()


