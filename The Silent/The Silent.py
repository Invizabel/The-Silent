#Documentation:
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
#https://www.w3schools.com/PYTHON/ref_requests_get.asp
#https://www.geeksforgeeks.org/python-check-url-string/
#https://www.w3schools.com/python/gloss_python_check_string.asp
#https://stackoverflow.com/questions/38015537/python-requests-exceptions-sslerror-dh-key-too-small
#https://www.geeksforgeeks.org/create-a-directory-in-python/
#https://stackoverflow.com/questions/7935972/writing-to-a-new-directory-in-python-without-changing-directory
#https://medium.com/@jasonrigden/using-tor-with-the-python-request-library-79015b2606cb
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
#https://content-blockchain.org/research/testing-different-image-hash-functions/
#https://pypi.org/project/ImageHash/
#https://www.geeksforgeeks.org/python-os-statvfs-method/
#https://www.geeksforgeeks.org/shutil-module-in-python/
#https://www.quora.com/How-to-recover-deleted-files-using-a-C++-or-Python-Program?share=1
#https://www.reddit.com/r/Python/comments/qe1ovu/recover_deleted_and_overwritten_files_with/
#https://stackoverflow.com/questions/443967/how-to-create-python-bytes-object-from-long-hex-string
#https://stackoverflow.com/questions/15374969/determining-if-a-string-contains-a-word
#https://www.geeksforgeeks.org/python-itertools-combinations_with_replacement/
#https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
#https://stackoverflow.com/questions/67423037/python-extract-email-address-from-a-huge-string
#https://www.geeksforgeeks.org/python-remove-after-substring-in-string/

#import libraries
from collections import *
from hashlib import *
from itertools import *

import codecs
import hashlib
import math
import os
import random
import re
import requests
import shutil
import socket
import socks
import time
import urllib3

