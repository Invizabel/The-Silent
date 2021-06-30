#Documentation:
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
#https://www.w3schools.com/PYTHON/ref_requests_get.asp
#https://www.geeksforgeeks.org/python-check-url-string/
#https://www.w3schools.com/python/gloss_python_check_string.asp
#https://stackoverflow.com/questions/38015537/python-requests-exceptions-sslerror-dh-key-too-small
#https://www.geeksforgeeks.org/create-a-directory-in-python/
#https://stackoverflow.com/questions/7935972/writing-to-a-new-directory-in-python-without-changing-directory
#https://medium.com/@jasonrigden/using-tor-with-the-python-request-library-79015b2606cb

import os
import random
import re
import requests
import time
import urllib3

tor = requests.session()
tor.proxies = {}

tor.proxies["http"] = "socks5h://localhost:9050"
tor.proxies["https"] = "socks5h://localhost:9050"

operating_systems = {}
operating_systems['User-agent'] = "Chrome"

#r = tor.get('https://httpbin.org/user-agent', headers = operating_systems)
#print(r.text)

main_folder = "data"
all_data_folder = "all data"
html_folder = "html"
images_folder = "images"
log_folder = "log"
pdf_folder = "pdf"

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

https = True
tor = False
valid_certificate = True

https_string = "https://"

website = ""

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

except AttributeError:
    pass

def find_url(string):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)
	return [x[0] for x in url]

def the_silent():
    os.system("clear")
    
    user_input = input("0 = security\n1 = data no log\n2 = data log\n3 = file\n4 = password generator\n5 = brute force (dictionary)\n")

    if user_input == "0":
        security()

    if user_input == "1":
        no_log()

    if user_input == "2":
        log()

    if user_input == "3":
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

    if user_input == "4":
        password_generator()

    if user_input == "5":
        brute_force_dictionary()

def security():
    global https
    global tor
    global valid_certificate

    global https_string
    
    os.system("clear")

    user_input = input("1 = security status\n2 = edit security\n3 = install tor\n4 = remove tor\n")

    if user_input == "1":
        os.system("clear")

        print("https =", https, "\nvalid certificate =", valid_certificate, "\ntor =", tor)

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

        user_tor = input("tor? y/n\n")

        if user_tor == "y":
            tor = True

            os.system("sudo service tor start")

        if user_tor == "n":
            tor = False

            os.system("sudo service tor stop")

    if user_input == "3":
        os.system("clear")

        user_tor = input("1 = debian\n2 = fedora\n")

        if user_tor == "1":
            os.system("clear")

            print("installing tor")
            os.system("sudo apt update")
            os.system("sudo apt install tor")

        if user_tor == "2":
            os.system("clear")

            print("installing tor")
            os.system("sudo dnf install tor")

    if user_input == "4":
        os.system("clear")

        user_tor = input("1 = debian\n2 = fedora\n")

        if user_tor == "1":
            os.system("clear")

            print("removing tor")
            os.system("sudo apt purge tor")

        if user_tor == "2":
            os.system("clear")

            print("removing tor")
            os.system("sudo dnf remove tor")

    the_silent()

def no_log():
    global website
    
    os.system("clear")

    website = input("enter website:\n")
    
    os.system("clear")

    user_input = input("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url\n")
    
    if user_input == "1":
        no_log_cookies()

    if user_input == "2":
        no_log_encoding()

    if user_input == "3":
        no_log_headers()

    if user_input == "4":
        no_log_html_code()

    if user_input == "5":
        no_log_ok()

    if user_input == "6":
        no_log_permanent_redirect()

    if user_input == "7":
        no_log_reason()

    if user_input == "8":
        no_log_redirect()

    if user_input == "9":
        no_log_status_code()

    if user_input == "10":
        no_log_url()

def no_log_cookies():
    os.system("clear")
    
    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("cookies: " + str(final.cookies))

    final.close()

    pause = input()

    the_silent()
    
def no_log_encoding():
    os.system("clear")
    
    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("encoding: " + str(final.encoding))

    final.close()

    pause = input()

    the_silent()
    
def no_log_headers():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("headers: " + str(final.headers))

    final.close()

    pause = input()

    the_silent()
    
def no_log_html_code():
    os.system("clear")
    
    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("html code: " + str(final.text))

    final.close()

    pause = input()

    the_silent()
    
def no_log_ok():
    os.system("clear")
    
    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("ok: " + str(final.ok))

    final.close()

    pause = input()

    the_silent()

def no_log_permanent_redirect():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("permanent redirect: " + str(final.is_permanent_redirect))

    final.close()

    pause = input()

    the_silent()

def no_log_reason():
    os.system("clear")
    
    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("reason: " + str(final.reason))

    final.close()

    pause = input()

    the_silent()

def no_log_redirect():
    os.system("clear")
    
    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("redirect: " + str(final.is_redirect))

    final.close()

    pause = input()

    the_silent()

def no_log_status_code():
    os.system("clear")
    
    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("status code: " + str(final.status_code))

    final.close()

    pause = input()

    the_silent()

def no_log_url():
    os.system("clear")
    
    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("url: " + str(final.url))

    final.close()

    pause = input()

    the_silent()
    
