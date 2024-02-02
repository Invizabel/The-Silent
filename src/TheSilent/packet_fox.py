import re
import ssl
import socket
import urllib.parse

def https(host,port=443,timeout=10,mode="text"):
    if not host.endswith("/"):
        host += "/"
    history = [host]
    context = ssl.create_default_context()
    context.check_hostname = False
    with socket.create_connection((urllib.parse.urlparse(host).netloc.split(":")[0].split("/")[0], int(port))) as sock:
        with context.wrap_socket(sock, server_hostname=urllib.parse.urlparse(host).netloc.split(":")[0].split("/")[0]) as ssock:
                ssock.settimeout(timeout)
                ssock.send(b"GET " + urllib.parse.urlparse(host).path.encode()  + b" HTTP/1.1\r\nHost: " + urllib.parse.urlparse(host).netloc.split(":")[0].split("/")[0].encode() + b"\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: identity\r\nDNT: 1\r\nSec-GPC: 1\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\n\r\n")
                data = ssock.recv(4096)
                print(data.decode())
                if data.lower().startswith(b"http/1.1 30") and mode != "status":
                    for i in range(1000):
                        if data.lower().startswith(b"http/1.1 30"):
                            location = re.findall("location\s*:\s*(https://\S+)", data.decode().lower())[0]
                            history.append(location)
                            ssock.send(b"GET " + urllib.parse.urlparse(location).path.encode()  + b" HTTP/1.1\r\nHost: " + urllib.parse.urlparse(location).netloc.split(":")[0].split("/")[0].encode() + b"\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: identity\r\nDNT: 1\r\nSec-GPC: 1\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\n\r\n")
                            data = ssock.recv(4096)
                            
                        elif data.lower().startswith(b"http/1.1 200"):
                            ssock.send(b"GET " + urllib.parse.urlparse(location).path.encode()  + b" HTTP/1.1\r\nHost: " + urllib.parse.urlparse(location).netloc.split(":")[0].split("/")[0].encode() + b"\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: identity\r\nDNT: 1\r\nSec-GPC: 1\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\n\r\n")
                            while True:
                                data += ssock.recv(4096)
                                if data.count(b"HTTP/1.1") > 1:
                                    break
                            result = b"HTTP/1.1" + data.split(b"HTTP/1.1")[0] + data.split(b"HTTP/1.1")[1]
                            result = re.sub(b"\r\n[0-9][0-9a-f]+",b"",result)
                            result = re.sub(b"\r\n[0]",b"",result)
                            if mode == "header":
                                if b"\r\n\r\n" in result:
                                    result = result.split(b"\r\n\r\n")[0]
                                elif b"\n\n" in result:
                                    result = result.split(b"\n\n")[0]
                                return result.decode(errors="ignore")
                            elif mode == "raw":
                                if b"\r\n\r\n" in result:
                                    result = result.split(b"\r\n\r\n")[1]
                                elif b"\n\n" in result:
                                    result = result.split(b"\n\n")[1]
                                return result
                            elif mode == "text":
                                if b"\r\n\r\n" in result:
                                    result = result.split(b"\r\n\r\n")[1]
                                elif b"\n\n" in result:
                                    result = result.split(b"\n\n")[1]
                                return result.decode(errors="ignore")
                            elif mode == "history":
                                return history
                            

                        elif not data.lower().startswith(b"http/1.1"):
                            ssock.send(b"GET " + urllib.parse.urlparse(location).path.encode()  + b" HTTP/1.1\r\nHost: " + urllib.parse.urlparse(location).netloc.split(":")[0].split("/")[0].encode() + b"\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: identity\r\nDNT: 1\r\nSec-GPC: 1\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\n\r\n")
                            data = ssock.recv(4096)

                        else:
                            return int(re.findall("http/1.1\s*(\d+)?", data.decode().lower())[0])

                elif data.lower().startswith(b"http/1.1 200") and mode != "status":
                    ssock.send(b"GET " + urllib.parse.urlparse(host).path.encode()  + b" HTTP/1.1\r\nHost: " + urllib.parse.urlparse(host).netloc.split(":")[0].split("/")[0].encode() + b"\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: identity\r\nDNT: 1\r\nSec-GPC: 1\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\n\r\n")
                    while True:
                        data += ssock.recv(4096)
                        if data.count(b"HTTP/1.1") > 1:
                            break

                    result = b"HTTP/1.1" + data.split(b"HTTP/1.1")[0] + data.split(b"HTTP/1.1")[1]
                    result = re.sub(b"\r\n[0-9][0-9a-f]+",b"",result)
                    result = re.sub(b"\r\n[0]",b"",result)
                    if mode == "header":
                        if b"\r\n\r\n" in result:
                            result = result.split(b"\r\n\r\n")[0]
                        elif b"\n\n" in result:
                            result = result.split(b"\n\n")[0]
                        return result.decode(errors="ignore")
                    elif mode == "raw":
                        if b"\r\n\r\n" in result:
                            result = result.split(b"\r\n\r\n")[1]
                        elif b"\n\n" in result:
                            result = result.split(b"\n\n")[1]
                        return result
                    elif mode == "text":
                        if b"\r\n\r\n" in result:
                            result = result.split(b"\r\n\r\n")[1]
                        elif b"\n\n" in result:
                            result = result.split(b"\n\n")[1]
                        return result.decode(errors="ignore")

                    elif mode == "history":
                        return history

                    return int(re.findall("http/1.1\s*(\d+)?", data.decode().lower())[0])

                elif mode == "status":
                    return int(re.findall("http/1.1\s*(\d+)?", data.decode().lower())[0])