#connect to tor
tor_proxy = {"http": "socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

#create sessions object
web_session = requests.Session()

#fake user agent
user_agent = {"User-Agent" : "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

#create data folder variables
main_folder = "data"
all_data_folder = "all data"
html_folder = "html"
images_folder = "images"
log_folder = "log"
pdf_folder = "pdf"

#create data folders
files = os.path.join(main_folder, all_data_folder)
os.makedirs(files, exist_ok = True)
files = os.path.join(main_folder, html_folder)
os.makedirs(files, exist_ok = True)
files = os.path.join(main_folder, images_folder)
os.makedirs(files, exist_ok = True)
files = os.path.join(main_folder, log_folder)
os.makedirs(files, exist_ok = True)
files = os.path.join(main_folder, pdf_folder)
os.makedirs(files, exist_ok = True)

#security variables
https = True
https_string = "https://"
tor_boolean = False
termux_tor_boolean = False
valid_certificate = True

#increased security
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

#increased security
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

except AttributeError:
    pass

#find url in a string
#source code taken from geeksforgeeks.org
def find_url(string):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)
	return [x[0] for x in url]

#source code taken from geeksforgeeks.org
def find_email(email):
    result = False
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    if(re.fullmatch(regex, email)):
        result = True
 
    else:
        result = False

    return result

#security settings
def security():
    global change_tor_boolean
    global https
    global https_string
    global tor_boolean
    global termux_tor_boolean
    global valid_certificate
    os.system("clear")
    user_input = input("1 = security status\n2 = edit security\n3 = install tor\n4 = remove tor\n")

    if user_input == "1":
        os.system("clear")
        print("https =", https, "\nvalid certificate =", valid_certificate, "\ntor (non termux users) =", tor_boolean, "\ntor (termux users) =", termux_tor_boolean)
        pause = input()

    if user_input == "2":
        os.system("clear")
        user_https = input("https? y/n\n")

        if user_https == "y":
            https = True
            https_string = "https://"

        if user_https == "n":
            https = False
            https_string = "http://"

        os.system("clear")
        user_valid_certificate = input("valid certificate? y/n\n")

        if user_valid_certificate == "y":
            valid_certificate = True

        if user_valid_certificate == "n":
            valid_certificate = False

        os.system("clear")
        user_tor = input("tor (non termux users)? y/n\n")

        if user_tor == "y":
            tor_boolean = True
            os.system("sudo service tor start")

        if user_tor == "n":
            tor_boolean = False
            os.system("sudo service tor stop")

        os.system("clear")
        user_tor = input("tor (termux users)? y/n\n")

        if user_tor == "y":
            termux_tor_boolean = True
            os.system("sv-enable tor")

        if user_tor == "n":
            termux_tor_boolean = False
            os.system("sv-disable tor")

    if user_input == "3":
        os.system("clear")
        user_tor = input("1 = debian\n2 = fedora\n3 = termux\n")

        if user_tor == "1":
            os.system("clear")
            print("installing tor")
            os.system("sudo apt update")
            os.system("sudo apt install tor")

        if user_tor == "2":
            os.system("clear")
            print("installing tor")
            os.system("sudo dnf install tor")

        if user_tor == "3":
            os.system("clear")
            print("installing tor")
            os.system("apt update")
            os.system("apt install tor")

    if user_input == "4":
        os.system("clear")
        user_tor = input("1 = debian\n2 = fedora\n3 = termux\n")

        if user_tor == "1":
            os.system("clear")
            print("removing tor")
            os.system("sudo apt purge tor")

        if user_tor == "2":
            os.system("clear")
            print("removing tor")
            os.system("sudo dnf remove tor")

        if user_tor == "3":
            os.system("clear")
            print("removing tor")
            os.system("apt remove tor")

#make a request not using a log
def no_log():
    global website
    os.system("clear")
    website = input("enter website:\n")
    os.system("clear")
    user_input = input("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url\n11 = server stats\n")
    
    if user_input == "1":
        print(no_log_cookies(website))
        pause = input()

    if user_input == "2":
        print(no_log_encoding(website))
        pause = input()

    if user_input == "3":
        no_log_headers(website)
        pause = input()

    if user_input == "4":
        print(no_log_html_code(website))
        pause = input()

    if user_input == "5":
        print(no_log_ok(website))
        pause = input()

    if user_input == "6":
        print(no_log_permanent_redirect(website))
        pause = input()

    if user_input == "7":
        print(no_log_reason(website))
        pause = input()

    if user_input == "8":
        print(no_log_redirect(website))
        pause = input()

    if user_input == "9":
        print(no_log_status_code(website))
        pause = input()

    if user_input == "10":
        print(no_log_url(website))
        pause = input()

    if user_input == "11":
        no_log_server_stats(website)
        pause = input()

def no_log_cookies(website):
    os.system("clear")
    output = https_string + website
    result = ""
    
    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)
            
        result = final.cookies

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result

