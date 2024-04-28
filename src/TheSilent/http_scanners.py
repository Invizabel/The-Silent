import re
import time
import urllib.parse
from urllib.error import HTTPError
from TheSilent.payloads import *
from TheSilent.puppy_requests import text

# check for bash injection time based payload
def bash_time_scanner(_, delay, mal_bash, forms):
    hits = []
    status_hits = []
    for mal in mal_bash:
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"bash injection in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"bash injection in url: {_}/{mal}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"bash injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"bash injection in method ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"bash injection in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"bash injection in cookie ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"bash injection in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"bash injection in referer ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"bash injection in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"bash injection in x-forwarded-for ({mal}): {_}")

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            start = time.time()
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"bash injection in forms: {action} | {field_dict}")

                        else:
                            start = time.time()
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"bash injection in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                if error.code == 504:
                    if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                        
                        hits.append(f"bash injection in forms: {action} | {field_dict}")

                    else:
                        
                        hits.append(f"bash injection in forms: {_} | {field_dict}")

            except:
                pass

    return hits, status_hits

# check for directory traversal
def directory_traversal_scanner(_, delay, mal_directory):
    hits = []
    status_hits  = []
    for mal in mal_directory:
        try:
            text(_ + mal)
            hits.append(_ + mal)
            
        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

    return hits, status_hits

# check for emoji injection based payload
def emoji_scanner(_, delay, mal_emoji, forms):
    hits = []
    status_hits = []
    for mal in mal_emoji:
        try:
            time.sleep(delay)
            data = text(_ + "/" + mal)
            status_hits.append(200)
            if mal in data:
                hits.append(f"emoji injection in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            if mal in data:
                hits.append(f"emoji injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Cookie": mal})
            status_hits.append(200)
            if mal in data:
                hits.append(f"emoji injection in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Referer": mal})
            status_hits.append(200)
            if mal in data:
                hits.append(f"emoji injection in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"X-Forwarded-For": mal})
            status_hits.append(200)
            if mal in data:
                hits.append(f"emoji injection in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            data = text(action, method = method_field, data = field_dict)
                            status_hits.append(200)
                            if mal in data:
                                hits.append(f"emoji injection in forms: {action} | {field_dict}")

                        else:
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            if mal in data:
                                hits.append(f"emoji injection in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)

            except:
                pass

    return hits, status_hits

# check for mssql injection time based payload
def mssql_time_scanner(_, delay, mal_mssql, forms):
    hits = []
    status_hits = []
    for mal in mal_mssql:
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mssql injection in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mssql injection in url: {_}/{mal}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mssql injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mssql injection in method ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mssql injection in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mssql injection in cookie ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mssql injection in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mssql injection in referer ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mssql injection in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mssql injection in x-forwarded-for ({mal}): {_}")

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            start = time.time()
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"mssql injection in forms: {action} | {field_dict}")

                        else:
                            start = time.time()
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"mssql injection in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                if error.code == 504:
                    if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                        hits.append(f"mssql injection in forms: {action} | {field_dict}")

                    else:
                        hits.append(f"mssql injection in forms: {_} | {field_dict}")

            except:
                pass

    return hits, status_hits

# check for mysql injection time based payload
def mysql_time_scanner(_, delay, mal_mysql, forms):
    hits = []
    status_hits = []
    for mal in mal_mysql:
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mysql injection in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mysql injection in url: {_}/{mal}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mysql injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mysql injection in method ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mysql injection in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mysql injection in cookie ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mysql injection in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mysql injection in referer ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"mysql injection in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"mysql injection in x-forwarded-for ({mal}): {_}")

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            start = time.time()
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"mysql injection in forms: {action} | {field_dict}")

                        else:
                            start = time.time()
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"mysql injection in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                if error.code == 504:
                    if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                        hits.append(f"mysql injection in forms: {action} | {field_dict}")

                    else:
                        hits.append(f"mysql injection in forms: {_} | {field_dict}")

            except:
                pass

    return hits, status_hits

 # check for oracle sql injection time based payload
def oracle_sql_time_scanner(_, delay, mal_oracle_sql, forms):
    hits = []
    status_hits = []
    for mal in mal_oracle_sql:
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"oracle sql injection in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"oracle sql injection in url: {_}/{mal}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"oracle sql injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(200)
            if error.code == 504:
                hits.append(f"oracle sql injection in method ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"oracle sql injection in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"oracle sql injection in cookie ({mal}): {_}")

        except:
            pass
                
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"oracle sql injection in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"oracle sql injection in referer ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"oracle sql injection in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"oracle sql injection in x-forwarded-for ({mal}): {_}")

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            start = time.time()
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"oracle sql injection in forms: {action} | {field_dict}")

                        else:
                            start = time.time()
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"oracle sql injection in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                if error.code == 504:
                    if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                        hits.append(f"oracle sql injection in forms: {action} | {field_dict}")

                    else:
                        hits.append(f"oracle sql injection in forms: {_} | {field_dict}")

            except:
                pass

    return hits, status_hits

