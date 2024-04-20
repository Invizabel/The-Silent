import argparse
import hashlib
import re
import socket
import sys
import time
import urllib.parse
from TheSilent.banner_scanner import *
from TheSilent.clear import clear
from TheSilent.evasion import *
from TheSilent.http_scanners import *
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.payloads import *
from TheSilent.puppy_requests import text, getheaders

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

def evasion_parser(mal, evasion):
    mal_payloads = []

    if "all" not in evasion:
        for j in evasion:
            if j == "append_random_string":
                for mal in mal_evasion:
                    mal_payloads.append_random_string(mal)

            if j == "directory_self_reference":
                for mal in mal_evasion:
                    mal_payloads.directory_self_reference(mal)

            if j == "percent_encoding":
                for mal in mal_evasion:
                    mal_payloads.percent_encoding(mal)

            if j == "prepend_random_string":
                for mal in mal_evasion:
                    mal_payloads.prepend_random_string(mal)

            if j == "random_case":
                for mal in mal_evasion:
                    mal_payloads.random_case(mal)

            if j == "utf8_encoding":
                for mal in mal_evasion:
                    mal_payloads.utf8_encoding(mal)

    else:
        for mal in mal_evasion:
            mal_payloads.append_random_string(mal)

        for mal in mal_evasion:
            mal_payloads.directory_self_reference(mal)

        for mal in mal_evasion:
            mal_payloads.percent_encoding(mal)
            
        for mal in mal_evasion:
            mal_payloads.prepend_random_string(mal)
            
        for mal in mal_evasion:
            mal_payloads.random_case(mal)
            
        for mal in mal_evasion:
            mal_payloads.utf8_encoding(mal)
        

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

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = bash_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
                
        if i == "emoji" or i == "all":
            # check for reflective emoji injection
            time.sleep(delay)
            mal_payloads = emoji_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = emoji_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
                
        if i == "mssql" or i == "all":
            # check for time based mssql injection
            time.sleep(delay)
            mal_payloads = mssql_time_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = mssql_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
            
        if i == "mysql" or i == "all":
            # check for time based mysql injection
            time.sleep(delay)
            mal_payloads = mysql_time_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = mysql_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
            
        if i == "oracle_sql" or i == "all":
            # check for time based oracle sql injection
            time.sleep(delay)
            mal_payloads = oracle_sql_time_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = oracle_sql_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
            
        if i == "php" or i == "all":
            # check for time based php injection
            time.sleep(delay)
            mal_payloads = php_time_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = php_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
        
        if i == "postgresql" or i == "all":
            # check for time based postgresql injection
            time.sleep(delay)
            mal_payloads = postgresql_time_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = postgresql_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
        
        if i == "powershell" or i == "all":
            # check for powershell injection
            time.sleep(delay)
            mal_payloads = powershell_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = powershell_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)
                
        if i == "python" or i == "all":
            time.sleep(delay)
            mal_payloads = python_reflective_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                    
            results, status_x = python_reflective_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)

            # check for time based python injection
            time.sleep(delay)
            mal_payloads = python_time_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
                
            results, status_x = python_time_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)

        # check for reflective xss
        if i == "xss" or i == "all":
            time.sleep(delay)
            mal_payloads = xss_reflective_payloads()

            if evasion != None:
                original_payloads = mal_payloads[:]
                for i in original_payloads:
                    mal_payloads.append(i)
            
            results, status_x = xss_reflective_scanner(_, delay, mal_payloads, forms)
            for result in results:
                hits.append(result)

            for status_y in status_x:
                finish.append(status_y)

    return hits, finish

def simple():
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", required = True)
    parser.add_argument("-scanner", required = True, nargs = "+", type = str, choices = ["all", "banner", "bash", "emoji", "fingerprint", "info", "mssql", "mysql", "oracle_sql", "php", "powershell", "python", "xss"])
    

    parser.add_argument("-crawl", default = 1, type = int)
    parser.add_argument("-delay", default = 0, type = float)
    parser.add_argument("-evasion", nargs = "+", type = str, choices = ["all", "append_random_string", "directory_self_reference", "percent_encoding", "prepend_random_string", "random_case", "utf8_encoding"])
    parser.add_argument("-log", default = False, type = bool)
    
    args = parser.parse_args()
    
    hits = []
    status_hits = []
    host = args.host.rstrip("/")

    if "banner" in args.scanner  or "all" in args.scanner:
        clear()
        print(CYAN + f"grabbing banners from: {urllib.parse.urlparse(host).netloc}")
        results = banner_grabber(urllib.parse.urlparse(host).netloc)
        for result in results:
            hits.append(result)

        try:
            http_banner = re.findall(r"server:\s*(.+)", str(getheaders(host)).lower())[0]
            hits.append(f"http banner: {http_banner}")

        except:
            pass

    if "fingerprint" in args.scanner or "all" in args.scanner:
        paths = ["favicon.ico"]
        fingerprint_dict = {"content-keeper": "06c673c63c930a65265e75e32ea49c6095c3628c5f82c8c06181a93a84e7948f",
                            "proxmox": "f171ad34a7b8fd7ccc8da32e5afdaecf11f7ab1cfbd57adef22620b242c2a6eb"}
        
        clear()
        print(CYAN + f"fingerprinting: {host}")

        try:
            http_banner = re.findall(r"server:\s*(.+)", str(getheaders(host)).lower())[0]
            hits.append(f"http banner: {http_banner}")

        except:
            pass

        path_bool = True
        for path in paths:
            try:
                if not path_bool:
                    break
                
                data = text(host + "/" + path, raw = True)
                status_hits.append(200)
                for i, j in fingerprint_dict.items():
                    if j == hashlib.sha256(data).hexdigest():
                        hits.append(f"found: {i}")
                        path_bool = False
                        break

            except HTTPError as error:
                status_hits.append(error.code)

            except:
                pass

    if "info" in args.scanner or "all" in args.scanner:
        clear()
        print(CYAN + f"grabbing log info from: {urllib.parse.urlparse(host).netloc}")

        try:
            hits.append(f"reverse dns: {socket.gethostbyname_ex(urllib.parse.urlparse(host).netloc)}")
            http_headers = getheaders(host)
            status_hits.append(200)
            for i in http_headers.items():
                hits.append(f"{i[0]}: {i[1]}")

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass
            
    # yes crawl
    if args.crawl > 1:
        hosts = kitten_crawler(args.host, args.delay, args.crawl)
        clear()
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
        clear()
        print(CYAN + f"checking: {host}")
        results, init_status_hits = hits_parser(host, args.delay, args.scanner, args.evasion)
        for result in results:
            hits.append(result)

        for i in init_status_hits:
            status_hits.append(i)

    else:
        print(RED + f"ERROR! Can't crawl with depth of {args.crawl}")
        sys.exit()
        
    clear()
    hits = list(set(hits[:]))
    hits.sort()

    status_results = list(set(status_hits[:]))
    status_results.sort()

    for i in status_results:
        print(CYAN + f"status {i} count: {status_hits.count(i)}")

    print(CYAN + f"total requests: {len(status_hits)}")

    if len(hits) > 0:
        if args.log:
            for hit in hits:
                print(RED + hit)
                with open("simple.log", "a") as file:
                    file.write(hit + "\n")

        else:
            for hit in hits:
                print(RED + hit)

    else:
        if args.log:
            print(GREEN + f"we didn't find anything interesting on {host}")
            with open("simple.log", "a") as file:
                file.write(f"we didn't find anything interesting on {host}\n")

        else:
            print(GREEN + f"we didn't find anything interesting on {host}")
    
        
if __name__ == "__main__":
    simple()