def no_log_encoding(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = final.encoding

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result

def no_log_headers(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = list(final.headers.items())
        result.sort()

        for i in result:
            print(i)

    except requests.exceptions.SSLError:
      result = str("invalid certificate")
      print(result)
    
def no_log_html_code(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = final.text

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result
    
def no_log_ok(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = final.ok

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result
    
def no_log_permanent_redirect(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = final.is_permanent_redirect

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result

def no_log_reason(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = final.reason

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result

def no_log_redirect(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = final.is_redirect

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result
    
def no_log_status_code(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = final.status_code

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result
    
def no_log_url(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            final = web_session.get(output, verify = valid_certificate, headers = user_agent)

        result = final.url

    except requests.exceptions.SSLError:
      result = str("invalid certificate")

    return result

def no_log_server_stats(website):
    os.system("clear")
    output = https_string + website
    result = ""

    try:
        if termux_tor_boolean == True or tor_boolean == True:
            url = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
            
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            url = web_session.get(output, verify = valid_certificate, headers = user_agent)
            
        web = list(url.headers.items())
        web.sort()

        for i in web:
            request_string = str(i)
            clean_1 = request_string.replace("(", "")
            clean_2 = clean_1.replace(")", "")
            clean_3 = clean_2.replace(",", ":")
            result = clean_3.replace("'", "")
            result = result.lower()

            if "server:" in result:
                print(result)

        url.close()

    except requests.exceptions.SSLError:
      result = str("invalid certificate")
      print(result)
      
#make a request using a log
def log():
    global file
    global website
    file = open(os.path.join("data/log", "log.txt"), "a")
    os.system("clear")
    website = input("enter website:\n")
    os.system("clear")
    user_input = input("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url\n11 = server stats\n")

    if user_input == "1":
        print(log_cookies(website))
        pause = input()
        
    if user_input == "2":
        print(log_encoding(website))
        pause = input()
        
    if user_input == "3":
        log_headers(website)
        pause = input()

    if user_input == "4":
        print(log_html_code(website))
        pause = input()

    if user_input == "5":
        print(log_ok(website))
        pause = input()

    if user_input == "6":
        print(log_permanent_redirect(website))
        pause = input()
            
    if user_input == "7":
        print(log_reason(website))
        pause = input()
            
    if user_input == "8":
        print(log_redirect(website))
        pause = input()
            
    if user_input == "9":
        print(log_status_code(website))
        pause = input()
            
    if user_input == "10":
        print(log_url(website))
        pause = input()

    if user_input == "11":
        log_server_stats(website)
        pause = input()

def log_cookies(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.cookies)
    file.write("\n\ncookies: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_encoding(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.encoding)
    file.write("\n\nencoding: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_headers(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = list(final.headers.items())
    result.sort()

    for i in result:
        print(i)
        file.write("\n\nheaders: " + str(i) + "\n\n")

    final.close()
    file.close()
    
def log_html_code(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.text)
    file.write("\n\nhtml code: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_ok(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.ok) 
    file.write("\n\nok: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_permanent_redirect(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.is_permanent_redirect)
    file.write("\n\npermanent redirect: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_reason(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.reason)
    file.write("\n\nreason: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_redirect(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.is_redirect)
    file.write("\n\nredirect: " + result + "\n\n")
    final.close()
    file.close()
    return result

def log_status_code(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.status_code)
    file.write("\n\nstatus code: " + result + "\n\n")
    final.close()
    file.close
    return result
    
def log_url(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.url)
    file.write("\n\nurl: " + result + "\n\n")
    final.close()
    file.close()
    return result

def log_server_stats(website):
    os.system("clear")
    output = https_string + website

    if termux_tor_boolean == True or tor_boolean == True:
        url = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        url = web_session.get(output, verify = valid_certificate, headers = user_agent)
        
    web = list(url.headers.items())
    web.sort()

    for i in web:
        request_string = str(i)
        clean_1 = request_string.replace("(", "")
        clean_2 = clean_1.replace(")", "")
        clean_3 = clean_2.replace(",", ":")
        result = clean_3.replace("'", "")
        result = result.lower()

        if "server:" in result:
            print(result)
            file.write("\n\n" + result + "\n\n")

    url.close()
    file.close

#port scanner
def port_scanner(host):
    if termux_tor_boolean == True or tor_boolean == True:
        socket_list = []
       
        for i in range(1, 1024):
            port = i
            print(port)

            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "localhost", 9050, True)
                sock = socks.socksocket()
                sock.settimeout(1)
                sock.connect((host, port))
                sock.close()

                socket_list.append(port)
                print(True)

            except TimeoutError:
                print(False)
                continue

            except socks.GeneralProxyError:
                print(False)
                continue
        
    
    if termux_tor_boolean == False and tor_boolean == False:
        socket_list = []
       
        for i in range(1, 1024):
            port = i
            print(port)

            try:
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, port))
                sock.close()

                socket_list.append(port)
                print(True)

            except TimeoutError:
                print(False)
                continue

    os.system("clear")
      
    return socket_list

#scans the local network for web servers
def network_mapper():
    host_list = []

    for i in range(0, 100):
        for j in range(0, 100):
            try:
                host = "192.168." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header))

                host_list.append(host + " === " + str(header))

            except TimeoutError:
                print(host + ": " + str(False))

            except ConnectionRefusedError:
                print(host + ": " + str(False))

    os.system("clear")

    return host_list

#scans for hyperlinks
def link_scanner(url):
    #variables
    i = -1
    original_url = url
    output = https_string + url
    total_web_list = []

    user_input = input("1 = domain links | 2 = all links\n")

    while True:
        try:
            i = i + 1

            if termux_tor_boolean == True or tor_boolean == True:
                final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
        
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                final = web_session.get(output, verify = valid_certificate, headers = user_agent, timeout = 5)

            try:
                result = str(final.text)
                web_list = find_url(result)
                web_list = set(web_list)

            except:
                print("ERROR!")

            for j in web_list:
                if user_input == "1":
                    domain_name = str(original_url) in j

                    if domain_name == True:
                        total_web_list = list(dict.fromkeys(total_web_list))
                        total_web_list.append(j)

                if user_input == "2":
                    total_web_list = list(dict.fromkeys(total_web_list))
                    total_web_list.append(j)
                    
            url = total_web_list[i]
            print(url)

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            break

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            continue

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            continue
            
        except IndexError:
            break

    os.system("clear")
    total_web_list = list(dict.fromkeys(total_web_list))

    total_web_list.append("https://" + url)
    total_web_list.sort
    
    return total_web_list

#scans for emails on website
def email_scanner(url):
    #variables
    email_list = []
    i = -1
    original_url = url
    output = https_string + url
    super_result = []
    super_web_result = []
    total_web_list = []
    web_result = []

    while True:
        try:
            i = i + 1

            if termux_tor_boolean == True or tor_boolean == True:
                final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
        
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                final = web_session.get(output, verify = valid_certificate, headers = user_agent, timeout = 5)

            try:
                result = str(final.text)
                web_list = find_url(result)
                web_list = set(web_list)
                
            except:
                print("ERROR!")

            for j in web_list:
                domain_name = str(original_url) in j

                if domain_name == True:
                    total_web_list = list(dict.fromkeys(total_web_list))
                    total_web_list.append(j)

            #checks wether there are emails in html code or not
            email_result = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", result)
            #print(str(email_result))

            if len(email_result) != 0:
                email_list.append(email_result)
                final_result = str(email_result) + " === " + str(url)
                web_result.append(final_result)

                print(final_result)
                    
            url = total_web_list[i]

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            break

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            continue

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            continue
            
        except IndexError:
            break

    os.system("clear")
    total_web_list = list(dict.fromkeys(total_web_list))
    total_web_list.sort

    for i in email_list:
        if i not in super_result:
            super_result.append(i)

    for i in web_result:
        if i not in super_web_result:
            super_web_result.append(i)

    super_result.sort
    super_web_result.sort
    
    return str(super_result) + "\n\n" + str(super_web_result)

#download specific image from a website
def image():
    secure = ""
    global website
    os.system("clear")
    website = input("enter website:\n")
    os.system("clear")
    name = input("enter desired name:\n")
    os.system("clear")
    print("Downloading!")
    start = time.time()

    if https == True:
        secure = "https://"

    if https == False:
        secure = "http://"
    
    output = secure + website

    picture = str(output)

    if termux_tor_boolean == True or tor_boolean == True:
        data = web_session.get(picture, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        data = web_session.get(picture, verify = valid_certificate, headers = user_agent, timeout = 5)
        
    with open(os.path.join("data/images", name), "wb") as file_writer:
        file_writer.write(data.content)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    data.close()
    pause = input()

#download pdf from a website
def pdf():
    secure = ""
    global website
    os.system("clear")
    website = input("enter website:\n")
    os.system("clear")
    name = input("enter desired name:\n")
    os.system("clear")
    print("Downloading!")
    start = time.time()

    if https == True:
        secure = "https://"

    if https == False:
        secure = "http://"
    
    output = secure + website
    pdf = output

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        data = web_session.get(pdf, stream = True, verify = valid_certificate, headers = user_agent, timeout = 5)

    data = requests.post(pdf, stream = True, verify = valid_certificate, headers = user_agent, timeout = 5)

    with open(os.path.join("data/pdf", name), "wb") as pdf:
        for chunk in data.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    data.close()
    pause = input()

#download source from a website
def html():
    secure = ""
    global website
    os.system("clear")
    website = input("enter website:\n")
    os.system("clear")
    print("Downloading!")
    start = time.time()

    if https == True:
        secure = "https://"

    if https == False:
        secure = "http://"
    
    output = secure + website

    if termux_tor_boolean == True or tor_boolean == True:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, timeout = 5)

    file = open(os.path.join("data/html", website + ".html"), "w+")
    file.write(final.text)
    final.close()
    file.close()
    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    pause = input()

#download all images from a website
def all_images():
    secure = ""
    count = 0
    global website
    os.system("clear")
    url = input("enter website:\n")
    os.system("clear")
    print("Scanning links!")
    start = time.time()

    if https == True:
        secure = "https://"

    if https == False:
        secure = "http://"

    website = link_scanner(url)

    os.system("clear")
    print("Downloading!")

    for i in website:
        if "im.vsco.co" in i:
            removal = ".jpg"
            extract_special = i.split("im.vsco.co")
            result = secure + "im.vsco.co" + extract_special[1]
            result = result[:result.index(removal) + len(removal)]
            print(result)

        else:
            result = i
            print(result)
            
        try:
            jpeg = ".jpeg" in result
            jpg = ".jpg" in result
            png = ".png" in result
            y = "http" in result

            if jpeg == True and y == True:
                count += 1
                picture = str(result)

                if termux_tor_boolean == True or tor_boolean == True:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                    
                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, timeout = 5)

                with open(os.path.join("data/images","image " + str(count)  + ".jpeg"), "wb") as file_writer:
                    file_writer.write(data.content)

            if jpeg == True and y == False:
                count += 1
                picture = secure + str(result)

                if termux_tor_boolean == True or tor_boolean == True:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                    
                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, timeout = 5)

                with open(os.path.join("data/images","image " + str(count)  + ".jpeg"), "wb") as file_writer:
                    file_writer.write(data.content)

            if jpg == True and y == True:
                count += 1
                picture = str(result)

                if termux_tor_boolean == True or tor_boolean == True:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                    
                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, timeout = 5)

                with open(os.path.join("data/images","image " + str(count)  + ".jpg"), "wb") as file_writer:
                    file_writer.write(data.content)
                    
            if jpg == True and y == False:
                count += 1
                picture = secure + str(result)

                if termux_tor_boolean == True or tor_boolean == True:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                    
                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, timeout = 5)

                with open(os.path.join("data/images","image " + str(count)  + ".jpg"), "wb") as file_writer:
                    file_writer.write(data.content)

            if png == True and y == True:
                count += 1
                picture = str(result)

                if termux_tor_boolean == True or tor_boolean == True:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                    
                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, timeout = 5)

                with open(os.path.join("data/images","image " + str(count)  + ".png"), "wb") as file_writer:
                    file_writer.write(data.content)

            if png == True and y == False:
                count += 1
                picture = secure + str(result)

                if termux_tor_boolean == True or tor_boolean == True:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                    
                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    data = web_session.get(picture, verify = valid_certificate, headers = user_agent, timeout = 5)

                with open(os.path.join("data/images","image " + str(count)  + ".png"), "wb") as file_writer:
                    file_writer.write(data.content)

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            break

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            continue

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            continue
        
        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            continue

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            continue

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            continue

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            continue

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            continue

    
    sources_boolean = False
    sources_list = []
    sources_string = ""

    super_sources_list = []

    for j in website:
        try:
            print(j)

            if termux_tor_boolean == True or tor_boolean == True:
                final = web_session.get(j, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                    
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                final = web_session.get(j, verify = valid_certificate, headers = user_agent, timeout = 5)
                
            html = final.text
            words = re.findall(r"\w+", html)

            for i in words:
                if i == "jpg" or i == "jpeg" or i == "png":
                    sources_boolean = False
                    sources_string += "." + i
                    result = url + sources_string
                    sources_list.append("https://" + result)
                    sources_string = ""

                if sources_boolean == True:
                    sources_string = sources_string + "/" + i
                
                if i == "src":
                    sources_boolean = True
                    sources_string = ""
                
        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            break

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            continue

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            continue
        
        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            continue

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            continue

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            continue

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            continue

    for i in sources_list:
        try:
            if termux_tor_boolean == True or tor_boolean == True:
                final = web_session.get(i, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                        
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                final = web_session.get(i, verify = valid_certificate, headers = user_agent, timeout = 5)
                
            file_found = final.status_code

            if file_found == 200:
                super_sources_list.append(i)

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            break

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            continue

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            continue
        
        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            continue

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            continue

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            continue

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            continue

    super_sources_list = list(dict.fromkeys(super_sources_list))

    for i in super_sources_list:
        jpeg = ".jpeg" in i
        jpg = ".jpg" in i
        png = ".png" in i

        print(i)

        if termux_tor_boolean == True or tor_boolean == True:
            data = web_session.get(i, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                    
        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
            data = web_session.get(i, verify = valid_certificate, headers = user_agent, timeout = 5)

        if jpeg == True:
            count += 1
            with open(os.path.join("data/images","image " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True:
            count += 1
            with open(os.path.join("data/images","image " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True:
            count += 1
            with open(os.path.join("data/images","image " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)
                
    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    pause = input()

#download all data from a website
def all_data():
    secure = ""
    count = 0
    global website
    os.system("clear")
    website = input("enter website:\n")
    os.system("clear")
    print("Downloading!")
    start = time.time()

    if https == True:
        secure = "https://"

    if https == False:
        secure = "http://"
    
    output = secure + website

    if tor_boolean == True:
        url = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        url = web_session.get(output, verify = valid_certificate, headers = user_agent)

    if change_tor_boolean == True:
        os.system("sudo service tor stop")
        os.system("sudo service tor start")
    
    out = str(url.text)
    web_list = find_url(out)
    file = open(os.path.join("data/all data", website + ".html"), "w+")
    file.write(url.text)
    url.close()
    file.close()

    for i in web_list:
        if change_tor_boolean == True:
            os.system("sudo service tor stop")
            os.system("sudo service tor start")
        
        app = ".app" in i
        avi = ".avi" in i
        bat = ".bat" in i
        cmd = ".cmd" in i
        css = ".css" in i
        doc = ".doc" in i
        docx = ".docx" in i
        exe = ".exe" in i
        gif = ".gif" in i
        html = ".html" in i
        jar = ".jar" in i
        java = ".java" in i
        jpeg = ".jpeg" in i
        jpg = ".jpg" in i
        jss = ".jss" in i
        m4a = ".m4a" in i
        mp3 = ".mp3" in i
        mp4 = ".mp4" in i
        pdf = ".pdf" in i
        png = ".png" in i
        py = ".py" in i
        sh = ".sh" in i
        txt = ".txt" in i
        xml = ".xml" in i
        y = "http" in i

        if app == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".app"), "wb") as file_writer:
                file_writer.write(data.content)

        if app == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data","file " + str(count)  + ".app"), "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".avi"), "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".avi"), "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".bat"), "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".bat"), "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".cmd"), "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".cmd"), "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".css"), "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".css"), "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".doc"), "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".doc"), "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".docx"), "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".docx"), "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".exe"), "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".exe"), "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".gif"), "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".gif"), "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".html"), "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.get("data/all data", "file " + str(count)  + ".html"), "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jar"), "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jar"), "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".java"), "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".java"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jss"), "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jss"), "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".m4a"), "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".m4a"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp3"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp3"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp4"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp4"), "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".pdf"), "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".pdf"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".py"), "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".py"), "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".sh"), "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".sh"), "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".txt"), "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".txt"), "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == True:
            count += 1
            data_file = str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".xml"), "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = web_session.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".xml"), "wb") as file_writer:
                file_writer.write(data.content)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    url.close()
    pause = input()

