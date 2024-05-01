import argparse
import hashlib
import re
import socket
import sys
import time
import urllib.parse
from urllib.error import HTTPError
from TheSilent.clear import clear
from TheSilent.evasion import *
from TheSilent.fingerprint_scanner import *
from TheSilent.http_scanners import *
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.payloads import *
from TheSilent.puppy_requests import text, getheaders

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

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

def cobra():
    clear()
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", required = True)
    parser.add_argument("-scanner", required = True, nargs = "+", type = str, choices = ["all", "banner", "bash", "directory_traversal", "emoji", "fingerprint", "mssql", "mysql", "oracle_sql", "php", "powershell", "python", "sql_error", "waf", "xss"])

    parser.add_argument("-crawl", default = 1, type = int)
    parser.add_argument("-delay", default = 0, type = float)
    parser.add_argument("-evasion", nargs = "+", type = str, choices = ["all", "append_random_string", "directory_self_reference", "percent_encoding", "prepend_random_string", "random_case", "utf8_encoding"])
    parser.add_argument("-log", default = False, type = bool)
    
    args = parser.parse_args()
    
    hits = []
    status_hits = []
    host = args.host.rstrip("/")

    # fingerprint server
    if "fingerprint" in args.scanner or "all" in args.scanner:
        init_hits, init_status_hits = fingerprint_server(host, args.delay)

        for hit in init_hits:
            hits.append(hit)

        for hit in init_status_hits:
            status_hits.append(hit)
            
    # yes crawl
    if args.crawl > 1:
        hosts = kitten_crawler(host, args.delay, args.crawl)
        for _ in hosts:
            print(CYAN + f"checking: {_}")
            if urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(_).netloc:
                results, init_status_hits = hits_parser(_, args.delay, args.scanner, args.evasion)
                for result in results:
                    hits.append(result)

                for i in init_status_hits:
                    status_hits.append(i)
                
    # no crawl
    elif args.crawl == 1:
        print(CYAN + f"checking: {host}")
        results, init_status_hits = hits_parser(host, args.delay, args.scanner, args.evasion)
        for result in results:
            hits.append(result)

        for i in init_status_hits:
            status_hits.append(i)

    elif args.crawl < 1:
        print(RED + "invalid crawl distance")
        sys.exit()

    if args.scanner == "directory_traversal" or args.scanner == "all":
        # check for directory traversal
        time.sleep(delay)
        mal_payloads = directory_traversal_payloads()

        original_payloads = mal_payloads[:]
        if evasion != None:
            for j in original_payloads:
                evade = evasion_parser(j, evasion)
                for k in evade:
                    mal_payloads.append(k)
                
        results, status_x = directory_traversal_scanner(_, delay, mal_payloads)
        for result in results:
            hits.append(result)
            
        for status_y in status_x:
            status_results.append(status_y)

    hits = list(set(hits[:]))
    hits.sort()

    status_results = list(set(status_hits[:]))
    status_results.sort()

    if len(hits) > 0:
        if args.log:
            for hit in hits:
                print(RED + hit)
                with open("simple.log", "a") as file:
                    file.write(hit + "\n")

            for i in status_results:
                print(RED + f"status {i} count: {status_hits.count(i)}")
                with open("simple.log", "a") as file:
                    file.write(f"status {i} count: {status_hits.count(i)}\n")

            print(RED + f"total requests: {len(status_hits)}")
            with open("simple.log", "a") as file:
                    file.write(f"total requests: {len(status_hits)}\n")

        else:
            for hit in hits:
                print(RED + hit)
                
            for i in status_results:
                print(RED + f"status {i} count: {status_hits.count(i)}")
            
            print(RED + f"total requests: {len(status_hits)}")

    else:
        if args.log:
            print(GREEN + f"we didn't find anything interesting on {host}")
            with open("simple.log", "a") as file:
                file.write(f"we didn't find anything interesting on {host}\n")

            for i in status_results:
                print(GREEN + f"status {i} count: {status_hits.count(i)}")
                with open("simple.log", "a") as file:
                    file.write(f"status {i} count: {status_hits.count(i)}\n")

            print(GREEN + f"total requests: {len(status_hits)}")
            with open("simple.log", "a") as file:
                    file.write(f"total requests: {len(status_hits)}\n")
                    
        else:
            print(GREEN + f"we didn't find anything interesting on {host}")

            for i in status_results:
                print(GREEN + f"status {i} count: {status_hits.count(i)}")

            print(GREEN + f"total requests: {len(status_hits)}")
    
        
if __name__ == "__main__":
    cobra()
