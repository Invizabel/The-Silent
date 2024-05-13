from TheSilent.evasion import *
from TheSilent.fingerprint_scanner import *
from TheSilent.http_scanners import *
from TheSilent.payloads import *

def evasion_parser(mal, evasion):
    mal_payloads = []

    for i in evasion:
        if i == "append_random_string" or i == "all":
            mal_evasion = append_random_string(mal)
            for j in mal_evasion:
                mal_payloads.append(j)

        if i == "directory_self_reference" or i == "all":
            mal_evasion = directory_self_reference(mal)
            for j in mal_evasion:
                mal_payloads.append(j)

        if i == "percent_encoding" or i == "all":
            mal_evasion = percent_encoding(mal)
            for j in mal_evasion:
                mal_payloads.append(j)

        if i == "prepend_random_string" or i == "all":
            mal_evasion = prepend_random_string(mal)
            for j in mal_evasion:
                mal_payloads.append(j)

        if i == "random_case" or i == "all":
            mal_evasion = random_case(mal)
            for j in mal_evasion:
                mal_payloads.append(j)

        if i == "utf8_encoding" or i == "all":
            mal_evasion = utf8_encoding(mal)
            for j in mal_evasion:
                mal_payloads.append(j)
        

    return mal_payloads

def hits_parser(_, delay, scanner, evasion):
    hits = []
    finish = []

    try:
        forms = re.findall(r"<form.+form>", text(_).replace("\n",""))

    except:
        forms = []

    for i in scanner:
        if i == "bash" or i == "all":
            # check for time based bash injection
            time.sleep(delay)
            mal_payloads = bash_time_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                    
            results, status_x = bash_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)
                
            for status_y in status_x:
                finish.append(status_y)
                
        if i == "emoji" or i == "all":
            # check for reflective emoji injection
            time.sleep(delay)
            mal_payloads = emoji_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                
            results, status_x = emoji_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
                
        if i == "mssql" or i == "all":
            # check for time based mssql injection
            time.sleep(delay)
            mal_payloads = mssql_time_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                
            results, status_x = mssql_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
            
        if i == "mysql" or i == "all":
            # check for time based mysql injection
            time.sleep(delay)
            mal_payloads = mysql_time_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                
            results, status_x = mysql_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
            
        if i == "oracle_sql" or i == "all":
            # check for time based oracle sql injection
            time.sleep(delay)
            mal_payloads = oracle_sql_time_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                
            results, status_x = oracle_sql_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
            
        if i == "php" or i == "all":
            # check for time based php injection
            time.sleep(delay)
            mal_payloads = php_time_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                
            results, status_x = php_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
        
        if i == "postgresql" or i == "all":
            # check for time based postgresql injection
            time.sleep(delay)
            mal_payloads = postgresql_time_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                
            results, status_x = postgresql_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
        
        if i == "powershell" or i == "all":
            # check for powershell injection
            time.sleep(delay)
            mal_payloads = powershell_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                
            results, status_x = powershell_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
                
        if i == "python" or i == "all":
            # check for reflective python injection
            time.sleep(delay)
            mal_payloads = python_reflective_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                    
            results, status_x = python_reflective_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)

            # check for time based python injection
            time.sleep(delay)
            mal_payloads = python_time_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                
            results, status_x = python_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)

        if i == "sql_error" or i == "all":
            # check for sql injection errors
            time.sleep(delay)
            mal_payloads = ["'", '"', ",", "*", ";"]

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
                    
            results, status_x = sql_error_scanner(_, delay, mal_payloads, forms)
            if results != None:
                for result in results:
                    hits.append(result)

            for status_y in status_x:
                finish.append(status_y)

        # check for waf
        if i == "waf":
            evade_options = ["append_random_string",
                             "directory_self_reference",
                             "percent_encoding",
                             "prepend_random_string",
                             "random_case",
                             "utf8_encoding"]
            
            time.sleep(delay)
            mal_payloads = waf_payloads()

            mal_payloads = waf_payloads()
            original_payloads = mal_payloads.copy()
            for j in original_payloads.items():
                for k in evade_options:
                    evade = evasion_parser(j[1], [k])
                    count = 0
                    for l in evade:
                        count += 1
                        mal_payloads.update({f"{j[0]} {k.replace('_', ' ')} | {count}": l})
            
            results, status_x = waf_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)

        # check for reflective xss
        if i == "xss" or i == "all":
            time.sleep(delay)
            mal_payloads = xss_reflective_payloads()

            original_payloads = mal_payloads[:]
            if evasion != None:
                for j in original_payloads:
                    evade = evasion_parser(j, evasion)
                    for k in evade:
                        mal_payloads.append(k)
            
            results, status_x = xss_reflective_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)

    return hits, finish