#password generator
def password_generator():
    os.system("clear")
    output = ""
    password_storage = [""]
    password_storage.clear()
    password_characters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    password_length = int(input("What is the password length?\n"))

    for i in range (0,password_length):
        rand = random.randint(0,len(password_characters) - 1)

        password_storage.append(password_characters[rand])

    for i in password_storage:
        output += i

    print("Password:", output)
    result = sha256(output.encode("utf-8")).hexdigest()
    print("hashed password: " + result)
    pause = input()

#brute force classic
def brute_force_classic(password, length):
    dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    maximum = int(length) + 1

    for i in range (1, maximum):
        for ii in combinations_with_replacement(dictionary, i):
            compute_1 = ''.join(ii)
            compute_2 = compute_1[::-1]

            if compute_1 == password or compute_2 == password:
                break

    return "password: " + password

#brute force password using dictionary method
def brute_force_dictionary():
    count = 0

    os.system("clear")
    
    user_input = input("Enter name of list: ")

    text_file = open(user_input, "r")
    tracker = text_file.readlines()

    os.system("clear")

    print("Enter password: ")
    key = input()

    check = str(key) + "\n"

    while True:
        if count == len(tracker):
            print("No more guesses!")
            text_file.close()
            exit()

        if str(tracker[count]) == check:
            print("The password is:", check, "!")
            text_file.close()
            exit()

        if str(tracker[count]) != check and count != len(tracker):
            count += 1

    pause = input()

