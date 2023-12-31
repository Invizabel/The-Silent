#Documentation:
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
#https://www.w3schools.com/PYTHON/ref_requests_get.asp
#https://www.geeksforgeeks.org/python-check-url-string/
#https://www.w3schools.com/python/gloss_python_check_string.asp
#https://stackoverflow.com/questions/38015537/python-requests-exceptions-sslerror-dh-key-too-small
#https://www.geeksforgeeks.org/create-a-directory-in-python/
#https://stackoverflow.com/quezzstions/7935972/writing-to-a-new-directory-in-python-without-changing-directory
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
#https://www.tutorialspoint.com/python-program-to-check-for-url-in-a-string

#import libraries

#try and except block required for Termux
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import *
    from selenium.webdriver.firefox.service import *
    from webdriver_manager.firefox import *

except:
    pass

from bs4 import BeautifulSoup
from collections import *
from hashlib import *
from itertools import *
from numpy import *
from PIL import Image
from PIL.ExifTags import *
from urllib.parse import urljoin

import codecs
import hashlib
import itertools
import math
import numpy as np
import os
import random
import re
import requests
import shutil
import socket
import socks
import sys
import time
import threading
import twint
import urllib3

#connect to tor
tor_proxy = {"http": "socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

#create html sessions object
web_session = requests.Session()

#fake user agent
user_agent = {"User-Agent" : "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}

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
'''
def find_url(string):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)
	return [x[0] for x in url]
'''

#find url in string
#source code is my own solution https://github.com/Invizabel
'''
def find_url(result):
    web_list = []

    https = "https://"
    end_double = "\""

    if https in result and len(result) <= 1000000:
        for i in range(0, len(result)):
            try:
                index_1 = result.index(https, i, len(result))
                index_2 = result.index(end_double, (index_1 + 9) , len(result))
                
                super_result = result[index_1 + len(https) + 0: index_2]

                x = super_result.split(" ", 1)

                if len(x) > 1:
                    for i in len(1, x):
                        x.pop(i)
                        x[0].replace("'","")
                        x[0].replace("<","")

                web_list.append("https://" + x[0])

            except:
                continue

        web_list = list(dict.fromkeys(web_list))

    if "https://" not in result and len(result) <= 1000000:
        print("ERROR: no url found!")

    return web_list
'''

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
        print("https =", https, "\nvalid certificate =", valid_certificate, "\ntor (linux/macOS (homebrew) users) =", tor_boolean, "\ntor (termux users) =", termux_tor_boolean)
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
        user_tor = input("tor (linux/macOS (homebrew) users)? y/n\n")

        if user_tor == "y":
            tor_boolean = True
            os.system("sudo service tor start")
            os.system("brew services start tor")

        if user_tor == "n":
            tor_boolean = False
            os.system("sudo service tor stop")
            os.system("brew services stop tor")

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
        user_tor = input("1 = debian\n2 = fedora\n3 = termux\n4 = macOS (homebrew)\n")

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

        if user_tor == "4":
            os.system("clear")
            print("installing tor")
            os.system("brew install tor")

    if user_input == "4":
        os.system("clear")
        user_tor = input("1 = debian\n2 = fedora\n3 = termux\n4 = macOS (homebrew)\n")

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

        if user_tor == "4":
            os.system("clear")
            print("installing tor")
            os.system("brew remove tor")

#download all data from a website
def all_data():
    secure = ""
    count = 0
    global website
    os.system("clear")
    website = input("enter website:\n")
    
    start = time.time()

    web_list = link_scanner(website)

    os.system("clear")
    print("Downloading!")

    for i in web_list:
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
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".app"), "wb") as file_writer:
                file_writer.write(data.content)

        if app == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data","file " + str(count)  + ".app"), "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == True:
            count += 1
            file_link = str(i)
            
            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".avi"), "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".avi"), "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".bat"), "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".bat"), "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".cmd"), "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".cmd"), "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".css"), "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".css"), "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".doc"), "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".doc"), "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".docx"), "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".docx"), "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".exe"), "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".exe"), "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".gif"), "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".gif"), "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".html"), "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.get("data/all data", "file " + str(count)  + ".html"), "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jar"), "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jar"), "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".java"), "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".java"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jss"), "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jss"), "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".m4a"), "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".m4a"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp3"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp3"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp4"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp4"), "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".pdf"), "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".pdf"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".py"), "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".py"), "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".sh"), "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".sh"), "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".txt"), "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".txt"), "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == True:
            count += 1
            file_link = str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".xml"), "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == False:
            count += 1
            file_link = secure + str(i)

            if termux_tor_boolean == True or tor_boolean == True:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
                            
            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                data = web_session.get(file_link, verify = valid_certificate, headers = user_agent, timeout = 5)

            with open(os.path.join("data/all data", "file " + str(count)  + ".xml"), "wb") as file_writer:
                file_writer.write(data.content)

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
                    if sources_boolean == True:
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
        
    sources_list = list(dict.fromkeys(sources_list))

    for i in sources_list:
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

def anti_virus(folder):
    os.system("clear")

    file_list = []

    mal_code = ["crypt", "fopen", "open", "read", "write"]
    virus_count = 0
    virus_list = []

    for root, dirs, files in os.walk(folder, topdown = True):
        for name in files:
            file_list.append(os.path.join(root, name))

    file_list.sort()
                
    for file in file_list:
        print("checking: " + file)
        mal_hits = 0
        result = ""

        try:
            if os.path.isfile(file) and file != "anti-virus.py" and os.stat(file).st_size > 0 and os.stat(file).st_size <= 1000000000:
                with open(file, "rb") as f:
                    for chunk in iter(lambda: f.read(32), b""):
                        ascii_convert = codecs.decode(chunk, "ascii")
                        clean = str(ascii_convert).replace("b", "")
                        clean = clean.replace("'", "")
                        clean = clean.replace("\\x", "")
                        clean = clean.replace("00", "")
                        result += clean

        except:
            continue

        for i in mal_code:
            if i in result:
                mal_hits += 1

        chance = mal_hits / len(mal_code) * 100

        if chance == 100:
            print("detected: " + file)
            virus_count += 1
            virus_list.append(file)

    os.system("clear")

    for i in virus_list:
        print(i)

    print("possible viruses detected: " + str(virus_count))

#brute force classic
def brute_force_classic(password):
    dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    maximum = 101

    crack_boolean = False

    for i in range (1, maximum):
        if crack_boolean == True:
            break
        
        print("attempting length: " + str(i))
        
        for ii in itertools.product(dictionary, repeat = i):
            compute_1 = ''.join(ii)
            compute_2 = compute_1[::-1]
            
            if compute_1 == password or compute_2 == password:
                crack_boolean = True
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

