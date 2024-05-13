import argparse
import sys
import time
import urllib.parse
from urllib.error import HTTPError
from TheSilent.clear import clear
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.parser import *
from TheSilent.puppy_requests import text, getheaders

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

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
        hosts.append(f"{host}/admin")
        hosts.append(f"{host}/login")
        hosts.append(f"{host}/signin")
        hosts.append(f"{host}/signup")
        hosts.append(f"{host}/search")
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
