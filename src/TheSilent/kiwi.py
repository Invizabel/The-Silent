import hashlib
import ipaddress
import re
import socket
import threading
from TheSilent.clear import clear
from TheSilent.puppy_requests import *

CYAN = "\033[1;36m"

hits = []

def juice(host):
    global hits

    fingerprint_images = {"Content Keeper": "06c673c63c930a65265e75e32ea49c6095c3628c5f82c8c06181a93a84e7948f",
                          "OpenVAS": "2baba8da070e1911ddfae6b4843401b735a9c95e14f72699662e9fe9d9f70b00"}

    fingerprint_paths = ["/favicon.ico",
                         "/img/favicon.png"]

    web_ports = [9392,8443,8080,443,80] # 9392 is the default OpenVAS port

    try:
        hits.append(f"{host} | {socket.gethostbyname_ex(host)}")

    except:
        pass

    ports = []
    for port in web_ports:
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(10)
            tcp_socket.connect((str(host), port))
            tcp_socket.close()
            ports.append(port)

        except:
            pass
        

    for port in ports:
        for path in fingerprint_paths:
            if port == 80:
                try:
                    data = text(f"http://{host}{path}", raw=True)
                    checksum = hashlib.sha256(data).hexdigest()
                    for fingerprint in fingerprint_images.items():
                        if checksum == fingerprint[1]:
                            hits.append(f"{host} | favicon fingerprint: " + fingerprint[0])

                except:
                    continue

            if port == 443:
                try:
                    data = text(f"https://{host}{path}", raw=True)
                    checksum = hashlib.sha256(data).hexdigest()
                    for fingerprint in fingerprint_images.items():
                        if checksum == fingerprint[1]:
                            hits.append(f"{host} | favicon fingerprint: " + fingerprint[0])

                except:
                    continue

            else:
                try:
                    data = text(f"https://{host}:{port}{path}", raw=True)
                    checksum = hashlib.sha256(data).hexdigest()
                    for fingerprint in fingerprint_images.items():
                        if checksum == fingerprint[1]:
                            hits.append(f"{host} | favicon fingerprint: " + fingerprint[0])

                except:
                    continue

        if port == 80:
            try:
                hits.append(f"{host} | request headers fingerprint: " + re.findall(f"server:(.+)", str(getheaders(f"http://{host}")).lower())[0])

            except:
                pass

        if port == 443:
            try:
                hits.append(f"{host} | request headers fingerprint: " + re.findall(f"server:(.+)", str(getheaders(f"https://{host}")).lower())[0])

            except:
                pass

        else:
            try:
                hits.append(f"{host} | request headers fingerprint: " + re.findall(f"server:(.+)", str(getheaders(f"http://{host}:{port}")).lower())[0])

            except:
                pass

def kiwi(host):
    global hits
    hits = []
    
    clear()
    
    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}", host):
        thread_list = []
        thread_count = 0

        print(f"checking: {host}")

        for ip in list(ipaddress.ip_network(host, strict=False).hosts()):
            thread_count += 1
            my_thread = threading.Thread(target = juice, args = (str(ip),))
            thread_list.append(my_thread)
            my_thread.start()

            if thread_count == 255:
                for thread in thread_list:
                    thread.join()

                thread_count = 0
                thread_list = []

        
        for thread in thread_list:
            thread.join()

        hits = list(set(hits[:]))
        hits.sort()
        with open("kiwi.log", "a") as file:
            for hit in hits:
                file.write(f"{hit}\n")
                print(CYAN + hit)

    else:
        print(CYAN + f"checking: {host}")
        my_thread = threading.Thread(target = juice, args = (host,))
        my_thread.start()
        my_thread.join()

        hits = list(set(hits[:]))
        hits.sort()
        with open("kiwi.log", "a") as file:
            for hit in hits:
                file.write(f"{hit}\n")
                print(CYAN + hit)
