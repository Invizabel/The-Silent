import urllib.robotparser

def kitten_crawler(host):
    host = host.rstrip("/")
    hits = [host]

    bot = urllib.robotparser.RobotFileParser()
    bot.set_url(f"{host}/robots.txt")
    bot.read()
    results = str(bot.default_entry).split("\n")
    for result in results:
        if "allow" in str(result):
            rule = "".join(str(result).split(":")[1:]).replace(" ", "")
            if rule.startswith("/"):
                hits.append(f"{host}{rule}")

            else:
                hits.append(f"{host}/{rule}")

    hits = list(dict.fromkeys(hits[:]))
    return hits