# check for php injection time based payload
def php_time_scanner(_, delay, mal_php, forms):
    hits = []
    status_hits = []
    for mal in mal_php:
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"php injection in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"php injection in url: {_}/{mal}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"php injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"php injection in method ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"php injection in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"php injection in cookie ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"php injection in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"php injection in referer ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"php injection in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"php injection in x-forwarded-for ({mal}): {_}")

        except:
            pass

        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            start = time.time()
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"php injection in forms: {action} | {field_dict}")

                        else:
                            start = time.time()
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"php injection in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                if error.code == 504:
                    if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                        hits.append(f"php injection in forms: {action} | {field_dict}")

                    else:
                        hits.append(f"php injection in forms: {_} | {field_dict}")

            except:
                pass

    return hits, status_hits

# check for postgresql injection time based payload
def postgresql_time_scanner(_, delay, mal_postgresql, forms):
    hits = []
    status_hits = []
    for mal in mal_postgresql:
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"postgresql injection in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"postgresql injection in url: {_}/{mal}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"posgtresql injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"postgresql injection in method ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"postgresql injection in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"postgresql injection in cookie ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"postgresql injection in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"postgresql injection in referer ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"postgresql injection in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"postgresql injection in x-forwarded-for ({mal}): {_}")

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            start = time.time()
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"postgresql injection in forms: {action} | {field_dict}")

                        else:
                            start = time.time()
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"postgresql injection in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                if error.code == 504:
                    if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                        hits.append(f"postgresql injection in forms: {action} | {field_dict}")

                    else:
                        hits.append(f"postgresql injection in forms: {_} | {field_dict}")

            except:
                pass

    return hits, status_hits

# check for powershell injection time based payload
def powershell_scanner(_, delay, mal_powershell, forms):
    hits = []
    status_hits = []
    for mal in mal_powershell:
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"powershell injection in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"powershell injection in url: {_}/{mal}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"powershell injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"powershell injection in method ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"powershell injection in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"powershell injection in cookie ({mal}): {_}")

        except:
            pass
        
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"powershell injection in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"powershell injection in referer ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"powershell injection in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"powershell injection in x-forwarded-for ({mal}): {_}")

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            start = time.time()
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"powershell injection in forms: {action} | {field_dict}")

                        else:
                            start = time.time()
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"powershell injection in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                if error.code == 504:
                    if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                        hits.append(f"powershell injection in forms: {action} | {field_dict}")

                    else:
                        hits.append(f"powershell injection in forms: {_} | {field_dict}")

            except:
                pass

    return hits, status_hits

 # check for reflective python injection based payload
