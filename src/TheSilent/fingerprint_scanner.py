import hashlib
import time
import re
from urllib.error import HTTPError
from TheSilent.puppy_requests import text, getheaders

def fingerprint_server(host, delay):
    hits = []
    status_hits = []
    
    favicon_paths = ["favicon.ico"]
    wordpress_paths = ["", "licence.txt", "readme.html", "wp-admin"]

    fingerprint_favicon_dict = {"content-keeper": "06c673c63c930a65265e75e32ea49c6095c3628c5f82c8c06181a93a84e7948f",
                                "proxmox": "f171ad34a7b8fd7ccc8da32e5afdaecf11f7ab1cfbd57adef22620b242c2a6eb"}

    # get headers
    try:
        http_banner = re.findall(r"server:\s*(.+)", str(getheaders(host)).lower())[0]
        hits.append(f"http banner: {http_banner}")

    except:
        pass

    # get favicons
    path_bool = True
    for path in favicon_paths:
        time.sleep(delay)
        try:
            if not path_bool:
                break
            
            data = text(host + "/" + path, raw = True)
            status_hits.append(200)
            for i, j in fingerprint_favicon_dict.items():
                if j == hashlib.sha256(data).hexdigest():
                    hits.append(f"found: {i}")
                    path_bool = False
                    break

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

    # detect wordpress
    for path in wordpress_paths:
        time.sleep(delay)
        try:
            if not path_bool:
                break
            
            data = text(host + "/" + path).lower()
            status_hits.append(200)
            if re.search(r"word\s*press|wp-content|wp-includes", data):
                hits.append("found: wordpress")
                path_bool = False
                break

        except HTTPError as error:
            status_hits.append(error.code)

        except:
            pass

    return hits, status_hits