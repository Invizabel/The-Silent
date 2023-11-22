import time
import urllib
from urllib.parse import urlparse
import TheSilent.puppy_requests as puppy
from TheSilent.clear import clear
from TheSilent.return_user_agent import return_user_agent

CYAN = "\033[1;36m"
RED = "\033[1;31m"

def owl(username,delay=0):
    clear()

    my_list = []

    special_list = ["_", "-", ".", ""]
    username_list = []

    website_dict = {
        "AllMyLinks": "https://allmylinks.com/{}",
        "Apple Developer": "https://developer.apple.com/forums/profile/{}",
        "Apple Discussions": "https://discussions.apple.com/profile/{}",
        "Archive.org": "https://archive.org/details/@{}",
        "Ask Fedora": "https://ask.fedoraproject.org/u/{}",
        "Bandcamp": "https://www.bandcamp.com/{}",
        "BongaCams": "https://pt.bongacams.com/profile/{}",
        "BraveCommunity": "https://community.brave.com/u/{}/",
        "BuyMeACoffee": "https://buymeacoff.ee/{}",
        "BuzzFeed": "https://buzzfeed.com/{}",
        "ChaturBate": "https://chaturbate.com/{}",
        "CloudflareCommunity": "https://community.cloudflare.com/u/{}",
        "Codecademy": "https://www.codecademy.com/profiles/{}",
        "Cryptomator Forum": "https://community.cryptomator.org/u/{}",
        "DailyMotion": "https://www.dailymotion.com/{}",
        "Fandom": "https://www.fandom.com/u/{}",
        "FortniteTracker": "https://fortnitetracker.com/profile/all/{}",
        "Freesound": "https://freesound.org/people/{}/",
        "Gamespot": "https://www.gamespot.com/profile/{}/",
        "Genius (Artists)": "https://genius.com/artists/{}",
        "Genius (Users)": "https://genius.com/{}",
        "geocaching": "https://www.geocaching.com/p/default.aspx?u={}",
        "Giphy": "https://giphy.com/{}",
        "GitHub": "https://www.github.com/{}",
        "GoodReads": "https://www.goodreads.com/{}",
        "HackerOne": "https://hackerone.com/{}",
        "Instructables": "https://www.instructables.com/member/{}",
        "Linktree": "https://linktr.ee/{}",
        "Minecraft": "https://api.mojang.com/users/profiles/minecraft/{}",
        "Newgrounds": "https://{}.newgrounds.com",
        "OnlyFans": "https://onlyfans.com/api2/v2/users/{}",
        "OpenStreetMap": "https://www.openstreetmap.org/user/{}",
        "Oracle Community": "https://community.oracle.com/people/{}",
        "Pastebin": "https://pastebin.com/u/{}",
        "Patreon": "https://www.patreon.com/{}",
        "Periscope": "https://www.periscope.tv/{}/",
        "Pinterest": "https://www.pinterest.com/{}/",
        "PlayStore": "https://play.google.com/store/apps/developer?id={}",
        "Pokemon Showdown": "https://pokemonshowdown.com/users/{}",
        "Pornhub": "https://pornhub.com/users/{}",
        "Poshmark": "https://poshmark.com/closet/{}",
        "PyPi": "https://pypi.org/user/{}",
        "Quizlet": "https://quizlet.com/{}",
        "Roblox": "https://www.roblox.com/user.aspx?username={}",
        "RoyalCams": "https://royalcams.com/profile/{}",
        "Scratch": "https://scratch.mit.edu/users/{}",
        "Signal": "https://community.signalusers.org/u/{}",
        "Slack": "https://{}.slack.com",
        "Slant": "https://www.slant.co/users/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "SourceForge": "https://sourceforge.net/u/{}",
        "Speedrun.com": "https://www.speedrun.com/users/{}",
        "TikTok": "https://tiktok.com/@{}",
        "Trello": "https://trello.com/1/Members/{}",
        "Twitch": "https://m.twitch.tv/{}",
        "Vimeo": "https://vimeo.com/{}",
        "VirusTotal": "https://www.virustotal.com/ui/users/{}/avatar",
        "VSCO": "https://vsco.co/{}",
        "Wattpad": "https://www.wattpad.com/api/v3/users/{}/",
        "Xbox Gamertag": "https://xboxgamertag.com/search/{}",
        "xHamster": "https://xhamster.com/users/{}",
        "Xvideos": "https://xvideos.com/profiles/{}",
        "YouPorn": "https://youporn.com/uservids/{}"}
    type_dict = {
        "AllMyLinks": "Not Found[False]",
        "Apple Developer": "status_code",
        "Apple Discussions": "The page you tried was not found. You may have used an outdated link or may have typed the address (URL) incorrectly.[False]",
        "Archive.org": "cannot find account[False]",
        "Ask Fedora": "status_code",
        "Bandcamp": "status_code",
        "BongaCams": "status_code",
        "BraveCommunity": "status_code",
        "BuyMeACoffee": "status_code",
        "BuzzFeed": "status_code",
        "ChaturBate": "status_code",
        "CloudflareCommunity": "status_code",
        "Codecademy": "This profile could not be found[False]",
        "Codecademy": "This profile could not be found",
        "Cryptomator Forum": "status_code",
        "DailyMotion": "status_code",
        "Fandom": "status_code",
        "FortniteTracker": "status_code",
        "Freesound": "status_code",
        "Gamespot": "status_code",
        "Genius (Artists)": "status_code",
        "Genius (Users)": "status_code",
        "geocaching": "status_code",
        "Giphy": "status_code",
        "GitHub": "status_code",
        "GoodReads": "status_code",
        "HackerOne": "status_code",
        "Instructables": "status_code",
        "Linktree": "status_code",
        "Minecraft": "status_code",
        "Newgrounds": "status_code",
        "OnlyFans": "status_code",
        "OpenStreetMap": "status_code",
        "Oracle Community": "status_code",
        "Pastebin": "Not Found (#404)[False]",
        "Patreon": "status_code",
        "Periscope": "status_code",
        "Pinterest": "@{}[True]",
        "PlayStore": "status_code",
        "Pokemon Showdown": "Pokemon Showdown",
        "Pornhub": "status_code",
        "Poshmark": "status_code",
        "PyPi": "status_code",
        "Quizlet": "status_code",
        "Roblox": "status_code",
        "RoyalCams": "status_code",
        "Scratch": "status_code",
        "Signal": "Oops! That page doesn\u2019t exist or is private.[False]",
        "Slack": "status_code",
        "Slant": "status_code",
        "SoundCloud": "status_code",
        "SourceForge": "status_code",
        "Speedrun.com": "status_code",
        "TikTok": "status_code",
        "Trello": "model not found[False]",
        "Twitch": "status_code",
        "Vimeo": "status_code",
        "VirusTotal": "status_code",
        "VSCO": "status_code",
        "Wattpad": "status_code",
        "Xbox Gamertag": "status_code",
        "xHamster": "status_code",
        "Xvideos": "status_code",
        "YouPorn": "status_code"}

    for i in special_list:
        username_list.append(username.replace(" ", i))
        try:
            new_name = username.split(" ")

        except IndexError:
            continue

    if " " not in username:
        for i in range(len(list(website_dict.values()))):
            time.sleep(delay)
            print(CYAN + "Checking: " + list(website_dict)[i] + " (" + username + ")")

            if list(type_dict.values())[i] == "status_code":
                url = list(website_dict.values())[i]
                url = url.replace("{}", username)

                try:
                    my_request = puppy.text(url)
                    print(CYAN + "True: " + list(website_dict)[i] + " (" + username + ")")
                    my_list.append(list(website_dict)[i] + " (" + username + ")")

                except urllib.error.HTTPError:
                    pass

                except PermissionError:
                    print(RED + "ERROR!")

                try:
                    if list(type_dict.values())[i] != "status_code":
                        url = list(website_dict.values())[i]
                        url = url.replace("{}", username)

                        my_request = puppy.text(url)

                        parse = list(type_dict.values())[i].replace("{}", username)
                        parse = parse.replace("[False]", "")
                        parse = parse.replace("[True]", "")

                        if parse not in my_request and "[False]" in list(type_dict.values())[i]:
                            print(CYAN + "True: " + list(website_dict)[i] + " (" + username + ")")
                            my_list.append(list(website_dict)[i] + " (" + username + ")")

                        if parse in my_request and "[True]" in list(type_dict.values())[i]:
                            print(CYAN + "True: " + list(website_dict)[i] + " (" + username + ")")
                            my_list.append(list(website_dict)[i] + " (" + username + ")")

                except urllib.error.HTTPError:
                    pass

                except:
                    print(RED + "ERROR!")

    if " " in username:
        for i in range(len(list(website_dict.values()))):
            for new_name in username_list:
                time.sleep(delay)
                print(CYAN + "Checking: " + list(website_dict)[i] + " (" + new_name + ")")
                if list(type_dict.values())[i] == "status_code":
                    url = list(website_dict.values())[i]
                    url = url.replace("{}", new_name)

                    try:
                        my_request = puppy.text(url)
                        print(CYAN + "True: " + list(website_dict)[i] + " (" + new_name + ")")
                        my_list.append(list(website_dict)[i] + " (" + new_name + ")")

                    except urllib.error.HTTPError:
                        pass
                
                    except:
                        print(RED + "ERROR!")

                    try:
                        if list(type_dict.values())[i] != "status_code":
                            url = list(website_dict.values())[i]
                            url = url.replace("{}", new_name)

                            my_request = puppy.text(url)

                            parse = list(type_dict.values())[i].replace("{}", username)
                            parse = parse.replace("[False]", "")
                            parse = parse.replace("[True]", "")

                            if parse not in my_request and "[False]" in list(type_dict.values())[i]:
                                print(CYAN + "True: " + list(website_dict)[i] + " (" + new_name + ")")
                                my_list.append(list(website_dict)[i] + " (" + new_name + ")")

                            if parse in my_request and "[True]" in list(type_dict.values())[i]:
                                print(CYAN + "True: " + list(website_dict)[i] + " (" + new_name + ")")
                                my_list.append(list(website_dict)[i] + " (" + new_name + ")")

                    except urllib.error.HTTPError:
                        pass

                    except:
                        print(RED + "ERROR!")

    print(CYAN + "")
    clear()

    return my_list
