import io
import numpy as np
import random
import sys
import time
from deepface import DeepFace
from PIL import Image
from TheSilent.clear import clear
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.puppy_requests import text

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

def owl(image,delay=0,crawl=1000,sites=[]):
    clear()

    try:
        DeepFace.verify(image, image)

    except ValueError:
        print(RED + "we either couldn't identify a face or the target image file doesn't exist")
        sys.exit()
    
    hits = []

    if sites != None:
        try:
            DeepFace.verify(image, image)

        except:
            print(RED + "either target image doesn't exist or we can't identify any faces")
            sys.exit()

        for site in sites:
            print(CYAN + f"crawling: {site}")
            hosts = kitten_crawler(site,delay,crawl)
            for host in hosts:
                if ".gif" in host or ".jpeg" in host or ".jpg" in host or ".png" in host or ".webp" in host:
                    print(CYAN + f"checking {host}")
                    time.sleep(delay)
                    try:
                        if DeepFace.verify(image, np.array(Image.open(io.BytesIO(text(host,raw=True)))))["verified"]:
                            hits.append(host)
                    
                    except:
                        pass

    hits = list(set(hits[:]))
    hits.sort()

    clear()
    if len(hits) > 0:
        for hit in hits:
            print(RED + f"found: {hit}")

    else:
        print(GREEN + f"we didn't find anything interesting")
