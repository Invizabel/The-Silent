import argparse
import http.cookiejar
import json
import importlib.util
import socket
import random
import re
import subprocess
import time
import urllib.parse
import urllib.request

apps = ["nmap"]
pips = ["sqlmap"]
class Tools:
    def __init__(self,host):
        self.host = host
    def nmap(self):
        out = subprocess.run(["nmap", "-Pn", "-p-", self.host], capture_output = True, text = True).stdout
        print(out)
    def sqlmap(self):
        out = subprocess.run(["sqlmap", f"--url=http://{self.host}", "--random-agent", "--level=5", "--risk=3", "--fingerprint", "--current-user", "--common-tables", " --common-columns", "--common-files", "--crawl=8", "--batch"], capture_output = True, text = True).stdout
        print(out)
        
class Parser:
    def __init__(self,data):
        self.data = data
    def Links(self):
        return [i.rstrip("/") for i in list(dict.fromkeys(re.findall(r"(?:href|src|action|data|cite|poster|content|background|profile|manifest|srcset|ping)\s*=\s*[\"'](\S+?)(?=[\"'\\])",self.data)))] + [i.rstrip("/") for i in list(dict.fromkeys(re.findall(r"src\s*=\s*[\"\'](\S+?)(?=[\"\'\\])", self.data)))]

class TheSilent:
    def __init__(self,host):
        self.host = host
        self.hits = []
        self.ports = [80, 443]
    def TCP(self):
        for i in self.ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(10)
                s.connect((self.host, i))
                s.close()
                return True
            except ConnectionRefusedError:
                return True
            except:
                pass
        return False
    def UDP(self):
        for i in self.ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(10)
                s.sendto(b"", (self.host, i))
                s.recvfrom(1)
                return True
            except ConnectionRefusedError:
                return True
            except:
                pass
        return False
    def DNS(self):
        try:
            addr = socket.gethostbyaddr(self.host)
            if addr[1]:
                for i in addr[1]:
                    if i.endswith(self.host):
                        self.hits.append(i)
                return self.hits
        except:
            return None
    def CRAWL(self):
        self.hits.append(f"http://{self.host}/")
        dead = []
        count = -1
        while True:
            count += 1
            self.hits = list(dict.fromkeys(self.hits[:]))
            time.sleep(random.uniform(1,8))
            try:
                fake_headers = {"Accept":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36","Accept-Encoding":"deflate","Accept-Language":"en-US,en;q=0.5","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36","UPGRADE-INSECURE-REQUESTS":"1"}
                cookie_jar = http.cookiejar.CookieJar()
                opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
                urllib.request.install_opener(opener)
                request = urllib.request.Request(url = self.hits[count], headers = fake_headers, method = "GET")
                response = urllib.request.urlopen(request, timeout = 10)
                if response.status == 200:
                    print(f"Found: {self.hits[count]}")
                    links = Parser(response.read().decode()).Links()
                    for i in links:
                        temp = i.rstrip("/")
                        if i.startswith("https://") or i.startswith("http://"):
                            if self.host in urllib.parse.urlparse(i).netloc:
                                if temp + "/" not in dead:
                                    self.hits.append(temp + "/")
                        elif i.startswith("/"):
                            if self.host in "http://" + urllib.parse.urlparse(response.url).netloc.rstrip("/") + temp + "/" and "http://" + urllib.parse.urlparse(response.url).netloc.rstrip("/") + temp + "/" not in dead:
                                self.hits.append("http://" + urllib.parse.urlparse(response.url).netloc.rstrip("/") + temp + "/")
                        elif not i.startswith("https://") and not i.startswith("http://"):
                            if self.host in "http://" + urllib.parse.urlparse(response.url).netloc.rstrip("/") + "/" + temp + "/" and "http://" + urllib.parse.urlparse(response.url).netloc.rstrip("/") + "/" + temp + "/" not in dead:
                                self.hits.append("http://" + urllib.parse.urlparse(response.url).netloc.rstrip("/") + "/" + temp + "/")
            except IndexError:
                break
            except:
                dead.append(self.hits[count])
                self.hits.remove(self.hits[count])
        return self.hits

if __name__ == "__main__":
    hits = {}
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", required = True)
    parser.add_argument("-filename", required = False)
    args = parser.parse_args()
    for i in pips:
        if not importlib.util.find_spec(i):
            print(f"Skipping: {i}")
            pips.remove(i)
        else:
            print(f"Found: {i}")

    for i in apps:
        try:
            subprocess.run(["which", i], capture_output=True, text=True, check=True)
            print(f"Found: {i}")
        except subprocess.CalledProcessError:
            print(f"Skipping: {i}")
            apps.remove(i)
    hosts = [args.host]
    count = -1
    while True:
        count += 1
        try:
            hosts = list(dict.fromkeys(hosts[:]))
            print(f"Discoving: {hosts[count]}")
            print(f"Checking: TCP")
            tcp = TheSilent(hosts[count]).TCP()
            print(f"Checking: UDP")
            udp = TheSilent(hosts[count]).UDP()
            print(f"Checking: DNS")
            dns = TheSilent(hosts[count]).DNS()
            print(f"Crawling: {hosts[count]}")
            crawl = TheSilent(hosts[count]).CRAWL()
            hits.update({hosts[count]: {"TCP": tcp, "UDP": udp, "DNS": dns, "CRAWL": crawl}})
            if dns:
                for i in dns:
                    if i.endswith(args.host):
                        hosts.append(i)
            if crawl:
                for i in crawl:
                    hosts.append(urllib.parse.urlparse(i).netloc)
        except IndexError:
            break

    for key in hits.keys():
        if "nmap" in apps:
            print(f"Running nmap against: {key}")
            tool = Tools(key).nmap()
        if "sqlmap" in pips:
            print(f"Running sqlmap against: {key}")
            tool = Tools(key).sqlmap()
    hits = json.dumps(hits, indent = 4)
    if args.filename:
        with open(args.filename, "w") as file:
            file.write(hits)
    print(hits)