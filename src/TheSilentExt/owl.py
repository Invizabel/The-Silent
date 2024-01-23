import io
import random
import re
import sys
import TheSilent.dolphin as dolphin
import time
import urllib.parse
from deepface import DeepFace
from itertools import *
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from TheSilent.clear import clear
from TheSilentExt.owl_crawler import owl_crawler
from TheSilent.puppy_requests import text

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def owl(username=None,delay=0,hueristics=False,image=None,keywords=None,sites=None):
    clear()
    
    hits = []

    if sites != None and image != None:
        try:
            DeepFace.verify(image, image)

        except:
            print(RED + "either target image doesn't exist or we can't identify any faces")
            sys.exit()
            
        domains_found = []
        with open(sites, "r") as file:
            for i in file:
                domains_found.append(i.replace("\n", "").rstrip("/"))

        for domain in domains_found:
            print(CYAN + f"crawling: {domain}")
            hosts = owl_crawler(domain,delay)
            for host in hosts:
                if ".gif" in host or ".jpeg" in host or ".jpg" in host or ".png" in host or ".webp" in host:
                    time.sleep(delay)
                    try:
                        if DeepFace.verify(image, io.BytesIO(text(host,raw=True)))["verified"]:
                            hits.append(host)
                    
                    except:
                        pass

    if username != None:
        words = []

        if keywords != None:
            with open(keywords, "r") as file:
                for i in file:
                    words.append(i.replace("\n", ""))
                    

        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)
        
        users = []

        if hueristics:
            hueristics_list = ["123",
                               "365",
                               "1234",
                               "1776",
                               "1812",
                               "247",
                               "24/7",
                               "czech",
                               "mega",
                               "real",
                               "the",
                               "thereal",
                               "the.real",
                               "the-real",
                               "the_real",
                               "vegan",
                               "zoomer"]

            for i in range(102):
                hueristics_list.append(str(i))

            for i in range(1910,2030):
                hueristics_list.append(str(i))

        spacing = product(".-_/",repeat=username.count(" "))
        for space in spacing:
            space_count = 0
            temp_user = username
            for _ in space:
                space_count += 1
                temp_user = temp_user.replace(" ", _, space_count)
                temp_user = temp_user.replace("/", "")

            users.append(temp_user)

        if re.search("^\s*\S+\s+\S+\s*$", username):
            space_enum = len(re.findall("\s*", username)[0])
            space_str = ""
            for _ in range(space_enum):
                space_str += " "

            girly_pattern = []
            if username.startswith(" ") and username.endswith(" "):
                girly_pattern.append(space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0][0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1]+ space_str)
                girly_pattern.append(space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0][0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1] + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1][-1] + space_str)
                girly_pattern.append(space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1][0] + space_str)

            elif username.startswith(" ") and not username.endswith(" "):
                girly_pattern.append(space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0][0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1])
                girly_pattern.append(space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0][0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1] + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1][-1])
                girly_pattern.append(space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1][0])

            elif not username.startswith(" ") and username.endswith(" "):
                girly_pattern.append(re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0][0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1]+ space_str)
                girly_pattern.append(re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0][0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1] + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1][-1] + space_str)
                girly_pattern.append(re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1][0] + space_str)

            
            else:
                girly_pattern.append(re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0][0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1])
                girly_pattern.append(re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0][0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1] + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1][-1])
                girly_pattern.append(re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[0] + space_str + re.sub("\s{2,}", " ", username.rstrip(" ").lstrip(" ")).split(" ")[1][0])

            for girl in girly_pattern:
                spacing = product(".-_/",repeat=girl.count(" "))
                for space in spacing:
                    temp_user = girl
                    space_count = 0
                    for _ in space:
                        space_count += 1
                        temp_user = temp_user.replace(" ", _, space_count)
                        temp_user = temp_user.replace("/", "")

                    users.append(temp_user)

        spacing = [".",
                   "-",
                   "_"]    

        if hueristics:
            temp_users = users[:]
            for hueristic in hueristics_list:
                for space in spacing:
                    for user in temp_users:
                        users.append(hueristic + space + user)
                        users.append(user + space + hueristic)
                        
        users = list(set(users[:]))
        users = random.sample(users, len(users))
        
        contents = {"github": 200,
                    "instagram": "Sorry, this page isn't avimagelable.",
                    "poshmark": 200,
                    "vsco": 200}

        urls = {"github": "https://github.com/{}",
                "instagram": "https://www.instagram.com/{}",
                "poshmark": "https://poshmark.com/closet/{}",
                "vsco": "https://vsco.co/{}"}

        for url in urls.items():
            for user in users:
                print(CYAN + "checking: " + url[1].replace("{}", user))
                time.sleep(delay)
                if contents[url[0]] == 200:
                    try:
                        text(url[1].replace("{}", user))
                        skip = False

                    except:
                        skip = True

                    if not skip:
                        if image != None:
                            crawl = []
                            driver.get(url[1].replace("{}", user))
                            data = driver.page_source
                            links = re.findall("content\s*=\s*[\"\'](\S+)(?=[\"\'])|href\s*=\s*[\"\'](\S+)(?=[\"\'])|src\s*=\s*[\"\'](\S+)(?=[\"\'])",data.lower())
                            for link in links:
                                for _ in link:
                                    _ = re.split("[\"\'\<\>\;\{\}]",_)[0]
                                    if _.startswith("/") and not _.startswith("//"):
                                        crawl.append(f"{urllib.parse.urlparse(url[1]).netloc}{_}")

                                    elif not _.startswith("/") and not _.startswith("http://") and not _.startswith("https://"):
                                        crawl.append(f"{urllib.parse.urlparse(url[1]).netloc}/{_}")

                                    elif _.startswith("http://") or _.startswith("https://"):
                                        crawl.append(_)

                            crawl = list(set(crawl[:]))
                            for crawly in crawl:
                                if ".jpeg" in crawly or ".jpg" in crawly or ".png" in crawly:
                                    time.sleep(delay)
                                    try:
                                        if DeepFace.verify(image, io.BytesIO(text(crawly,raw=True)))["verified"]:
                                            hits.append(url[1].replace("{}", user))
                                    
                                    except:
                                        pass

                        elif keywords != None:
                            driver.get(url[1].replace("{}", user))
                            data = driver.page_source
                            for word in words:
                                if word.lower() in data.lower():
                                    hits.append(url[1].replace("{}", user))

                        else:
                            hits.append(url[1].replace("{}", user))


                else:
                    driver.get(url[1].replace("{}", user))
                    data = driver.page_source
                    if not contents[url[0]] in data:
                        if image != None and keywords != None:
                            crawl = []
                            links = re.findall("content\s*=\s*[\"\'](\S+)(?=[\"\'])|href\s*=\s*[\"\'](\S+)(?=[\"\'])|src\s*=\s*[\"\'](\S+)(?=[\"\'])",data.lower())
                            for link in links:
                                for _ in link:
                                    _ = re.split("[\"\'\<\>\;\{\}]",_)[0]
                                    if _.startswith("/") and not _.startswith("//"):
                                        crawl.append(f"{urllib.parse.urlparse(url[1]).netloc}{_}")

                                    elif not _.startswith("/") and not _.startswith("http://") and not _.startswith("https://"):
                                        crawl.append(f"{urllib.parse.urlparse(url[1]).netloc}/{_}")

                                    elif _.startswith("http://") or _.startswith("https://"):
                                        crawl.append(_)

                            crawl = list(set(crawl[:]))
                            for crawly in crawl:
                                if ".jpeg" in crawly or ".jpg" in crawly or ".png" in crawly:
                                    time.sleep(delay)
                                    try:
                                        if DeepFace.verify(image, io.BytesIO(text(crawly,raw=True)))["verified"]:
                                            hits.append(url[1].replace("{}", user))
                                    
                                    except:
                                        pass

                        elif keywords != None:
                            driver.get(url[1].replace("{}", user))
                            data = driver.page_source
                            for word in words:
                                if word.lower() in data.lower():
                                    hits.append(url[1].replace("{}", user))

                        else:
                            hits.append(url[1].replace("{}", user))

        driver.quit()

    hits = list(set(hits[:]))
    hits.sort()

    clear()
    if len(hits) > 0:
        for hit in hits:
            print(RED + f"found: {hit}")

    else:
        print(GREEN + f"we didn't find anything interesting")
