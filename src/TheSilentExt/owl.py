import io
import numpy as np
import random
import re
import sys
import time
import urllib.parse
from deepface import DeepFace
from itertools import *
from PIL import Image
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from TheSilent.clear import clear
from TheSilentExt.owl_crawler import owl_crawler
from TheSilent.puppy_requests import text

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def owl(username=None,delay=0,image=None,keywords=None,sites=None):
    clear()

    if image != None:
        try:
            DeepFace.verify(image, image)

        except ValueError:
            print(RED + "we either couldn't identify a face or the target image file doesn't exist")
            sys.exit()
    
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
                        if DeepFace.verify(image, np.array(Image.open(io.BytesIO(text(i.get_attribute("src"),raw=True)))))["verified"]:
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

        spacing = [".",
                   "-",
                   "_"]    
        users = []
        spacing = product(".-_/",repeat=username.count(" "))
        for space in spacing:
            space_count = 0
            temp_user = username
            for _ in space:
                space_count += 1
                temp_user = temp_user.replace(" ", _, space_count)
                temp_user = temp_user.replace("/", "")

            users.append(temp_user)
                
        users = list(set(users[:]))
        users = random.sample(users, len(users))
        
        contents = {"github": 200,
                    "instagram": "Sorry, this page isn't available.",
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
                        if image != None and keywords == None:
                            img_elements = driver.find_elements(By.CLASS_NAME, "img")
                            for i in img_elements:
                                if i.get_attribute("src") != None:
                                    time.sleep(delay)
                                    try:
                                        if DeepFace.verify(image, np.array(Image.open(io.BytesIO(text(i.get_attribute("src"), raw=True))).convert("RGB")), enforce_detection=False)["verified"]:
                                            hits.append(url[1].replace("{}", user))
                                            break
                                    
                                    except:
                                        pass
                                    
                            img_elements = driver.find_elements(By.TAG_NAME, "img")
                            for i in img_elements:
                                if i.get_attribute("src") != None:
                                    time.sleep(delay)
                                    try:
                                        if DeepFace.verify(image, np.array(Image.open(io.BytesIO(text(i.get_attribute("src"), raw=True))).convert("RGB")), enforce_detection=False)["verified"]:
                                            hits.append(url[1].replace("{}", user))
                                            break
                                    
                                    except:
                                        pass

                        elif keywords != None:
                            driver.get(url[1].replace("{}", user))
                            time.sleep(delay)
                            data = driver.page_source
                            for word in words:
                                if word.lower() in data.lower():
                                    hits.append(url[1].replace("{}", user))

                        elif image == None and keywords == None:
                            hits.append(url[1].replace("{}", user))


                else:
                    driver.get(url[1].replace("{}", user))
                    data = driver.page_source
                    time.sleep(delay)
                    if not contents[url[0]] in data:
                        if image != None and keywords == None:
                            img_elements = driver.find_elements(By.CLASS_NAME, "img")
                            for i in img_elements:
                                if i.get_attribute("src") != None:
                                    time.sleep(delay)
                                    try:
                                        if DeepFace.verify(image, np.array(Image.open(io.BytesIO(text(i.get_attribute("src"), raw=True))).convert("RGB")), enforce_detection=False)["verified"]:
                                            hits.append(url[1].replace("{}", user))
                                            break
                                    
                                    except:
                                        pass
                                    
                            img_elements = driver.find_elements(By.TAG_NAME, "img")
                            for i in img_elements:
                                if i.get_attribute("src") != None:
                                    time.sleep(delay)
                                    try:
                                       if DeepFace.verify(image, np.array(Image.open(io.BytesIO(text(i.get_attribute("src"), raw=True))).convert("RGB")), enforce_detection=False)["verified"]:
                                            hits.append(url[1].replace("{}", user))
                                            break
                                    
                                    except:
                                        pass

                        elif keywords != None:
                            time.sleep(delay)
                            data = driver.page_source
                            for word in words:
                                if word.lower() in data.lower():
                                    hits.append(url[1].replace("{}", user))

                        elif image == None and keywords == None:
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
