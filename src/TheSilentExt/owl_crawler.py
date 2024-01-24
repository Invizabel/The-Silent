import re
import time
import urllib.parse
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

CYAN = "\033[1;36m"

def owl_crawler(host,delay=0):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)

    hits = [host]
    total = []
    depth = -1
    while True:
        depth += 1
        hits = list(dict.fromkeys(hits[:]))
        try:
            if urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(hits[depth]).netloc or ".js" in hits[depth] or ".gif" in hit or ".jpeg" in hit or ".jpg" in hit or ".png" in hit or ".webp" in hit:
                time.sleep(delay)
                valid = bytes(hits[depth],"ascii")
                print(CYAN + hits[depth])
                driver.get(hits[depth])
                time.seep(5)
                data = driver.page_source
                total.append(hits[delay])

        except IndexError:
            break

        except:
            continue

        try:
            links = re.findall("content\s*=\s*[\"\'](\S+)(?=[\"\'])|href\s*=\s*[\"\'](\S+)(?=[\"\'])|src\s*=\s*[\"\'](\S+)(?=[\"\'])",data.lower())
            for link in links:
                for _ in link:
                    _ = re.split("[\"\'\<\>\;\{\}]",_)[0]
                    if _.startswith("/") and not _.startswith("//"):
                        hits.append(f"{host}{_}")

                    elif not _.startswith("/") and not _.startswith("http://") and not _.startswith("https://"):
                        hits.append(f"{host}/{_}")

                    elif _.startswith("http://") or _.startswith("https://"):
                        hits.append(_)

        except:
            pass

    hits = list(dict.fromkeys(hits[:]))
    hits.sort()
    results = []
    for hit in total:
        try:
            if urllib.parse.urlparse(host).netloc in hit or ".gif" in hit or ".jpeg" in hit or ".jpg" in hit or ".png" in hit or ".webp" in hit:
                valid = bytes(hit,"ascii")
                results.append(hit)

        except UnicodeDecodeError:
            pass

    return results