def python_reflective_scanner(_, delay, mal_python_reflective, forms):
    hits = []
    status_hits = []
    for mal in mal_python_reflective:
        try:
            time.sleep(delay)
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            if "<script>prompt(1)</script>" in data:
                hits.append(f"reflective python in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if "<script>prompt(1)</script>" in data:
                hits.append(f"reflective python in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            if "<script>prompt(1)</script>" in data:
                hits.append(f"reflective python in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            if "<script>prompt(1)</script>" in data:
                hits.append(f"reflective python in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            if "<script>prompt(1)</script>" in data:
                hits.append(f"reflective python in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            if "<script>prompt(1)</script>" in data:
                                hits.append(f"reflective python in forms: {action} | {field_dict}")

                        else:
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            if "<script>prompt(1)</script>" in data:
                                hits.append(f"reflective python in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                
            except:
                pass

    return hits, status_hits

# check for python injection time based payload
def python_time_scanner(_, delay, mal_python_time, forms):
    hits = []
    status_hits = []
    for mal in mal_python_time:
        try:
            time.sleep(delay)
            start = time.time()
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"python injection time based payload in url: {_}/{mal}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"python injection time based payload in url: {_}/{mal}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"python injection in method ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"python injection in method ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"python injection time based payload in method: {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"python injection time based payload in method: {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"python injection time based payload in cookie ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"python injection time based payload in cookie ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"python injection time based payload in referer ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"python injection time based payload in referer ({mal}): {_}")

        except:
            pass

        try:
            time.sleep(delay)
            start = time.time()
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            end = time.time()
            if end - start >= 55:
                hits.append(f"python injection time based payload in x-forwarded-for ({mal}): {_}")

        except HTTPError as error:
            status_hits.append(error.code)
            if error.code == 504:
                hits.append(f"python injection time based payload in x-forwarded-for ({mal}): {_}")

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            start = time.time()
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"python injection time based payload in forms: {action} | {field_dict}")

                        else:
                            start = time.time()
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            end = time.time()
                            if end - start >= 55:
                                hits.append(f"python injection time based payload in forms: {_} | {field_dict}")

            except HTTPError as error:
                status_hits.append(error.code)
                if error.code == 504:
                    if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                        hits.append(f"python injection time based payload in forms: {action} | {field_dict}")

                    else:
                        hits.append(f"python injection time based payload in forms: {_} | {field_dict}")

            except:
                pass

    return hits, status_hits

# check for sql errors (used for fingerprinting and hueristics)
def sql_error_scanner(_, delay, mal_payloads, forms):
    hits = []
    status_hits = []

    mal_errors = {"mssql": r"(?s)Exception.*?\bRoadhouse\.Cms\.|Driver.*? SQL[\-\_\ ]*Server|OLE DB.*? SQL Server|\bSQL Server[^&lt;&quot;]+Driver|Warning.*?\W(mssql|sqlsrv)_|\bSQL Server[^&lt;&quot;]+[0-9a-fA-F]{8}|System\.Data\.SqlClient\.(SqlException|SqlConnection\.OnError)|Microsoft SQL Native Client error '[0-9a-fA-F]{8}|\[SQL Server\]|ODBC SQL Server Driver|ODBC Driver \d+ for SQL Server|SQLServer JDBC Driver|com\.jnetdirect\.jsql|macromedia\.jdbc\.sqlserver|Zend_Db_(Adapter|Statement)_Sqlsrv_Exception|com\.microsoft\.sqlserver\.jdbc|Pdo[./_\\](Mssql|SqlSrv)|SQL(Srv|Server)Exception|Unclosed quotation mark after the character string",
                  "mysql": r"SQL syntax.*?MySQL|Warning.*?\Wmysqli?_|MySQLSyntaxErrorException|valid MySQL result|check the manual that (corresponds to|fits) your MySQL server version|Unknown column '[^ ]+' in 'field list'|MySqlClient\.|com\.mysql\.jdbc|Zend_Db_(Adapter|Statement)_Mysqli_Exception|Pdo[./_\\]Mysql|MySqlException|SQLSTATE\[\d+\]: Syntax error or access violation",
                  "oracle sql": r"\bORA-\d{5}|Oracle error|Oracle.*?Driver|Warning.*?\W(oci|ora)_|quoted string not properly terminated|SQL command not properly ended|macromedia\.jdbc\.oracle|oracle\.jdbc|Zend_Db_(Adapter|Statement)_Oracle_Exception|Pdo[./_\\](Oracle|OCI)|OracleException",
                  "postgresql": r"PostgreSQL.*?ERROR|Warning.*?\Wpg_|valid PostgreSQL result|Npgsql\.|PG::SyntaxError:|org\.postgresql\.util\.PSQLException|ERROR:\s\ssyntax error at or near|ERROR: parser: parse error at or near|PostgreSQL query failed|org\.postgresql\.jdbc|Pdo[./_\\]Pgsql|PSQLException"}

    for mal in mal_payloads:
        try:
            time.sleep(delay)
            data = text(_ + "/" + mal)
            status_hits.append(200)
            for i, j in mal_errors.items():
                if re.search(j, data):
                    hits.append(f"found: {i} in url ({_})")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            for i, j in mal_errors.items():
                if re.search(j, data):
                    hits.append(f"found: {i} in method ({_})")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Cookie": mal})
            status_hits.append(200)
            for i, j in mal_errors.items():
                if re.search(j, data):
                    hits.append(f"found: {i} in cookie ({_})")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Referer": mal})
            status_hits.append(200)
            for i, j in mal_errors.items():
                if re.search(j, data):
                    hits.append(f"found: {i} in referer ({_})")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"X-Forwarded-For": mal})
            status_hits.append(200)
            for i, j in mal_errors.items():
                if re.search(j, data):
                    hits.append(f"found: {i} in x-forwarded-for ({_})")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            data = text(action, method = method_field, data = field_dict)
                            status_hits.append(200)
                            for i, j in mal_errors.items():
                                if re.search(j, data):
                                    hits.append(f"found: {i} in forms ({_})")

                        else:
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            for i, j in mal_errors.items():
                                if re.search(j, data):
                                    hits.append(f"found: {i} in forms ({_})")

            except HTTPError as error:
                status_hits.append(error.code)

            except:
                pass

    if len(hits) > 0:
        hits = list(dict.fromkeys(hits[:]))
        return hits, status_hits

    else:
        return None, status_hits

# check for waf
def waf_scanner(_, delay, mal_waf, forms):
    hits = []
    status_hits = []
    for mal in mal_waf.items():
        try:
            time.sleep(delay)
            data = text(_ + "/" + mal[1])
            status_hits.append(200)
            hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in url")

        except HTTPError as error:
            status_hits.append(error.code)

            if error.code != 403:
                hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in url")
            
        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, method = mal[1], timeout = 120)
            status_hits.append(200)
            hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in method")

        except HTTPError as error:
            status_hits.append(error.code)

            if error.code != 403:
                hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in method")

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Cookie": mal[1]})
            status_hits.append(200)
            hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in cookie")

        except HTTPError as error:
            status_hits.append(error.code)

            if error.code != 403:
                hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in cookie")

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Referer": mal[1]})
            status_hits.append(200)
            hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in referer")

        except HTTPError as error:
            status_hits.append(error.code)

            if error.code != 403:
                hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in referer")

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"X-Forwarded-For": mal[1]})
            status_hits.append(200)
            hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in x-forwarded-for")

        except HTTPError as error:
            status_hits.append(error.code)

            if error.code != 403:
                hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in x-forwarded-for")

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal[1]})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            data = text(action, method = method_field, data = field_dict)
                            status_hits.append(200)
                            hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in forms")

                        else:
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in forms")

            except HTTPError as error:
                status_hits.append(error.code)

                if error.code != 403:
                    hits.append(f"{re.sub(r'\s\d', '', mal[0])} injection possible in forms")

            except:
                pass

    return hits, status_hits

