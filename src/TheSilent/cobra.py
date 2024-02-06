import re
import time
import urllib.parse
from TheSilent.clear import clear
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.puppy_requests import text

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

def cobra(host,delay=0,crawl=1):
    clear()
    
    hits = []

    mal_command = [r"sleep 30"]

    mal_directory = [r"/admin",
                     r"/login",
                     r"/signup"]

    mal_php = [r"sleep(30)",
               r"sleep(30);"]

    mal_python = [r"time.sleep(30)",
                  r"eval(compile('import time\ntime.sleep(30)','cobra','exec'))",
                  r"eval(compile('import os\nos.system('sleep 30')','cobra','exec'))",
                  r"__import__('time').sleep(30)",
                  r"__import__('os').system('sleep 30')",
                  r'eval("__import__(\'time\').sleep(30)")',
                  r'eval("__import__(\'os\').system(\'sleep 30\')")',
                  r'exec("__import__(\'time\').sleep(30)")',
                  r'exec("__import__(\'os\').system(\'sleep 30\')")',
                  r'exec("import time\ntime.sleep(30)")',
                  r'exec("import os\nos.system(\'sleep 30\')")']
    
    mal_subdomain = ["ad",
                     "admin",
                     "byod",
                     "camera",
                     "cameras",
                     "cctv",
                     "dev",
                     "extranet",
                     "git",
                     "hr",
                     "internal",
                     "intranet",
                     "it",
                     "lan",
                     "ldap",
                     "local",
                     "private",
                     "secret",
                     "secrets",
                     "test",
                     "wan"]
    
    mal_xss = [r"<iframe>Cobra</iframe>",
               r"<p>cobra</p>",
               r"<script>alert('Cobra')</script>",
               r"<script>await sleep(30);</script>",
               r"<script>prompt('Cobra')</script>",
               r"<strong>cobra</strong>",
               r"<style>body{background-color:red;}</style>",
               r"<title>cobra</title>"]

    print(CYAN + f"checking for sensitive subdomains on {host}")
    for mal in mal_subdomain:
        time.sleep(delay)
        try:
            print(f"checking: http://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))
            text("http://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))
            hits.append("found sensitive subdomain: http://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))

        except:
            pass

        try:
            print(f"checking: https://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))
            text("https://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))
            hits.append("found sensitive subdomain: https://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))

        except:
            pass

    print(CYAN + f"crawling: {host}")
    hosts = kitten_crawler(host,delay,crawl)

    for mal in mal_directory:
        time.sleep(delay)
        try:
            print(CYAN + host.rstrip("/") + mal)
            text(host.rstrip("/") + mal)
            hosts.append(host.rstrip("/") + mal)
        except:
            pass

    hosts = list(dict.fromkeys(hosts[:]))
    clear()
    for _ in hosts:
        if urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(_).netloc:
            print(CYAN + f"checking: {_}")
            try:
                forms = re.findall("<form.+form>",text(_).replace("\n",""))

            except:
                forms = []

            # check for command injection
            for mal in mal_command:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"command injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"command injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"command injection in referer ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall("<input.+?>",form)
                    try:
                        action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall("method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search("name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search("type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall("name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall("type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall("value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
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
                                    if end - start >= 25:
                                        hits.append(f"command injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start >= 25:
                                        hits.append(f"command injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for python injection
            for mal in mal_python:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"python injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"python injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"python injection in referer ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall("<input.+?>",form)
                    try:
                        action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall("method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search("name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search("type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall("name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall("type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall("value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
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
                                    if end - start >= 25:
                                        hits.append(f"python injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start >= 25:
                                        hits.append(f"python injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for php injection
            for mal in mal_php:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"php injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"php injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start >= 25:
                        hits.append(f"php injection in referer ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall("<input.+?>",form)
                    try:
                        action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall("method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search("name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search("type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall("name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall("type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall("value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
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
                                    if end - start >= 25:
                                        hits.append(f"php injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start >= 25:
                                        hits.append(f"php injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for xss
            for mal in mal_xss:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    data = text(_ + "/" + mal)
                    if mal in data:
                        hits.append(f"xss in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"Cookie",mal})
                    if mal in data:
                        hits.append(f"xss in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"Referer",mal})
                    if mal in data:
                        hits.append(f"xss in referer ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall("<input.+?>",form)
                    try:
                        action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall("method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search("name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search("type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall("name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall("type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall("value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action:
                                    data = text(action,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"xss in forms: {action} | {field_dict}")

                                else:
                                    data = text(action,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"xss in forms: {_} | {field_dict}")

                    except:
                        pass

    clear()
    hits = list(set(hits[:]))
    hits.sort()

    if len(hits) > 0:
        for hit in hits:
            print(RED + hit)
            with open("cobra.log", "a") as file:
                file.write(hit + "\n")

    else:
        print(GREEN + f"we didn't find anything interesting on {host}")
        with open("cobra.log", "a") as file:
                file.write(f"we didn't find anything interesting on {host}\n")