#compare perceptual hashes
def compare_perceptual_hash(file_1, file_2):
    try:
        from PIL import Image
        import imagehash
        first_hash = Image.open(file_1).convert("L")
        first_hash.thumbnail((256, 256))
        first_hash = imagehash.phash(first_hash)
        second_hash = Image.open(file_2).convert("L")
        second_hash.thumbnail((256, 256))
        second_hash = imagehash.phash(second_hash)
        equal = str(first_hash == second_hash)
        hamming_distance = str(first_hash - second_hash)
        result = "equal: " + equal + "\nhamming distance: " + hamming_distance + "\nfile 1 hash: " + str(first_hash) + "\nfile 2 hash: " + str(second_hash)

    except:
        result = "image hash library not found"
        
    return result

#display stats about device storage
def device_storage(directory):
    stats = os.statvfs(directory)
    block_size = stats.f_bsize
    free_blocks = stats.f_bfree
    free_space = math.floor(free_blocks * block_size / 1000000000)

    file_count = 0
    directory_count = 0
    os.chdir(directory)

    for root, dirs, files in os.walk(".", topdown = True):
       for name in files:
          file_count += 1

       for name in dirs:
          directory_count += 1

    return "block size: " + str(block_size) + "\nfree blocks: " + str(free_blocks) + "\nfree space: " + str(free_space) + " GB" + "\nFiles: " + str(file_count) + "\nDirectories: " + str(directory_count)

