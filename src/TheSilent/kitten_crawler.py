import re
import time
import urllib.parse
import urllib.robotparser
from TheSilent.puppy_requests import text

CYAN = "\033[1;36m"

def kitten_crawler(host, delay = 0, crawl = 1, ethics = True):
    host = host.rstrip("/")

    try:
        if len(text(f"{host}/robots.txt")) > 2:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(f"{host}/robots.txt")
            rp.read()
            crawl_all = False

        else:
            crawl_all = True

    except:
        crawl_all = True
        
    hits = [host]
    total = []
    depth = -1
    for depth in range(crawl):
        hits = list(dict.fromkeys(hits[:]))
        try:
            if urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(hits[depth]).netloc or ".js" in hits[depth]:
                if ethics and not crawl_all and rp.can_fetch("*", urllib.parse.urlparse(hits[depth]).path) and rp.can_fetch("GPTBot", urllib.parse.urlparse(hits[depth]).path):
                    valid = bytes(hits[depth],"ascii")
                    time.sleep(delay)
                    print(CYAN + f"crawling: {hits[depth]}")
                    data = text(hits[depth])
                    total.append(hits[depth])

                elif not ethics or crawl_all:
                    valid = bytes(hits[depth],"ascii")
                    time.sleep(delay)
                    print(CYAN + f"crawling: {hits[depth]}")
                    data = text(hits[depth])
                    total.append(hits[depth])

        except IndexError:
            break

        except:
            continue

        try:
            links = re.findall(r"content\s*=\s*[\"\']([\x21-\x7e]+)(?=[\"\'])|href\s*=\s*[\"\']([\x21-\x7e]+)(?=[\"\'])|src\s*=\s*[\"\']([\x21-\x7e]+)(?=[\"\'])", data.lower())
            for link in links:
                for _ in link:
                    _ = re.split(r"[\"\'\<\>\;\{\}\,\(\)]",_)[0]
                    if _.startswith("/") and not _.startswith("//"):
                        hits.append(f"{host}{_}".rstrip("/"))

                    elif not _.startswith("/") and not _.startswith("http://") and not _.startswith("https://"):
                        hits.append(f"{host}/{_}".rstrip("/"))

                    elif _.startswith("http://") or _.startswith("https://"):
                        hits.append(_.rstrip("/"))

        except:
            pass

    hits = list(dict.fromkeys(hits[:]))
    hits.sort()
    results = []
    for hit in total:
        try:
            if urllib.parse.urlparse(host).netloc in hit:
                valid = bytes(hit, "ascii")
                results.append(hit)

        except:
            pass

    return results
