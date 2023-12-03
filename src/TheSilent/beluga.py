import re
import time
import urllib.parse
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.puppy_requests import text
from TheSilent.clear import clear

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def beluga(host,delay=0,crawl=1,verbose=True):
    if verbose:
        clear()
    hits = []

    mal_command = ["sleep 60",
                   r"\s\l\e\e\p \6\0"]

    mal_python = [r"eval(compile('import time\ntime.sleep(60)','beluga','exec'))",
                  r"return beluga"]
    
    mal_xss = ["<iframe>beluga</iframe>",
                "<p>beluga</p>",
                "<script>alert('beluga')</script>",
                "<script>prompt('beluga')</script>"]

    hosts = kitten_crawler(host,delay,crawl,verbose)

    for _ in hosts:
        if verbose:
            print(CYAN + f"checking: {_}")
        _.rsplit("/")
        try:
            forms = re.findall("<form.+form>",text(_).replace("\n",""))

        except:
            forms = []

        # check for command injection
        for mal in mal_command:
            time.sleep(delay)
            try:
                start = time.time()
                data = text(_ + "/" + mal)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"command injection: {host}/{mal}")

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
                                    hits.append(f"command injection: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"command injection: {_} | {field_dict}")

                except:
                    pass

        # check for python injection
        for mal in mal_python:
            time.sleep(delay)
            try:
                start = time.time()
                data = text(_ + "/" + mal)
                end = time.time()
                if end - start >= 45:
                    hits.append(f"python injection: {host}/{mal}")

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
                                    hits.append(f"python injection: {action} | {field_dict}")

                            else:
                                start = time.time()
                                data = text(action,method=method_field,data=field_dict,timeout=120)
                                end = time.time()
                                if end - start >= 45:
                                    hits.append(f"python injection: {_} | {field_dict}")

                except:
                    pass

        # check for xss
        for mal in mal_xss:
            time.sleep(delay)
            try:
                data = text(_ + "/" + mal)
                if mal in data:
                    hits.append(f"xss: {host}/{mal}")

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
                                data = text(action,method=method_field,data=field_dict)
                                if mal in data:
                                    hits.append(f"xss: {action} | {field_dict}")

                            else:
                                data = text(_,method=method_field,data=field_dict)
                                if mal in data:
                                    hits.append(f"xss: {_} | {field_dict}")

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