# check for reflective xss
def xss_reflective_scanner(_, delay, mal_xss_reflective, forms):
    hits = []
    status_hits = []
    original_payloads = xss_reflective_payloads()
    for mal in mal_xss_reflective:
        try:
            time.sleep(delay)
            data = text(_ + "/" + mal, timeout = 120)
            status_hits.append(200)
            for og in original_payloads:
                if og in data:
                    hits.append(f"reflective xss in url: {_}/{mal}")
                    break

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, method = mal, timeout = 120)
            status_hits.append(200)
            for og in original_payloads:
                if og in data:
                    hits.append(f"reflective xss in method ({mal}): {_}")
                    break

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Cookie": mal}, timeout = 120)
            status_hits.append(200)
            for og in original_payloads:
                if og in data:
                    hits.append(f"reflective xss in cookie ({mal}): {_}")
                    break

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"Referer": mal}, timeout = 120)
            status_hits.append(200)
            for og in original_payloads:
                if og in data:
                    hits.append(f"reflective xss in referer ({mal}): {_}")
                    break

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

        try:
            time.sleep(delay)
            data = text(_, headers = {"X-Forwarded-For": mal}, timeout = 120)
            status_hits.append(200)
            for og in original_payloads:
                if og in data:
                    hits.append(f"reflective xss in x-forwarded-for ({mal}): {_}")
                    break

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass
        
        for form in forms:
            field_list = []
            input_field = re.findall(r"<input.+?>",form)
            try:
                action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                if action_field.startswith("/"):
                    action = _ + action_field

                elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                    action = _ + "/" + action_field

                else:
                    action = action_field
                    
            except IndexError:
                pass

            try:
                method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']", form)[0].upper()
                for in_field in input_field:
                    if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                        name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        try:
                            value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']", in_field)[0]
                        
                        except IndexError:
                            value_field = ""
                        
                        if type_field == "submit" or type_field == "hidden":
                            field_list.append({name_field: value_field})


                        if type_field != "submit" and type_field != "hidden":
                            field_list.append({name_field: mal})

                        field_dict = field_list[0]
                        for init_field_dict in field_list[1:]:
                            field_dict.update(init_field_dict)

                        time.sleep(delay)

                        if action and urllib.parse.urlparse(_).netloc in urllib.parse.urlparse(action).netloc:
                            data = text(action, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            for og in original_payloads:
                                if og in data:
                                    hits.append(f"reflective xss in forms: {action} | {field_dict}")
                                    break

                        else:
                            data = text(_, method = method_field, data = field_dict, timeout = 120)
                            status_hits.append(200)
                            for og in original_payloads:
                                if og in data:
                                    hits.append(f"reflective xss in forms: {_} | {field_dict}")
                                    break

            except HTTPError as error:
                status_hits.append(error.code)

            except:
                pass

    return hits, status_hits