def log():
    global file
    global website

    file = open(os.path.join("data/log", "log.txt"), "a")

    os.system("clear")

    website = input("enter website:\n")
    
    os.system("clear")

    print("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url")
    user_input = input()

    if user_input == "1":
        log_cookies()
        
    if user_input == "2":
        log_encoding()
        
    if user_input == "3":
        log_headers()

    if user_input == "4":
        log_html_code()

    if user_input == "5":
        log_ok()

    if user_input == "6":
        log_permanent_redirect()
            
    if user_input == "7":
        log_reason()
            
    if user_input == "8":
        log_redirect()
            
    if user_input == "9":
        log_status_code()
            
    if user_input == "10":
        log_url()

def log_cookies():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("cookies: " + str(final.cookies))
    file.write("\n\ncookies: " + str(final.cookies))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_encoding():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("encoding: " + str(final.encoding))
    file.write("\n\nencoding: " + str(final.encoding))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_headers():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("headers: " + str(final.headers))
    file.write("\n\nheaders: " + str(final.headers))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_html_code():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("html code: " + str(final.text))
    file.write("\n\nhtml code: " + str(final.text))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_ok():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("ok: " + str(final.ok))
    file.write("\n\nok: " + str(final.ok))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_permanent_redirect():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("permanent redirect: " + str(final.is_permanent_redirect))
    file.write("\n\npermanent redirect: " + str(final.is_permanent_redirect))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_reason():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("reason: " + str(final.reason))
    file.write("\n\nreason: " + str(final.reason))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_redirect():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("redirect: " + str(final.is_redirect))
    file.write("\n\nredirect: " + str(final.is_redirect))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_status_code():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("status code: " + str(final.status_code))
    file.write("\n\nstatus code: " + str(final.status_code))

    final.close()
    file.close

    pause = input()

    the_silent()

def log_url():
    os.system("clear")

    output = https_string + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("url: " + str(final.url))
    file.write("\n\nurl: " + str(final.url) + "\n\n")

    final.close()
    file.close()

    pause = input()

    the_silent()

def image():
    secure = ""

    global website
    
    os.system("clear")

    website = input("enter website:\n")

    os.system("clear")
    
    name = input("\nenter desired name:\n")
    
    os.system("clear")
    print("Downloading!")

    start = time.time()

    if https == True:
        secure = "https://"

    if https == False:
        secure = "http://"
    
    output = secure + website

    picture = str(output)

    data = requests.get(picture, verify = valid_certificate)

    with open(os.path.join("data/images", name), "wb") as file_writer:
        file_writer.write(data.content)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")

    data.close()

    the_silent()

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

    data = requests.get(pdf, stream = True, verify = valid_certificate)

    with open(os.path.join("data/pdf", name), "wb") as pdf:
        for chunk in data.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")

    data.close()

    the_silent()

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

    final = requests.get(output, verify = valid_certificate)

    file = open(os.path.join("data/html", website + ".html"), "w+")
    file.write(final.text)

    final.close()
    file.close()

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")

    the_silent()

def all_images():
    secure = ""
    
    count = 0
    
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

    url = requests.get(output, verify = valid_certificate)
    out = str(url.text)
    web_list = find_url(out)

    for i in web_list:
        jpeg = ".jpeg" in i
        jpg = ".jpg" in i
        png = ".png" in i
        y = "http" in i

        if jpeg == True and y == True:
            count += 1

            picture = str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open(os.path.join("data/images","image " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == False:
            count += 1

            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open(os.path.join("data/images","image " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == True:
            count += 1

            picture = str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open(os.path.join("data/images","image " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)
                
        if jpg == True and y == False:
            count += 1

            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open(os.path.join("data/images","image " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == True:
            count += 1

            picture = str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open(os.path.join("data/images","image " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == False:
            count += 1

            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open(os.path.join("data/images","image " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")

    url.close()

    pause = input()

    the_silent()

def all_data():
    secure = ""

    count = 0
    
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

    url = requests.get(output, verify = valid_certificate)
    out = str(url.text)
    web_list = find_url(out)

    file = open(os.path.join("data/all data", website + ".html"), "w+")
    file.write(url.text)

    url.close()
    file.close()

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

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".app"), "wb") as file_writer:
                file_writer.write(data.content)

        if app == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data","file " + str(count)  + ".app"), "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".avi"), "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".avi"), "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".bat"), "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".bat"), "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".cmd"), "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".cmd"), "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".css"), "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".css"), "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".doc"), "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".doc"), "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".docx"), "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".docx"), "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".exe"), "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".exe"), "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".gif"), "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".gif"), "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".html"), "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".html"), "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jar"), "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jar"), "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".java"), "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".java"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jss"), "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jss"), "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".m4a"), "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".m4a"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp3"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp3"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp4"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp4"), "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".pdf"), "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".pdf"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".py"), "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".py"), "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".sh"), "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".sh"), "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".txt"), "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".txt"), "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".xml"), "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open(os.path.join("data/all data", "file " + str(count)  + ".xml"), "wb") as file_writer:
                file_writer.write(data.content)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")

    url.close()

    pause = input()

    the_silent()

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

    print("Password:", output)

    pause = input()

    the_silent()

def brute_force_dictionary():
    count = 0

    os.system("clear")
    
    user_input = input("Enter name of list:")

    text_file = open(user_input, "r")
    tracker = text_file.readlines()

    os.system("clear")

    print("Enter password:")
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

    the_silent()
			
the_silent()
