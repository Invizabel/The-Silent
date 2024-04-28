import urllib.robotparser
from TheSilent.puppy_requests import text

CYAN = "\033[1;36m"

def kitten_crawler(host):
    host = host.rstrip("/")
    hits = [host]
    
    try:
        bot = urllib.robotparser.RobotFileParser()
        bot.set_url(f"{host}/robots.txt")
        bot.read()
        results = str(bot.default_entry).split("\n")
        for result in results:
            if "allow" in str(result):
                rule = "".join(str(result).split(":")[1:]).replace(" ", "")
                if rule.startswith("/"):
                    try:
                        print(CYAN + f"checking for 200 status code: {host}{rule}")
                        text(f"{host}{rule}")
                        hits.append(f"{host}{rule}")

                    except:
                        pass
                    

                else:
                    try:
                        print(CYAN + f"checking for 200 status code: {host}/{rule}")
                        text(f"{host}/{rule}")
                        hits.append(f"{host}/{rule}")

                    except:
                        pass

    except:
        pass
        
    hits = list(dict.fromkeys(hits[:]))
    return hits