#recover deleted data
def data_recovery(image):
    jpg_header = "ffd8ff"
    jpg_footer = "ffd9"
    png_header = "89504e470d0a1a0a"
    png_footer = "49454e44ae426082"

    code = ""
    hex_boolean = False
    png_count = 0
    hex_code_list = []

    #progress_bar
    progress_count = 0
    total_progress = 0
    total, used, free = shutil.disk_usage("/")
    total_storage = int("%d" % (total / (2**30))) * 1000000000
    my_progress = total_storage / 100

    with open(image, "rb") as f:
        for chunk in iter(lambda: f.read(32), b""):
            hex_code = str(codecs.encode(chunk, "hex"))

            progress_count += 32

            if progress_count >= my_progress:
                total_progress += 1
                progress_count = 0
                print(str(total_progress) + "%")

            if hex_boolean == True:
                hex_code_list.append(str(hex_code))

            if hex_boolean == False:
                hex_code_list = []
            
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

def extract_image_metadata(image):
    image = Image.open(image)
    exifdata = image.getexif()

    for tagid in exifdata:
        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        os.system("clear")
        print(f"{tagname:25}: {value}")

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
    total_web_list.sort()

    for i in email_list:
        if i not in super_result:
            super_result.append(i)

    for i in web_result:
        if i not in super_web_result:
            super_web_result.append(i)

    super_result.sort()
    super_web_result.sort()
    
    return str(super_result) + "\n\n" + str(super_web_result)

#simple hex editor
def hex_editor(file, keyword):
    os.system("clear")

    my_boolean = False

    count = 0
    
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(128), b""):
            try:
                ascii_convert = codecs.decode(chunk, "ascii")
            
                clean = str(ascii_convert).replace("b", "")
                clean = clean.replace("'", "")

                my_list = list(clean)
                my_list = list(set(my_list))

                if len(my_list) != 1 and my_list[0] != "\\x00" and keyword in clean:
                    print(clean)

                    count += 1

                    if count == 64:
                        count = 0
                        pause = input()
                    
            except:
                pass

        for chunk in iter(lambda: f.read(2), b""):
            hex_convert = codecs.encode(chunk, "hex")

            clean_hex = str(hex_convert).replace("b", "")
            clean_hex = clean_hex.replace("'", "")

            if clean_hex == "0a":
                print("")

    print("done")

#human detection
def human_detection(input_image, output):
    size = (1920,1080)
    min_range = np.array([100,75,65])
    max_range = np.array([250,240,235])

    final_list = []
    final_image = np.array([])

    image = Image.open(input_image)

    size = image.resize(size)

    result = asarray(size)

    super_result = (result > min_range) & (result < max_range)

    result[np.where((super_result == [True, True, True]).all(axis = 2))] = [255,255,255]
    result[np.where((super_result != [True, True, True]).any(axis = 2))] = [0,0,0]

    data = Image.fromarray(result, "RGB")

    data.save(output)

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
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
        
    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, timeout = 5)

    file = open(os.path.join("data/html", website + ".html"), "w+")
    file.write(final.text)
    final.close()
    file.close()
    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    pause = input()

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

