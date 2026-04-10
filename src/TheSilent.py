
import argparse
import json
import importlib.util
import re
import socket
import subprocess
import urllib.request

apps = ["nikto", "nmap"]
pips = ["sqlmap"]
class Tools:
    def __init__(self,host):
        self.host = host
    def NIKTO(self):
        out = subprocess.run(["nikto", "-Tuning=x", f"-host={self.host}"], capture_output = True, text = True).stdout
        return out
    def NMAP(self):
        out = subprocess.run(["nmap", "-Pn", "-p-", "--script=vuln", self.host], capture_output = True, text = True).stdout
        return out
    def SQLMAP(self):
        out = subprocess.run(["sqlmap", f"--url=http://{self.host}", "--random-agent", "--level=5", "--risk=3", "--fingerprint", "--current-user", "--common-tables", " --common-columns", "--common-files", "--crawl=8", "--batch"], capture_output = True, text = True).stdout
        return out
        
class TheSilent:
    def __init__(self,host):
        self.host = host
        self.ports = [80, 443]
        self.hits = []
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
    def WAYBACK(self):
        try:
            response = urllib.request.urlopen(f"http://web.archive.org/cdx/search/cdx?url=*.{self.host}/*&output=text&fl=original&collapse=urlkey")
            links = response.read().decode("ascii", errors="ignore").lower().split("\n")
            for i in links:
                if re.search(r"\S+\.\S+", i):
                    self.hits.append(urllib.parse.urlparse(i).netloc.split(":")[0])
                    self.hits = list(dict.fromkeys(self.hits[:]))
        except:
            pass
        return self.hits

if __name__ == "__main__":
    hits = {}
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", required = True)
    parser.add_argument("-attack", action = "store_true")
    args = parser.parse_args()

    hosts = [args.host]
    count = -1
    while True:
        count += 1
        try:
            print(f"Discoving: {hosts[count]}")
            print(f"Checking: TCP")
            tcp = TheSilent(hosts[count]).TCP()
            print(f"Checking: UDP")
            udp = TheSilent(hosts[count]).UDP()
            print(f"Checking: DNS")
            dns = TheSilent(hosts[count]).DNS()
            print(f"Checking: The Wayback Machine")
            wayback = TheSilent(hosts[count]).WAYBACK()
            hits.update({hosts[count]: {"TCP": tcp, "UDP": udp, "DNS": dns, "WAYBACK": wayback}})
            if dns:
                for i in dns:
                    if i.endswith(args.host):
                        hosts.append(i)
                        hosts = list(dict.fromkeys(hosts[:]))
            if wayback:
                for i in wayback:
                    if i.endswith(args.host):
                        hosts.append(i)
                        hosts = list(dict.fromkeys(hosts[:]))
        except IndexError:
            break

    hits = json.dumps(hits, indent = 4)
    print(hits)

    if args.attack:
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

        alive = False
        hits = json.loads(hits)
        if hits[args.host]["TCP"] or hits[args.host]["UDP"] or hits[args.host]["DNS"]:
            alive = True
        if not alive:
            is_alive = input("Host seems to be down, are you sure you want to test? y/N ")
        if alive or is_alive.lower() == "y":
            choice = input("Test all targets? y/N ")
            if choice.lower() == "y":
                if "nikto" in apps:
                    for i in hosts:
                        print(f"Running nikto against: {i}")
                        nikto = Tools(i).NIKTO()
                        print(nikto)
                if "nmap" in apps:
                    for i in hosts:
                        print(f"Running nmap against: {i}")
                        nmap = Tools(i).NMAP()
                        print(nmap)
                if "sqlmap" in pips:
                    for i in hosts:
                        print(f"Running sqlmap against: {i}")
                        sqlmap = Tools(i).SQLMAP()
                        print(sqlmap)
            else:
                if "nikto" in apps:
                    print(f"Running nikto against: {args.host}")
                    nikto = Tools(args.host).NIKTO()
                    print(nikto)
                if "nmap" in apps:
                    print(f"Running nmap against: {args.host}")
                    nmap = Tools(args.host).NMAP()
                    print(nmap)
                if "sqlmap" in pips:
                    print(f"Running sqlmap against: {args.host}")
                    sqlmap = Tools(args.host).SQLMAP()
                    print(sqlmap)
        else:
            print("Aborted by user!")
