import re
import socket
import time
import urllib.parse
from TheSilent.dolphin import dolphin
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.puppy_requests import text
from TheSilent.clear import clear

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def cobra(host,delay=0,crawl=1,verbose=True):
    hits = []

    mal_python = ["__import__('time').sleep(60)",
                          "__import__('os').system('sleep 60')"]

    if verbose:
        clear()
        print(CYAN + "port scanning")

    if re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",host):
        ports = dolphin(host)

    else:
        ports = dolphin(urllib.parse.urlparse(host).netloc)

    for port in ports:
        if verbose:
            print(CYAN + f"checking port: {port}")

        for mal in mal_python:
            time.sleep(delay)
            my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            my_socket.settimeout(120)
            try:
                my_socket.connect((urllib.parse.urlparse(host).netloc,port))
                start = time.time()
                my_socket.send(mal.encode())
                data = my_socket.recv(65535).decode()
                end = time.time()
                if end - start > 45:
                    hits.append(f"python injection found on port {port} with payload {mal}: {data}")

            except TimeoutError:
                pass
        
    if re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",host):
        hosts = kitten_crawler("http://" + host,delay,crawl,verbose)

    else:
        hosts = kitten_crawler(host,delay,crawl,verbose)

    for _ in hosts:
        if verbose:
            print(CYAN + f"checking: {_}")

        try:
            forms = re.findall("<form.+form>",text(_).replace("\n",""))

        except:
            forms = []

        # check for python injection
        for mal in mal_python:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"python injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"python injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"python injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"python injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    action_bool = True
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

                    else:
                        action = action_field
                        
                except IndexError:
                    action_bool = False

                try:
                    method_field = re.findall("method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                    for in_field in input_field:
                        if re.search("name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search("type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                            name_field = re.findall("name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                            type_field = re.findall("type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                            value_field = re.findall("value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                            if type_field == "submit" or type_field == "hidden":
                                field_list.append({name_field:value_field})


                            if type_field != "submit" and type_field != "hidden":
                                field_list.append({name_field:mal})

                            field_dict = field_list[0]
                            for init_field_dict in field_list[1:]:
                                field_dict.update(init_field_dict)

                            time.sleep(delay)

                            if action:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"python injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"python injection in forms: {_} | {field_dict}")

                except:
                    pass

    if verbose:
        clear()

    hits = list(set(hits[:]))
    hits.sort()
    if len(hits) > 0:
        return hits
    else:
        return [f"we didn't find anything interesting on {host}"]
