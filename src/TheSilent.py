import argparse
import os
import re
import socket
import ssl
import urllib.parse
import urllib.request
from os import name

def TheSilent(host,dns_only):
    if name == "nt":
        os.system("cls")
    
    else:
        os.system("clear")

    count = -1
    hits = [host]
    context = ssl.create_default_context()

    while True:
        try:
            count += 1
            print(hits[count].split(":")[0])
            
            # dns
            dns = socket.gethostbyname_ex(hits[count].split(":")[0])
            hits.append(dns[0])
            
            for i in dns[1]:
                hits.append(i)
            
            for i in dns[2]:
                hits.append(i)
                try:
               
                    hits.append(socket.getnameinfo((i,0),0)[0])
                
                except:
                    pass

            # reverse dns
            reverse_dns = socket.gethostbyaddr(hits[count].split(":")[0])
            hits.append(reverse_dns[0])
            for i in reverse_dns[1]:
                hits.append(i)
            for i in reverse_dns[2]:
                hits.append(i)
                try:
                    hits.append(socket.getnameinfo((i,0),0)[0])
                except:
                    pass


        except IndexError:
            break

        except:
            pass

        try:
            # ssl cert dns
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(10)
            tcp_socket.connect((hits[count].split(":")[0], 443))
            ssl_socket = context.wrap_socket(tcp_socket, server_hostname = hits[count].split(":")[0])
            cert = ssl_socket.getpeercert()
            tcp_socket.close()
            for dns_cert in cert["subject"]:
                if "commonName" in dns_cert[0]:
                    hits.append(dns_cert[1].replace("*.", "").split(":")[0])

        except:
            pass

        try:
            # ssl cert dns
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(10)
            tcp_socket.connect((hits[count].split(":")[0], 443))
            ssl_socket = context.wrap_socket(tcp_socket, server_hostname = hits[count].split(":")[0])
            cert = ssl_socket.getpeercert()
            tcp_socket.close()    
            for dns_cert in cert["subjectAltName"]:
                if "DNS" in dns_cert[0]:
                    hits.append(dns_cert[1].replace("*.", "").split(":")[0])

        except:
            pass

        if not dns_only:
            try:
                response = urllib.request.urlopen(f"http://{hits[count]}/robots.txt",timeout=10)
                robots = response.read().decode("ascii",errors="ignore").lower()
                sitemaps = re.findall(r"sitemap\:\s*(.+)", robots)
                for sitemap in sitemaps:
                    response = urllib.request.urlopen(sitemap,timeout=10)
                    data = response.read().decode("ascii",errors="ignore").lower()
                    hosts = re.findall(r"<.+loc>(\S+)(?=<)",data)
                    for host in host:    
                        if re.search(r"\S+\.\S+",host):
                            hits.append(urllib.parse.urlparse(host).netloc.split(":")[0])

            except:
                pass

            try:
                response = urllib.request.urlopen(f"http://{hits[count]}/sitemap.xml",timeout=10)
                data = response.read().decode("ascii",errors="ignore").lower()
                hosts = re.findall(r"<.+loc>(\S+)(?=<)",data)
                for host in host:    
                    if re.search(r"\S+\.\S+",host):
                        hits.append(urllib.parse.urlparse(host).netloc.split(":")[0])

            except:
                pass

            try:
                response = urllib.request.urlopen(f"http://web.archive.org/cdx/search/cdx?url=*.{args.host}/*&output=text&fl=original&collapse=urlkey")
                waybacks = response.read().decode("ascii",errors="ignore").lower().split("\n")
                for wayback in waybacks:
                    if re.search(r"\S+\.\S+",wayback):
                        hits.append(urllib.parse.urlparse(wayback).netloc.split(":")[0])
            
            except:
                pass

        hits = list(dict.fromkeys(hits[:]))

    hits = list(dict.fromkeys(hits[:]))
    hits.sort()
    return hits

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required = True, help = "hostname to check")
    parser.add_argument("--filename", required = False, help = "name of file")
    parser.add_argument("--dns-only", required = False, action = "store_false", help = "use dns and ssl certificates only (fast but not full)")
    args = parser.parse_args()
    hits = TheSilent(args.host, args.dns_only)
    if args.filename:
        for hit in hits:
            with open(args.filename, "a") as file:
                file.write(f"{hit}\n")
