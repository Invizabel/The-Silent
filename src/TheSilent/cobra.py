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

    mal_command = [r"$(echo -e '\x73\x6C\x65\x65\x70\x20\x36\x30')"]
    new_mal = []
    for mal in mal_command:
        new_mal.append(r"$(echo -e '\x73\x6C\x65\x65\x70\x20\x36\x30')")
        new_mal.append(urllib.parse.quote(mal))
        new_mal.append(urllib.parse.quote(urllib.parse.quote(mal)))
    mal_command = new_mal[:]
    
    mal_emoji = [r"&#128124;",
                 r"&#128293;",
                 r"&#128568;",
                 r"&#128049;",
                 r"&#127814;",
                 r"&#x1F47C",
                 r"&#x1F525",
                 r"&#x1F638",
                 r"&#x1F431",
                 r"&#x1F346"]

    mal_ms_sql = [r'WAITFOR DELAY "00:01"']
    new_mal = []
    for mal in mal_ms_sql:
        new_mal.append(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))
        new_mal.append(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000")))
        new_mal.append(urllib.parse.quote(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))))
    mal_ms_sql = new_mal[:]

    mal_my_sql = [r"SELECT SLEEP(60);"]
    new_mal = []
    for mal in mal_my_sql:
        new_mal.append(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))
        new_mal.append(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000")))
        new_mal.append(urllib.parse.quote(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))))
    mal_my_sql = new_mal[:]

    mal_oracle_sql = [r"DBMS_LOCK.sleep(60);",
                  r"DBMS_SESSION.sleep(60);"]
    new_mal = []
    for mal in mal_oracle_sql:
        new_mal.append(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))
        new_mal.append(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000")))
        new_mal.append(urllib.parse.quote(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))))
    mal_oracle_sql = new_mal[:]

    mal_postgresql = [r"pg_sleep(60);",
                      r"PERFORM pg_sleep(60);",
                      r"SELECT pg_sleep(60);"]
    new_mal = []
    for mal in mal_postgresql:
        new_mal.append(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))
        new_mal.append(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000")))
        new_mal.append(urllib.parse.quote(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))))
    mal_postgresql = new_mal[:]
    
    mal_python = [r"time.sleep(60)",
                  r"eval(compile('import time\ntime.sleep(60)','cobra','exec'))",
                  r"eval(compile('import os\nos.system('sleep 60')','cobra','exec'))",
                  r"__import__('time').sleep(60)",
                  r"__import__('os').system('sleep 60')",
                  r'eval("__import__(\'time\').sleep(60)")',
                  r'eval("__import__(\'os\').system(\'sleep 60\')")',
                  r'exec("__import__(\'time\').sleep(60)")',
                  r'exec("__import__(\'os\').system(\'sleep 60\')")',
                  r'exec("import time\ntime.sleep(60)")',
                  r'exec("import os\nos.system(\'sleep 60\')")']
    new_mal = []
    for mal in mal_python:
        new_mal.append(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))
        new_mal.append(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000")))
        new_mal.append(urllib.parse.quote(urllib.parse.quote(str(" " + " ".join(format(ord(char), "x") for char in mal)).replace(" ", r"\U000000"))))
    mal_python = new_mal[:]

    print(CYAN + f"crawling: {host}")
    hosts = kitten_crawler(host,delay,crawl)
            
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
                    if end - start > 45:
                        hits.append(f"command injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"command injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
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

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"command injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"command injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for emoji injection
            for mal in mal_emoji:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    data = text(_ + "/" + mal)
                    if mal in data:
                        hits.append(f"emoji injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"Cookie",mal})
                    if mal in data:
                        hits.append(f"emoji injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"Referer",mal})
                    if mal in data:
                        hits.append(f"emoji injection in referer ({mal}): {_}")

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

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    data = text(action,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"emoji injection in forms: {action} | {field_dict}")

                                else:
                                    data = text(_,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"emoji injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for ms sql injection
            for mal in mal_ms_sql:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"ms sql injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"ms sql injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"ms sql injection in referer ({mal}): {_}")

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

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"ms sql injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"ms sql injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for my sql injection
            for mal in mal_my_sql:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"my sql injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"my sql injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"my sql injection in referer ({mal}): {_}")

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

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"my sql injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"my sql injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for oracle sql injection
            for mal in mal_oracle_sql:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"oracle sql injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"oracle sql injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"oracle sql injection in referer ({mal}): {_}")

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

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"oracle sql injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"oracle sql injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for postgresql injection
            for mal in mal_postgresql:
                print(CYAN + f"checking {_} with payload {mal}")
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"postgresql injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"postgresql injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"postgresql injection in referer ({mal}): {_}")

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

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"postgresql injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"postgresql injection in forms: {_} | {field_dict}")

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
                    if end - start > 45:
                        hits.append(f"python injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
                        hits.append(f"python injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout = 120)
                    end = time.time()
                    if end - start > 45:
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

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"python injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict,timeout=120)
                                    end = time.time()
                                    if end - start > 45:
                                        hits.append(f"python injection in forms: {_} | {field_dict}")

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