#recover deleted data
def data_recovery(image):
    png_header = "89504e470d0a1a0a"
    png_footer = "49454e44ae426082"

    code = ""
    hex_boolean = False
    png_count = 0
    hex_code_list = []

    #progress bar
    stat = str(shutil.disk_usage(image))
    stat = stat.split("usage(total=")
    result = stat[1]
    result = int(result[:result.index(",") + len("")])
    progress = math.floor(result / 100)
    progress_count = 0
    total_progress = 0

    with open(image, "rb") as f:
        for chunk in iter(lambda: f.read(32), b""):
            hex_code = str(codecs.encode(chunk, "hex"))

            progress_count = progress_count + 32

            if progress_count >= progress:
                progress_count = 0
                total_progress = total_progress + 1
                print(str(total_progress) + "%")

            if hex_boolean == True:
                hex_code_list.append(str(hex_code))

            if hex_boolean == False:
                hex_code_list.clear()
            
            if png_header in hex_code:
                hex_boolean = True
                hex_code_list.clear()
                hex_code_list.append(str(hex_code))

            if png_footer in hex_code:
                hex_code_list.append(str(hex_code))
                hex_boolean = False
                png_count += 1

                for i in hex_code_list:
                    code = str(code + i)
                    clean_1 = code.replace("'b'", "")
                    clean_2 = clean_1.replace("b'", "")
                    clean_3 = clean_2.replace("'", "")
                    result = clean_3.replace("\n", "")

                try:
                    png_extract = bytes.fromhex(result)

                except:
                    print("ERROR!")
                    continue

                with open(os.path.join("data/images", "image " + str(png_count) + ".png"), "wb") as file:
                    file.write(png_extract)