#scans for hyperlinks
def link_scanner(url):
    #variables
    i = -1
    original_url = url
    output = https_string + url
    total_web_list = []
    total_web_list.append(output)
    result_list = []
    web_list = []

    user_input = input("1 = search domain links | 2 = search all links | 3 = search for a specific link | 4 = search domain links using selenium\n")

    if user_input == "3":
        specific_link = input("Enter specific link: ")

    if user_input == "4":
        return link_scanner_selenium(url)

    while True:
        try:
            total_web_list = list(dict.fromkeys(total_web_list))
            
            i += 1

            if termux_tor_boolean == True or tor_boolean == True:
                final = web_session.get(total_web_list[i], verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                final = web_session.get(total_web_list[i], verify = valid_certificate, headers = user_agent, timeout = (5, 30))
                
            found = str(final.status_code)

            if found == "200" and len(final.text) <= 1000000:
                try:
                    print(total_web_list[i])
                    result = str(final.text)

                    soup = BeautifulSoup(result, "html.parser")

                    for my_link in soup.find_all("a", href = True):
                        if "http://" in my_link["href"] or "https://" in my_link["href"]:
                            web_list.append(my_link["href"])

                        if "http://" not in my_link["href"] and "https://" not in my_link["href"]:
                            try:
                                if my_link["href"].index("/") == 0:
                                    web_list.append(str(output + my_link["href"]))

                            except:
                                web_list.append(str(output + "/" + my_link["href"]))
                                
                    web_list = list(dict.fromkeys(web_list))
                    web_list.sort()

                except:
                    print("ERROR!")

                for j in web_list:
                    
                    if user_input == "1":
                        domain_name = str(original_url) in j

                        if domain_name == True:
                            parse = re.findall(r'(?<=<a href="/)[^"]*', result)
                            parse = list(dict.fromkeys(parse))
                            parse.sort()

                            for href in parse:
                                href_result = output + href
                                total_web_list.append(href_result)
                            
                            if "\'" in j:
                                j.split("\'")
                                total_web_list.append(j[0])

                            if "<" in j:
                                j.split("<")
                                total_web_list.append(j[0])

                            if "\\" in j:
                                j.split("\\")
                                total_web_list.append(j[0])

                            if "href" in j:
                                j.split("href")
                                total_web_list.append(j[0])

                            if ")" in j:
                                j.split(")")
                                total_web_list.append(j[0])

                            else:
                                total_web_list.append(j)
                            
                    if user_input == "2":
                        if "\'" in j:
                            j.split("\'")
                            total_web_list.append(j[0])

                        if "<" in j:
                            j.split("<")
                            total_web_list.append(j[0])

                        if "\\" in j:
                            j.split("\\")
                            total_web_list.append(j[0])

                        if "href" in j:
                            j.split("href")
                            total_web_list.append(j[0])

                        if ")" in j:
                                j.split(")")
                                total_web_list.append(j[0])

                        else:
                            total_web_list.append(j)

                    if user_input == "3":
                        domain_name = str(original_url) in j

                        if domain_name == True:
                            if "\'" in j:
                                j.split("\'")
                                total_web_list.append(j[0])

                            if "<" in j:
                                j.split("<")
                                total_web_list.append(j[0])

                            if "\\" in j:
                                j.split("\\")
                                total_web_list.append(j[0])

                            if "href" in j:
                                j.split("href")
                                total_web_list.append(j[0])

                            if ")" in j:
                                j.split(")")
                                total_web_list.append(j[0])

                            else:
                                total_web_list.append(j)

                            for k in web_list:
                                specific = str(specific_link) in k

                                if specific == True:
                                    if "\'" in k:
                                        k.split("\'")
                                        result_list.append(k[0])

                                    if "<" in k:
                                        k.split("<")
                                        result_list.append(k[0])

                                    if "\\" in k:
                                        k.split("\\")
                                        result_list.append(k[0])

                                    if "href" in k:
                                        k.split("href")
                                        total_web_list.append(k[0])

                                    if ")" in k:
                                        k.split(")")
                                        total_web_list.append(k[0])

                                    else:
                                        result_list.append(k)

            else:
                continue
                    
        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            continue

        except requests.exceptions.ChunkedEncodingError:
            print("ERROR: chunked encoding error!")
            continue

        except urllib3.exceptions.LocationParseError:
            print("ERROR: location parse error!")
            continue

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            continue

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
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

        except requests.exceptions.TooManyRedirects:
            print("ERROR: too many redirects!")
            continue

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            continue
            
        except IndexError:
            break

    os.system("clear")
    result_list = list(dict.fromkeys(result_list))
    total_web_list = list(dict.fromkeys(total_web_list))
    
    result_list.sort()

    if user_input == "1" or user_input == "2":
        return total_web_list

    if user_input == "3":
        return result_list

def link_scanner_selenium(url):
    result = https_string + url
    
    driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
    os.system("clear")

    i = -1
    total_web_list = []
    total_web_list.append(result)
    web_list = []

    while True:
        i = i + 1
        
        try:
            print(total_web_list[i])
            driver.get(total_web_list[i])

        except IndexError:
            break

        except:
            continue
        
        try:
            for ii in driver.find_elements(by = By.XPATH, value = ".//a"):
                web_list.append(ii.get_attribute("href"))

        except:
            pass

        web_list = list(dict.fromkeys(web_list))

        for iii in web_list:
            try:
                domain_name = result in iii

                parse = iii.index(result, 0, len(result))
                
                if domain_name == True and parse == 0:
                    total_web_list.append(iii)
                    total_web_list = list(dict.fromkeys(total_web_list))

            except:
                continue

    total_web_list = list(dict.fromkeys(total_web_list))
    total_web_list.sort()

    return total_web_list

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

#get md5 hash
def md5():
    buffer = 1000000
    md5 = hashlib.md5()
    
    os.system("clear")
    file = input("file: ")

    try:
        if os.stat(file).st_size > 0:
            with open(file, "rb") as f:
                while True:
                    data = f.read(buffer)
                    
                    if not data:
                        break

                    md5.update(data)

    except:
        print("ERROR!")

    my_hash = md5.hexdigest()

    print(my_hash)
    pause = input()

#scans the local network for hosts
def network_mapper_1(ip):
    host_list = []

    for i in range(0, 5):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
                
#scans the local network for hosts
def network_mapper_2(ip):
    host_list = []

    for i in range(5, 10):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
                
#scans the local network for hosts
def network_mapper_3(ip):
    host_list = []

    for i in range(10, 15):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
                
#scans the local network for hosts
def network_mapper_4(ip):
    host_list = []

    for i in range(15, 20):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
                
#scans the local network for hosts
def network_mapper_5(ip):
    host_list = []

    for i in range(20, 25):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
                
#scans the local network for hosts
def network_mapper_6(ip):
    host_list = []

    for i in range(25, 30):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
                
#scans the local network for hosts
def network_mapper_7(ip):
    host_list = []

    for i in range(30, 35):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
        
#scans the local network for hosts
def network_mapper_8(ip):
    host_list = []

    for i in range(35, 40):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
                
#scans the local network for hosts
def network_mapper_9(ip):
    host_list = []

    for i in range(40, 45):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue
                
#scans the local network for hosts
def network_mapper_10(ip):
    host_list = []

    for i in range(45, 50):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_11(ip):
    host_list = []

    for i in range(50, 55):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_12(ip):
    host_list = []

    for i in range(55, 60):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_13(ip):
    host_list = []

    for i in range(60, 65):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_14(ip):
    host_list = []

    for i in range(65, 70):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_15(ip):
    host_list = []

    for i in range(70, 75):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_16(ip):
    host_list = []

    for i in range(75, 80):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_17(ip):
    host_list = []

    for i in range(80, 85):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_18(ip):
    host_list = []

    for i in range(85, 90):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_19(ip):
    host_list = []

    for i in range(90, 95):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_20(ip):
    host_list = []

    for i in range(95, 100):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_21(ip):
    host_list = []

    for i in range(100, 105):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_22(ip):
    host_list = []

    for i in range(105, 110):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_23(ip):
    host_list = []

    for i in range(110, 115):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_24(ip):
    host_list = []

    for i in range(115, 120):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_25(ip):
    host_list = []

    for i in range(120, 125):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_26(ip):
    host_list = []

    for i in range(125, 130):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_27(ip):
    host_list = []

    for i in range(130, 135):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_28(ip):
    host_list = []

    for i in range(135, 140):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_29(ip):
    host_list = []

    for i in range(140, 145):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_30(ip):
    host_list = []

    for i in range(145, 150):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_31(ip):
    host_list = []

    for i in range(150, 155):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_32(ip):
    host_list = []

    for i in range(155, 160):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_33(ip):
    host_list = []

    for i in range(160, 165):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_34(ip):
    host_list = []

    for i in range(165, 170):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_35(ip):
    host_list = []

    for i in range(170, 175):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_36(ip):
    host_list = []

    for i in range(175, 180):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_37(ip):
    host_list = []

    for i in range(180, 185):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_38(ip):
    host_list = []

    for i in range(185, 190):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_39(ip):
    host_list = []

    for i in range(190, 195):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_40(ip):
    host_list = []

    for i in range(195, 200):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_41(ip):
    host_list = []

    for i in range(200, 205):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_42(ip):
    host_list = []

    for i in range(205, 210):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_43(ip):
    host_list = []

    for i in range(210, 215):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_44(ip):
    host_list = []

    for i in range(215, 220):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_45(ip):
    host_list = []

    for i in range(220, 225):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_46(ip):
    host_list = []

    for i in range(225, 230):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_47(ip):
    host_list = []

    for i in range(230, 235):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_48(ip):
    host_list = []

    for i in range(235, 240):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_49(ip):
    host_list = []

    for i in range(240, 245):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_50(ip):
    host_list = []

    for i in range(245, 250):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

#scans the local network for hosts
def network_mapper_51(ip):
    host_list = []

    for i in range(250, 256):
        for j in range(0, 256):
            try:
                host = ip + "." + str(i) + "." + str(j)
                sock = socket.socket()
                sock.settimeout(1)
                sock.connect((host, 80))
                sock.close()

                output = "http://" + host

                url = requests.get(output, verify = False)
        
                header = list(url.headers.items())
                header.sort()

                url.close()

                print(host + " === " + str(header) + "\n")

                host_list.append(host + " === " + str(header))

            except ConnectionRefusedError:
                continue

            except OSError:
                continue

            except TimeoutError:
                continue

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

    print("password: " + output)
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
        final = web_session.get(output, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = 5)
        
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

            except ConnectionRefusedError:
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

            except ConnectionRefusedError:
                print(False)
                continue

    os.system("clear")
      
    return socket_list

def sha512():
    buffer = 1000000
    sha512 = hashlib.sha512()
    
    os.system("clear")
    file = input("file: ")

    try:
        if os.stat(file).st_size > 0:
            with open(file, "rb") as f:
                while True:
                    data = f.read(buffer)
                    
                    if not data:
                        break

                    sha512.update(data)

    except:
        print("ERROR!")

    my_hash = sha512.hexdigest()

    print(my_hash)
    pause = input()

def sql_injection_scanner(url):
    os.system("clear")
    my_url = https_string + url

    #sql errors
    error_mesage = {"SQL syntax.*?MySQL", "Warning.*?\Wmysqli?_", "MySQLSyntaxErrorException", "valid MySQL result", "check the manual that (corresponds to|fits) your MySQL server version", "check the manual that (corresponds to|fits) your MariaDB server version", "check the manual that (corresponds to|fits) your Drizzle server version", "Unknown column '[^ ]+' in 'field list'", "MySqlClient\.", "com\.mysql\.jdbc", "Zend_Db_(Adapter|Statement)_Mysqli_Exception", "Pdo\[./_\\]Mysql", "MySqlException", "SQLSTATE\[\d+\]: Syntax error or access violation", "MemSQL does not support this type of query", "is not supported by MemSQL", "unsupported nested scalar subselect", "PostgreSQL.*?ERROR", "Warning.*?\Wpg_", "valid PostgreSQL result", "Npgsql\.", "PG::SyntaxError:", "org\.postgresql\.util\.PSQLException", "ERROR:\s\ssyntax error at or near", "ERROR: parser: parse error at or near", "PostgreSQL query failed", "org\.postgresql\.jdbc", "Pdo\[./_\\]Pgsql", "PSQLException", "OLE DB.*? SQL Server", "\bSQL Server[^&lt;&quot;]+Driver", "Warning.*?\W(mssql|sqlsrv)_", "\bSQL Server[^&lt;&quot;]+[0-9a-fA-F]{8}", "System\.Data\.SqlClient\.(SqlException|SqlConnection\.OnError)", "(?s)Exception.*?\bRoadhouse\.Cms\.", "Microsoft SQL Native Client error '[0-9a-fA-F]{8}", "\[SQL Server\]", "ODBC SQL Server Driver", "ODBC Driver \d+ for SQL Server", "SQLServer JDBC Driver", "com\.jnetdirect\.jsql", "macromedia\.jdbc\.sqlserver", "Zend_Db_(Adapter|Statement)_Sqlsrv_Exception", "com\.microsoft\.sqlserver\.jdbc", "Pdo\[./_\\](Mssql|SqlSrv)", "SQL(Srv|Server)Exception", "Unclosed quotation mark after the character string", "Microsoft Access (\d+ )?Driver", "JET Database Engine", "Access Database Engine", "ODBC Microsoft Access", "Syntax error \(missing operator\) in query expression", "\bORA-\d{5}", "Oracle error", "Oracle.*?Driver", "Warning.*?\W(oci|ora)_", "quoted string not properly terminated", "SQL command not properly ended", "macromedia\.jdbc\.oracle", "oracle\.jdbc", "Zend_Db_(Adapter|Statement)_Oracle_Exception", "Pdo\[./_\\](Oracle|OCI)", "OracleException", "CLI Driver.*?DB2", "DB2 SQL error", "\bdb2_\w+\(", "SQLCODE[=:\d, -]+SQLSTATE", "com\.ibm\.db2\.jcc", "Zend_Db_(Adapter|Statement)_Db2_Exception", "Pdo\[./_\\]Ibm", "DB2Exception", "ibm_db_dbi\.ProgrammingError", "Warning.*?\Wifx_", "Exception.*?Informix", "Informix ODBC Driver", "ODBC Informix driver", "com\.informix\.jdbc", "weblogic\.jdbc\.informix", "Pdo\[./_\\]Informix", "IfxException", "Dynamic SQL Error", "Warning.*?\Wibase_", "org\.firebirdsql\.jdbc", "Pdo\[./_\\]Firebird", "SQLite/JDBCDriver", "SQLite\.Exception", "(Microsoft|System)\.Data\.SQLite\.SQLiteException", "Warning.*?\W(sqlite_|SQLite3::)", "\[SQLITE_ERROR\]", "SQLite error \d+:", "sqlite3.OperationalError:", "SQLite3::SQLException", "org\.sqlite\.JDBC", "Pdo\[./_\\]Sqlite", "SQLiteException", "SQL error.*?POS([0-9]+)", "Warning.*?\Wmaxdb_", "DriverSapDB", "-3014.*?Invalid end of SQL statement", "com\.sap\.dbtech\.jdbc", "\[-3008\].*?: Invalid keyword or missing delimiter", "Warning.*?\Wsybase_", "Sybase message", "Sybase.*?Server message", "SybSQLException", "Sybase\.Data\.AseClient", "com\.sybase\.jdbc", "Warning.*?\Wingres_", "Ingres SQLSTATE", "Ingres\W.*?Driver", "com\.ingres\.gcf\.jdbc", "Exception (condition )?\d+\. Transaction rollback", "com\.frontbase\.jdbc", "Syntax error 1. Missing", "(Semantic|Syntax) error [1-4]\d{2}\.", "Unexpected end of command in statement \[", "Unexpected token.*?in statement \[", "org\.hsqldb\.jdbc", "org\.h2\.jdbc", "\[42000-192\]", "![0-9]{5}![^\n]+(failed|unexpected|error|syntax|expected|violation|exception)", "\[MonetDB\]\[ODBC Driver", "nl\.cwi\.monetdb\.jdbc", "Syntax error: Encountered", "org\.apache\.derby", "ERROR 42X01", ", Sqlstate: (3F|42).{3}, (Routine|Hint|Position):", "/vertica/Parser/scan", "com\.vertica\.jdbc", "org\.jkiss\.dbeaver\.ext\.vertica", "com\.vertica\.dsi\.dataengine", "com\.mckoi\.JDBCDriver", "com\.mckoi\.database\.jdbc", "&lt;REGEX_LITERAL&gt;", "com\.facebook\.presto\.jdbc", "io\.prestosql\.jdbc", "com\.simba\.presto\.jdbc", "UNION query has different number of fields: \d+, \d+", "Altibase\.jdbc\.driver", "com\.mimer\.jdbc", "Syntax error,[^\n]+assumed to mean", "io\.crate\.client\.jdbc", "encountered after end of query", "A comparison operator is required here", "-10048: Syntax error", "rdmStmtPrepare\(.+?\) returned", "SQ074: Line \d+:", "SR185: Undefined procedure", "SQ200: No table ", "Virtuoso S0002 Error", "\[(Virtuoso Driver|Virtuoso iODBC Driver)\]\[Virtuoso Server\]"}
    
    #malicious sql code
    mal_sql = ["\"", "\'", ";"]

    my_list = []

    user_input = input("1 = scan url | 2 = scan url and hyperlinks\n")
    os.system("clear")
    
    if user_input == "1":
        for c in mal_sql:
            new_url = f"{my_url}{c}"
            print("Checking: " + new_url)
            
            try:
                if termux_tor_boolean == True or tor_boolean == True:
                    result = web_session.get(new_url, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    result = web_session.get(new_url, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                for i in error_mesage:
                    my_regex = re.search(i, result.text)
                    my_boolean = False

                    try:
                        if my_regex:
                            my_boolean = True
                            break

                    except UnicodeDecodeError:
                        break

                if my_boolean == True:
                    print("True: " + new_url)
                    my_list.append(new_url)

            except requests.exceptions.SSLError:
                print("ERROR: invalid certificate!")
                continue

            except urllib3.exceptions.LocationParseError:
                print("ERROR: location parse error!")
                continue

            except requests.exceptions.ConnectionError:
                print("ERROR: connection error!")
                continue

            except requests.exceptions.ConnectTimeout:
                print("ERROR: connect timeout!")
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

            except requests.exceptions.TooManyRedirects:
                print("ERROR: too many redirects!")
                continue

            except requests.exceptions.ReadTimeout:
                print("ERROR: read timeout!")
                continue

        try:
            print("Checking for forms on: " + my_url)
            
            if termux_tor_boolean == True or tor_boolean == True:
                result = web_session.get(my_url, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                result = web_session.get(my_url, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

            try:
                soup = BeautifulSoup(result.text, "html.parser")
                get_input = soup.find_all("input")

            except:
                pass

            form_list = []

            for i in get_input:
                if "email" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "hidden" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass
                    
                if "number" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "password" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "query" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "search" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                        
                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "tel" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "text" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "url" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

            form_list = list(dict.fromkeys(form_list))
            form_list.sort()

            for forms in form_list:
                for mal in mal_sql:
                    form_dict = {forms: mal}

                    print("Checking form (" + mal + "): " + forms)

                    if termux_tor_boolean == True or tor_boolean == True:
                        send_data = web_session.post(my_url, data = form_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        send_data = web_session.post(my_url, data = form_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    for i in error_mesage:
                        my_regex = re.search(i, send_data.text)
                        my_boolean = False

                        try:
                            if my_regex:
                                    my_boolean = True
                                    break

                        except UnicodeDecodeError:
                            continue

                    if my_boolean == True:
                        print("True: " + url + " form: " + forms)
                        my_list.append(url + " form: " + forms)

                    if termux_tor_boolean == True or tor_boolean == True:
                        get_data = web_session.get(my_url, params = form_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        get_data = web_session.get(my_url, params = form_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    for i in error_mesage:
                        my_regex = re.search(i, get_data.text)
                        my_boolean = False

                        try:
                            if my_regex:
                                    my_boolean = True
                                    break

                        except UnicodeDecodeError:
                            continue

                    if my_boolean == True:
                        print("True: " + url + " form: " + forms)
                        my_list.append(url + " form: " + forms)

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print("ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print("ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            pass

    if user_input == "2":
        my_result = link_scanner(url)

        for j in my_result:
            for c in mal_sql:
                new_url = f"{j}{c}"

                print("Checking: " + new_url)

                try:
                    if termux_tor_boolean == True or tor_boolean == True:
                        result = web_session.get(new_url, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        result = web_session.get(new_url, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    for i in error_mesage:
                        my_regex = re.search(i, result.text)
                        my_boolean = False

                        try:
                            if my_regex:
                                my_boolean = True
                                break

                        except UnicodeDecodeError:
                            continue

                    if my_boolean == True:
                        print("True: " + new_url)
                        my_list.append(new_url)

                except requests.exceptions.SSLError:
                    print("ERROR: invalid certificate!")
                    pass

                except urllib3.exceptions.LocationParseError:
                    print("ERROR: location parse error!")
                    pass

                except requests.exceptions.ConnectionError:
                    print("ERROR: connection error!")
                    pass

                except requests.exceptions.ConnectTimeout:
                    print("ERROR: connect timeout!")
                    pass

                except requests.exceptions.InvalidSchema:
                    print("ERROR: invalid schema!")
                    pass

                except requests.exceptions.InvalidURL:
                    print("ERROR: invalid url!")
                    pass

                except requests.exceptions.MissingSchema:
                    print("ERROR: missing schema!")
                    pass

                except requests.exceptions.TooManyRedirects:
                    print("ERROR: too many redirects!")
                    pass

                except requests.exceptions.ReadTimeout:
                    print("ERROR: read timeout!")
                    pass
                
            try:
                print("Checking for forms on: " + j)

                if termux_tor_boolean == True or tor_boolean == True:
                    result = web_session.get(j, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    result = web_session.get(j, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                try:
                    soup = BeautifulSoup(result.text, "html.parser")
                    get_input = soup.find_all("input")

                except:
                    pass

                form_list = []

                for i in get_input:
                    if "email" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "hidden" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass
                        
                    if "number" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "password" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "query" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "search" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "tel" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "text" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "url" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                form_list = list(dict.fromkeys(form_list))
                form_list.sort()

                for forms in form_list:
                    for mal in mal_sql:
                        form_dict = {forms: mal}

                        print("Checking form (" + mal + "): " + forms)

                        if termux_tor_boolean == True or tor_boolean == True:
                            send_data = web_session.post(j, data = form_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                            send_data = web_session.post(j, data = form_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                        for i in error_mesage:
                            my_regex = re.search(i, send_data.text)
                            my_boolean = False

                            try:
                                if my_regex:
                                        my_boolean = True
                                        break

                            except UnicodeDecodeError:
                                continue

                        if my_boolean == True:
                            print("True: " + url + " form: " + forms)
                            my_list.append(url + " form: " + forms)

                        if termux_tor_boolean == True or tor_boolean == True:
                            get_data = web_session.get(j, params = form_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                        if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                            get_data = web_session.get(j, params = form_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                        for i in error_mesage:
                            my_regex = re.search(i, get_data.text)
                            my_boolean = False

                            try:
                                if my_regex:
                                        my_boolean = True
                                        break

                            except UnicodeDecodeError:
                                continue

                        if my_boolean == True:
                            print("True: " + url + " form: " + forms)
                            my_list.append(url + " form: " + forms)

            except requests.exceptions.SSLError:
                print("ERROR: invalid certificate!")
                continue

            except urllib3.exceptions.LocationParseError:
                print("ERROR: location parse error!")
                continue

            except requests.exceptions.ConnectionError:
                print("ERROR: connection error!")
                continue

            except requests.exceptions.ConnectTimeout:
                print("ERROR: connect timeout!")
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

            except requests.exceptions.TooManyRedirects:
                print("ERROR: too many redirects!")
                continue

            except requests.exceptions.ReadTimeout:
                print("ERROR: read timeout!")
                continue

    os.system("clear")
    
    return my_list

def xss_scanner(url):
    os.system("clear")
    my_list = []
    my_url = https_string + url
    
    #malicious script
    mal_script = "<script>alert('The Silent')</script>"

    user_input = input("1 = scan url | 2 = scan url and hyperlinks\n")
    os.system("clear")

    if user_input == "1":
        try:
            super_result = my_url.split("=")
            print("Checking: " + super_result[0] + "=" + mal_script)
            
            if termux_tor_boolean == True or tor_boolean == True:
                result = web_session.get(super_result[0] + "=" + mal_script, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                result = web_session.get(super_result[0] + "=" + mal_script, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

            if mal_script in result.text:
                    print("True: " + super_result[0] + "=" + mal_script + " (script in url)")
                    my_list.append(super_result[0] + "=" + mal_script + " (script in url)")

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print("ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print("ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            pass

        except UnicodeError:
            pass
        
        try:
            print("Checking: " + my_url + mal_script)
            
            if termux_tor_boolean == True or tor_boolean == True:
                result = web_session.get(my_url + mal_script, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                result = web_session.get(my_url + mal_script, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

            if mal_script in result.text:
                    print("True: " + my_url + mal_script + " (script in url)")
                    my_list.append(my_url + mal_script + " (script in url)")

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print("ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print("ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            pass

        except UnicodeError:
            pass

        try:
            print("Checking for forms on: " + my_url)
        
            if termux_tor_boolean == True or tor_boolean == True:
                result = web_session.get(my_url, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

            if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                result = web_session.get(my_url, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

            try:
                soup = BeautifulSoup(result.text, "html.parser")
                get_input = soup.find_all("input")

            except:
                pass

            form_list = []

            for i in get_input:
                if "email" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                        
                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "hidden" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass
                    
                if "number" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "password" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "query" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                        
                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "search" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "tel" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                        
                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "text" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                        
                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                if "url" in str(i):
                    form_name = ""

                    try:
                        parse_name_start = str(i).index("name=\"")
                        parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                        
                        for ii in range(parse_name_start + 6, parse_name_end):
                            form_name = form_name + str(i)[ii]

                        form_list.append(form_name)

                    except:
                        pass

                form_list = list(dict.fromkeys(form_list))
                form_list.sort()

                for forms in form_list:
                    print("Checking form: " + forms)
                    mal_dict = {forms: mal_script}

                    if termux_tor_boolean == True or tor_boolean == True:
                        get_data = web_session.get(my_url, params = mal_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        get_data = web_session.get(my_url, params = mal_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    if termux_tor_boolean == True or tor_boolean == True:
                        send_data = web_session.post(my_url, data = mal_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        send_data = web_session.post(my_url, data = mal_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    if mal_script in send_data.text or mal_script in get_data.text:
                        print("True: " + url + " form: " + forms)
                        my_list.append(url + " form: " + forms)

        except requests.exceptions.SSLError:
            print("ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print("ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print("ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print("ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print("ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print("ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print("ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print("ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print("ERROR: read timeout!")
            pass

        except UnicodeError:
            pass

    if user_input == "2":
        my_result = link_scanner(url) 

        for links in my_result:
            try:
                super_result = links.split("=")
                print("Checking: " + super_result[0] + "=" + mal_script)
                
                if termux_tor_boolean == True or tor_boolean == True:
                    result = web_session.get(super_result[0] + "=" + mal_script, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    result = web_session.get(super_result[0] + "=" + mal_script, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                if mal_script in result.text:
                        print("True: " + super_result[0] + "=" + mal_script + " (script in url)")
                        my_list.append(super_result[0] + "=" + mal_script + " (script in url)")

            except requests.exceptions.SSLError:
                print("ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print("ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print("ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print("ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print("ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print("ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print("ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print("ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print("ERROR: read timeout!")
                pass

            except UnicodeError:
                pass
                
            try:
                print("Checking: " + links + mal_script)
                
                if termux_tor_boolean == True or tor_boolean == True:
                    result = web_session.get(links + mal_script, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    result = web_session.get(links + mal_script, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                if mal_script in result.text:
                        print("True: " + links  + mal_script + " (script in url)")
                        my_list.append(links  + mal_script + " (script in url)")

            except requests.exceptions.SSLError:
                print("ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print("ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print("ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print("ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print("ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print("ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print("ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print("ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print("ERROR: read timeout!")
                pass

            except UnicodeError:
                pass

            try:
                print("Checking for forms on: " + links)
                
                if termux_tor_boolean == True or tor_boolean == True:
                    result = web_session.get(links, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                    result = web_session.get(links, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                try:
                    soup = BeautifulSoup(result.text, "html.parser")
                    get_input = soup.find_all("input")

                except:
                    pass

                form_list = []

                for i in get_input:
                    if "email" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "hidden" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass
                        
                    if "number" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "password" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "query" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "search" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))

                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "search" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "tel" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "text" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                    if "url" in str(i):
                        form_name = ""

                        try:
                            parse_name_start = str(i).index("name=\"")
                            parse_name_end = str(i).index("\"", parse_name_start + 6, len(str(i)))
                            
                            for ii in range(parse_name_start + 6, parse_name_end):
                                form_name = form_name + str(i)[ii]

                            form_list.append(form_name)

                        except:
                            pass

                form_list = list(dict.fromkeys(form_list))
                form_list.sort()

                for forms in form_list:
                    print("Checking form: " + forms)
                    mal_dict = {forms: mal_script}

                    if termux_tor_boolean == True or tor_boolean == True:
                        get_data = web_session.get(links, params = mal_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        get_data = web_session.get(links, params = mal_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    if termux_tor_boolean == True or tor_boolean == True:
                        send_data = web_session.post(links, data = mal_dict, verify = valid_certificate, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor_boolean == False and termux_tor_boolean == False and tor_boolean == False:
                        send_data = web_session.post(links, data = mal_dict, verify = valid_certificate, headers = user_agent, timeout = (5, 30))

                    if mal_script in send_data.text or mal_script in get_data.text:
                        print("True: " + links + " form: " + forms)
                        my_list.append(links + " form: " + forms)

            except requests.exceptions.SSLError:
                print("ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print("ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print("ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print("ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print("ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print("ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print("ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print("ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print("ERROR: read timeout!")
                pass

            except UnicodeError:
                pass

    my_list = list(dict.fromkeys(my_list))
    my_list.sort()

    os.system("clear")

    return my_list
          
#mainloop
while True:
    os.system("clear")
    user_input = input("0 = security\n1 = digital forensics\n2 = osint\n3 = penetration testing\n4 = other\ne = exit\n")

    #security
    if user_input == "0":
        security()

    #digital forensics
    if user_input == "1":
        os.system("clear")
        print("digital forensics tools")
        my_input = input("1 = compare perceptual hash\n2 = data recovery\n3 = device storage\n4 = extract image metadata\n5 = file finder\n6 = hex editor\n7 = md5 hash\n8 = sha512\ne = exit\n")

        #compare perceptual hash
        if my_input == "1":
            os.system("clear")
            file_1 = input("name of file 1: ")
            file_2 = input("name of file 2: ")
            print(compare_perceptual_hash(file_1, file_2))
            pause = input()

        #data recovery
        if my_input == "2":
            os.system("clear")
            image = input("device name: ")
            data_recovery(image)

        #device storage
        if my_input == "3":
            os.system("clear")
            directory = input("directory: ")
            print(device_storage(directory))
            pause = input()

        #extract image metadata
        if my_input == "4":
            os.system("clear")
            image = input("Enter image: ")
            extract_image_metadata(image)
            pause = input()

        #file finder
        if my_input == "5":
            os.system("clear")
            file = input("file to find: ")
            directory = input("directory to search: ")
            print(file_finder(file, directory))
            pause = input()

        #hex editor
        if my_input == "6":
            os.system("clear")
            file = input("file name: ")
            keyword = input("keyword: ")
            hex_editor(file, keyword)
            pause = input()

        #md5 hash
        if my_input == "7":
            md5()

        #sha512 hash
        if my_input == "8":
            sha512()

        #exit
        if my_input == "e":
            exit()

    #osint
    if user_input == "2":
        os.system("clear")
        print("osint tools")
        my_input = input("1 = email scanner\n2 = get request file\n3 = get request (log)\n4 = get request (no log)\n5 = get security questions (twitter)\n6 = link scanner\n7 = link scanner (selenium)\n8 = network mapper\n9 = scan twitter\ne = exit\n")

        #email scanner
        if my_input == "1":
            os.system("clear")
            url = input("url: ")
            print(email_scanner(url))
            pause = input()

        #get request file
        if my_input == "2":
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

        #get request (log)
        if my_input == "3":
            log()

        #get request (no log)
        if my_input == "4":
            no_log()

        #get security questions (twitter)
        if my_input == "5":
            os.system("clear")
            user_name = input("Enter twitter username: ")
            print("")

            keywords = ["anniversary", "bff", "birthday", "born", "boyfriend", "brother", "cat", "child", "children", "college", "color", "dad", "daughter", "dog", "elementary", "father", "favorite", "friend", "girlfriend", "husband", "kid", "kitten", "mom", "mother", "pet", "primary", "puppy", "school", "sister", "son", "wife"]

            result = twint.Config()
            result.Username = user_name

            for i in keywords:
                print("keyword === " + i)
                result.Search = i
                twint.run.Search(result)
                print("")

            print("Done!")

            pause = input()

        #link scanner
        if my_input == "6":
            os.system("clear")
            url = input("url: ")
            print(link_scanner(url))
            pause = input()

        #link scanner (selenium)
        if my_input == "7":
            os.system("clear")
            url = input("Enter url: ")
            print(link_scanner_selenium(url))
            pause = input()

        #network mapper
        if my_input == "8":
            os.system("clear")

            ip = input("Enter first two numbers of ip address (default = 192.168): ")

            if ip == "":
                ip = ("192.168",)

            else:
                ip = (ip,)

            print("Scanning...\n")

            thread_1 = threading.Thread(name = "network_mapper_1", target = network_mapper_1, args = ip)
            thread_1.start()

            thread_2 = threading.Thread(name = "network_mapper_2", target = network_mapper_2, args = ip)
            thread_2.start()

            thread_3 = threading.Thread(name = "network_mapper_3", target = network_mapper_3, args = ip)
            thread_3.start()

            thread_4 = threading.Thread(name = "network_mapper_4", target = network_mapper_4, args = ip)
            thread_4.start()

            thread_5 = threading.Thread(name = "network_mapper_5", target = network_mapper_5, args = ip)
            thread_5.start()

            thread_6 = threading.Thread(name = "network_mapper_6", target = network_mapper_6, args = ip)
            thread_6.start()

            thread_7 = threading.Thread(name = "network_mapper_7", target = network_mapper_7, args = ip)
            thread_7.start()

            thread_8 = threading.Thread(name = "network_mapper_8", target = network_mapper_8, args = ip)
            thread_8.start()

            thread_9 = threading.Thread(name = "network_mapper_9", target = network_mapper_9, args = ip)
            thread_9.start()

            thread_10 = threading.Thread(name = "network_mapper_10", target = network_mapper_10, args = ip)
            thread_10.start()

            thread_11 = threading.Thread(name = "network_mapper_11", target = network_mapper_11, args = ip)
            thread_11.start()

            thread_12 = threading.Thread(name = "network_mapper_12", target = network_mapper_12, args = ip)
            thread_12.start()

            thread_13 = threading.Thread(name = "network_mapper_13", target = network_mapper_13, args = ip)
            thread_13.start()

            thread_14 = threading.Thread(name = "network_mapper_14", target = network_mapper_14, args = ip)
            thread_14.start()

            thread_15 = threading.Thread(name = "network_mapper_15", target = network_mapper_15, args = ip)
            thread_15.start()

            thread_16 = threading.Thread(name = "network_mapper_16", target = network_mapper_16, args = ip)
            thread_16.start()

            thread_17 = threading.Thread(name = "network_mapper_17", target = network_mapper_17, args = ip)
            thread_17.start()

            thread_18 = threading.Thread(name = "network_mapper_18", target = network_mapper_18, args = ip)
            thread_18.start()

            thread_19 = threading.Thread(name = "network_mapper_19", target = network_mapper_19, args = ip)
            thread_19.start()

            thread_20 = threading.Thread(name = "network_mapper_20", target = network_mapper_20, args = ip)
            thread_20.start()

            thread_21 = threading.Thread(name = "network_mapper_21", target = network_mapper_21, args = ip)
            thread_21.start()

            thread_22 = threading.Thread(name = "network_mapper_22", target = network_mapper_22, args = ip)
            thread_22.start()

            thread_23 = threading.Thread(name = "network_mapper_23", target = network_mapper_23, args = ip)
            thread_23.start()

            thread_24 = threading.Thread(name = "network_mapper_24", target = network_mapper_24, args = ip)
            thread_24.start()

            thread_25 = threading.Thread(name = "network_mapper_25", target = network_mapper_25, args = ip)
            thread_25.start()

            thread_26 = threading.Thread(name = "network_mapper_26", target = network_mapper_26, args = ip)
            thread_26.start()

            thread_27 = threading.Thread(name = "network_mapper_27", target = network_mapper_27, args = ip)
            thread_27.start()

            thread_28 = threading.Thread(name = "network_mapper_28", target = network_mapper_28, args = ip)
            thread_28.start()

            thread_29 = threading.Thread(name = "network_mapper_29", target = network_mapper_29, args = ip)
            thread_29.start()

            thread_30 = threading.Thread(name = "network_mapper_30", target = network_mapper_30, args = ip)
            thread_30.start()

            thread_31 = threading.Thread(name = "network_mapper_31", target = network_mapper_31, args = ip)
            thread_31.start()

            thread_32 = threading.Thread(name = "network_mapper_32", target = network_mapper_32, args = ip)
            thread_32.start()

            thread_33 = threading.Thread(name = "network_mapper_33", target = network_mapper_33, args = ip)
            thread_33.start()

            thread_34 = threading.Thread(name = "network_mapper_34", target = network_mapper_34, args = ip)
            thread_34.start()

            thread_35 = threading.Thread(name = "network_mapper_35", target = network_mapper_35, args = ip)
            thread_35.start()

            thread_36 = threading.Thread(name = "network_mapper_36", target = network_mapper_36, args = ip)
            thread_36.start()

            thread_37 = threading.Thread(name = "network_mapper_37", target = network_mapper_37, args = ip)
            thread_37.start()

            thread_38 = threading.Thread(name = "network_mapper_38", target = network_mapper_38, args = ip)
            thread_38.start()

            thread_39 = threading.Thread(name = "network_mapper_39", target = network_mapper_39, args = ip)
            thread_39.start()

            thread_40 = threading.Thread(name = "network_mapper_40", target = network_mapper_40, args = ip)
            thread_40.start()

            thread_41 = threading.Thread(name = "network_mapper_41", target = network_mapper_41, args = ip)
            thread_41.start()

            thread_42 = threading.Thread(name = "network_mapper_42", target = network_mapper_42, args = ip)
            thread_42.start()

            thread_43 = threading.Thread(name = "network_mapper_43", target = network_mapper_43, args = ip)
            thread_43.start()

            thread_44 = threading.Thread(name = "network_mapper_44", target = network_mapper_44, args = ip)
            thread_44.start()

            thread_45 = threading.Thread(name = "network_mapper_45", target = network_mapper_45, args = ip)
            thread_45.start()

            thread_46 = threading.Thread(name = "network_mapper_46", target = network_mapper_46, args = ip)
            thread_46.start()

            thread_47 = threading.Thread(name = "network_mapper_47", target = network_mapper_47, args = ip)
            thread_47.start()

            thread_48 = threading.Thread(name = "network_mapper_48", target = network_mapper_48, args = ip)
            thread_48.start()

            thread_49 = threading.Thread(name = "network_mapper_49", target = network_mapper_49, args = ip)
            thread_49.start()

            thread_50 = threading.Thread(name = "network_mapper_50", target = network_mapper_50, args = ip)
            thread_50.start()

            thread_51 = threading.Thread(name = "network_mapper_51", target = network_mapper_51, args = ip)
            thread_51.start()
            
            thread_1.join()
            thread_2.join()
            thread_3.join()
            thread_4.join()
            thread_5.join()
            thread_6.join()
            thread_7.join()
            thread_8.join()
            thread_9.join()
            thread_10.join()
            thread_11.join()
            thread_12.join()
            thread_13.join()
            thread_14.join()
            thread_15.join()
            thread_16.join()
            thread_17.join()
            thread_18.join()
            thread_19.join()
            thread_20.join()
            thread_21.join()
            thread_22.join()
            thread_23.join()
            thread_24.join()
            thread_25.join()
            thread_26.join()
            thread_27.join()
            thread_28.join()
            thread_29.join()
            thread_30.join()
            thread_31.join()
            thread_32.join()
            thread_33.join()
            thread_34.join()
            thread_35.join()
            thread_36.join()
            thread_37.join()
            thread_38.join()
            thread_39.join()
            thread_40.join()
            thread_41.join()
            thread_42.join()
            thread_43.join()
            thread_44.join()
            thread_45.join()
            thread_46.join()
            thread_47.join()
            thread_48.join()
            thread_49.join()
            thread_50.join()
            thread_51.join()

            print("Done!")

            pause = input()

        #scan twitter (twint)
        if my_input == "9":
            os.system("clear")
            
            user_name = input("Enter username: ")
            keyword = input("Enter keyword: ")
            print()

            #configure
            result = twint.Config()
            result.Username = user_name
            result.Search = keyword

            #run
            twint.run.Search(result)

            pause = input()

        #exit
        if my_input == "e":
            exit()
        
    #penetration testing
    if user_input == "3":
        os.system("clear")
        print("penetration testing tools")
        my_input = input("1 = brute force (classic)\n2 = brute force (dictionary)\n3 = port scanner\n4 = sql injection scanner\n5 = xss scanner\ne = exit\n")

        #brute force (classic)
        if my_input == "1":
            os.system("clear")
            password = input("enter password: ")
            print(brute_force_classic(password))
            pause = input()

        #brute force (dictionary)
        if my_input == "2":
            brute_force_dictionary()

        #port scanner
        if my_input == "3":
            os.system("clear")
            website = input("website: ")
            print(port_scanner(website))
            pause = input()

        #sql injection scanner
        if my_input == "4":
            os.system("clear")
            url = input("Enter url: ")
            print(sql_injection_scanner(url))
            print("Done!")
            pause = input()
            

        #xss scanner
        if my_input == "5":
            os.system("clear")
            url = input("Enter url: ")
            print(xss_scanner(url))
            print("Done!")
            pause = input()

        #exit
        if my_input == "e":
            exit()
        
    #other
    if user_input == "4":
        os.system("clear")
        print("other tools")
        my_input = input("1 = anti-virus\n2 = generate password hash\n3 = human detection\n4 = password generator\ne = exit\n")

        #anti-virus
        if my_input == "1":
            os.system("clear")
            folder = input("Enter directory or folder: ")
            anti_virus(folder)
            pause = input()

        #generate password hash
        if my_input == "2":
            os.system("clear")
            password = input("password: ")
            result = sha256(password.encode("utf-8")).hexdigest()
            print(result)
            pause = input()

        #human detection
        if my_input == "3":
            os.system("clear")
            input_image = input("enter name of image (input): ")
            output = input("enter name of image (output): ")
            human_detection(input_image, output)

        #password generator
        if my_input == "4":
            password_generator()

        #exit
        if my_input == "e":
            exit()
    
    if user_input == "e":
        exit()