def hex_editor(file):
    os.system("clear")
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(32), b""):
            print(codecs.encode(chunk, "hex"))

#file finder finds files based on hash signatures
def file_finder(file, directory):
    os.system("clear")

    size = 1000000
    hash_file = hashlib.sha512()

    with open(file, 'rb') as f:
        data = f.read(size)

        while len(data) > 0:
            hash_file.update(data)
            data = f.read(size)

    display_progress = 0
    errors = 0
    file_count = 0
    file_list = []
    progress = 0

    stats = os.statvfs(directory)
    os.chdir(directory)

    for root, dirs, files in os.walk(".", topdown = True):
       for name in files:
          file_count += 1

    total_progress = math.ceil(file_count / 100 )

    for (root, dirs, files) in os.walk(".", topdown = True):
       for name in files:
          progress = progress + 1
          size = 1000000
          file_hash = hashlib.sha512()
          clean = root.replace("./", "")
          result = os.path.join(directory, clean, name)
          file_exists = os.path.isfile(result)

          if progress == total_progress:
             display_progress = display_progress + 1
             progress = 0
             print(str(display_progress) + "%")

          try:
             file_has_data = os.stat(result).st_size == 0

          except:
             continue

          if file_exists == True and file_has_data == False:
             try:
                with open(result, 'rb') as f:
                   data = f.read(size)

                   while len(data) > 0:
                      file_hash.update(data)
                      data = f.read(size)

                if file_hash.hexdigest() == "":
                   continue

             except:
                continue

          else:
             errors = errors + 1
             continue

          if file_hash.hexdigest() == hash_file.hexdigest():
            file_list.append(result)

    os.system("clear")
    return str("errors = " + str(errors) + "\n" + "\n" + "files found: " + str(file_list))
          
#mainloop
while True:
    os.system("clear")
    user_input = input("0 = security\n1 = request (no log)\n2 = request (log)\n3 = request file\n4 = password generator\n5 = brute force (dictionary)\n6 = compare perceptual hash\n7 = generate password hash\n8 = device storage\n9 = data recovery\n10 = hex editor\n11 = brute force (classic)\n12 = port scanner\n13 = file finder\n14 = link scanner\n15 = email scanner\n16 = network mapper\ne = exit\n")

    if user_input == "0":
        security()

    if user_input == "1":
        no_log()

    if user_input == "2":
        log()

    if user_input == "3":
        os.system("clear")
        user_file = input("1 = image | 2 = pdf | 3 = html | 4 = all images | 5 = all data\n")

        if user_file == "1":
            image()

        if user_file == "2":
            pdf()

        if user_file == "3":
            html()

        if user_file == "4":
            all_images()

        if user_file == "5":
            all_data()

    if user_input == "4":
        password_generator()

    if user_input == "5":
        brute_force_dictionary()

    if user_input == "6":
        os.system("clear")
        file_1 = input("name of file 1: ")
        file_2 = input("name of file 2: ")
        print(compare_perceptual_hash(file_1, file_2))
        pause = input()

    if user_input == "7":
        os.system("clear")
        password = input("password: ")
        result = sha256(password.encode("utf-8")).hexdigest()
        print(result)
        pause = input()

    if user_input == "8":
        os.system("clear")
        directory = input("directory: ")
        print(device_storage(directory))
        pause = input()

    if user_input == "9":
        os.system("clear")
        image = input("device name: ")
        data_recovery(image)

    if user_input == "10":
        os.system("clear")
        file = input("file name: ")
        hex_editor(file)
        pause = input()

    if user_input == "11":
        os.system("clear")
        password = input("enter password: ")
        password_length = input("enter length of password: ")
        print(brute_force_classic(password, password_length))
        pause = input()

    if user_input == "12":
        os.system("clear")
        website = input("website: ")
        print(port_scanner(website))
        pause = input()

    if user_input == "13":
        os.system("clear")
        file = input("file to find: ")
        directory = input("directory to search: ")
        print(file_finder(file, directory))
        pause = input()

    if user_input == "14":
        os.system("clear")
        url = input("url: ")
        print(link_scanner(url))
        pause = input()

    if user_input == "15":
        os.system("clear")
        url = input("url: ")
        print(email_scanner(url))
        pause = input()

    if user_input == "16":
        os.system("clear")
        print(network_mapper())
        pause = input()
    
    if user_input == "e":
        exit()
