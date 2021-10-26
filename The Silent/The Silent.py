#Documentation:
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
#https://www.w3schools.com/PYTHON/ref_requests_get.asp
#https://www.geeksforgeeks.org/python-check-url-string/
#https://www.w3schools.com/python/gloss_python_check_string.asp
#https://stackoverflow.com/questions/38015537/python-requests-exceptions-sslerror-dh-key-too-small
#https://www.geeksforgeeks.org/create-a-directory-in-python/
#https://stackoverflow.com/questions/7935972/writing-to-a-new-directory-in-python-without-changing-directory
#https://medium.com/@jasonrigden/using-tor-with-the-python-request-library-79015b2606cb
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
#https://content-blockchain.org/research/testing-different-image-hash-functions/
#https://pypi.org/project/ImageHash/

from hashlib import sha256
from PIL import Image
import imagehash
import os
import random
import re
import requests
import time
import urllib3

tor = requests.session()
tor.proxies = {}
tor.proxies["https"] = "socks5h://localhost:9050"

user_agent = {"User-Agent" : "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

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

change_tor_boolean = False
https = True
https_string = "https://"
tor_boolean = False
valid_certificate = True

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
    
def security():
    global change_tor_boolean
    global https
    global https_string
    global tor_boolean
    global valid_certificate
    os.system("clear")
    user_input = input("1 = security status\n2 = edit security\n3 = install tor\n4 = remove tor\n")

    if user_input == "1":
        os.system("clear")
        print("https =", https, "\nvalid certificate =", valid_certificate, "\ntor =", tor_boolean, "\nchange tor circuit with each request =", change_tor_boolean)
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
            tor_boolean = True
            os.system("sudo service tor start")

        if user_tor == "n":
            tor_boolean = False
            os.system("sudo service tor stop")

        os.system("clear")
        user_change_tor = input("change tor circuit with each request? y/n\n")

        if user_change_tor == "y":
            change_tor_boolean = True

        if user_change_tor == "n":
            change_tor_boolean = False

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

def perceptual_hash(file_1, file_2):
    first_hash = imagehash.phash(Image.open(file_1))
    second_hash = imagehash.phash(Image.open(file_2))
    equal = str(first_hash == second_hash)
    hamming_distance = str(first_hash - second_hash)
    result = "equal: " + equal + "\nhamming distance: " + hamming_distance + "\nfile 1 hash: " + str(first_hash) + "\nfile 2 hash: " + str(second_hash)
    return result
            
def no_log():
    global website
    os.system("clear")
    website = input("enter website:\n")
    os.system("clear")
    user_input = input("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url\n")
    
    if user_input == "1":
        print(no_log_cookies(website))
        pause = input()

    if user_input == "2":
        print(no_log_encoding(website))
        pause = input()

    if user_input == "3":
        print(no_log_headers(website))
        pause = input()

    if user_input == "4":
        print(no_log_html_code(website))
        pause = input()

    if user_input == "5":
        print(no_log_ok(website))
        pause = input()

    if user_input == "6":
        print(no_log_permanent_redirect(website))
        pause = input()

    if user_input == "7":
        print(no_log_reason(website))
        pause = input()

    if user_input == "8":
        print(no_log_redirect(website))
        pause = input()

    if user_input == "9":
        print(no_log_status_code(website))
        pause = input()

    if user_input == "10":
        print(no_log_url(website))
        pause = input()

def no_log_cookies(website):
    os.system("clear")
    output = https_string + website

    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.cookies

def no_log_encoding(website):
    os.system("clear")
    output = https_string + website

    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    return final.encoding

def no_log_headers(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.headers
    
def no_log_html_code(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.text
    
def no_log_ok(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.ok
    
def no_log_permanent_redirect(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.is_permanent_redirect

def no_log_reason(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.reason

def no_log_redirect(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.is_redirect
    
def no_log_status_code(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.status_code
    
def no_log_url(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    return final.url

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
        print(log_cookies(website))
        pause = input()
        
    if user_input == "2":
        print(log_encoding(website))
        pause = input()
        
    if user_input == "3":
        print(log_headers(website))
        pause = input()

    if user_input == "4":
        print(log_html_code(website))
        pause = input()

    if user_input == "5":
        print(log_ok(website))
        pause = input()

    if user_input == "6":
        print(log_permanent_redirect(website))
        pause = input()
            
    if user_input == "7":
        print(log_reason(website))
        pause = input()
            
    if user_input == "8":
        print(log_redirect(website))
        pause = input()
            
    if user_input == "9":
        print(log_status_code(website))
        pause = input()
            
    if user_input == "10":
        print(log_url(website))
        pause = input()

def log_cookies(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.cookies)
    file.write("\n\ncookies: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_encoding(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.encoding)
    file.write("\n\nencoding: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_headers(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.headers)
    file.write("\n\nheaders: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_html_code(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.text)
    file.write("\n\nhtml code: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_ok(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.ok) 
    file.write("\n\nok: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_permanent_redirect(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.is_permanent_redirect)
    file.write("\n\npermanent redirect: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_reason(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.reason)
    file.write("\n\nreason: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def log_redirect(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.is_redirect)
    file.write("\n\nredirect: " + result + "\n\n")
    final.close()
    file.close()
    return result

def log_status_code(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.status_code)
    file.write("\n\nstatus code: " + result + "\n\n")
    final.close()
    file.close
    return result
    
def log_url(website):
    os.system("clear")
    output = https_string + website
    
    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    result = str(final.url)
    file.write("\n\nurl: " + result + "\n\n")
    final.close()
    file.close()
    return result
    
def image():
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

    picture = str(output)

    if tor_boolean == True:
        data = tor.get(picture, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        data = requests.get(picture, verify = valid_certificate, headers = user_agent)
        
    with open(os.path.join("data/images", name), "wb") as file_writer:
        file_writer.write(data.content)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    data.close()
    pause = input()

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

    if tor_boolean == True:
        data = tor.get(pdf, stream = True, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        data = requests.get(pdf, stream = True, verify = valid_certificate, headers = user_agent)

    data = requests.get(pdf, stream = True, verify = valid_certificate)

    with open(os.path.join("data/pdf", name), "wb") as pdf:
        for chunk in data.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    data.close()
    pause = input()

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

    if tor_boolean == True:
        final = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        final = requests.get(output, verify = valid_certificate, headers = user_agent)

    file = open(os.path.join("data/html", website + ".html"), "w+")
    file.write(final.text)
    final.close()
    file.close()
    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    pause = input()

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

    if tor_boolean == True:
        url = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        url = requests.get(output, verify = valid_certificate, headers = user_agent)

    out = str(url.text)
    web_list = find_url(out)

    for i in web_list:
        if change_tor_boolean == True:
            os.system("sudo service tor stop")
            os.system("sudo service tor start")
        
        jpeg = ".jpeg" in i
        jpg = ".jpg" in i
        png = ".png" in i
        y = "http" in i

        if jpeg == True and y == True:
            count += 1
            picture = str(i)
            data = requests.get(picture, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/images","image " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == False:
            count += 1
            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/images","image " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == True:
            count += 1
            picture = str(i)
            data = requests.get(picture, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/images","image " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)
                
        if jpg == True and y == False:
            count += 1
            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/images","image " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == True:
            count += 1
            picture = str(i)
            data = requests.get(picture, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/images","image " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == False:
            count += 1
            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/images","image " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    url.close()
    pause = input()

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

    if tor_boolean == True:
        url = tor.get(output, verify = valid_certificate, headers = user_agent)
        
    if tor_boolean == False:
        url = requests.get(output, verify = valid_certificate, headers = user_agent)
        
    out = str(url.text)
    web_list = find_url(out)
    file = open(os.path.join("data/all data", website + ".html"), "w+")
    file.write(url.text)
    url.close()
    file.close()

    for i in web_list:
        if change_tor_boolean == True:
            os.system("sudo service tor stop")
            os.system("sudo service tor start")
        
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
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".app"), "wb") as file_writer:
                file_writer.write(data.content)

        if app == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data","file " + str(count)  + ".app"), "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".avi"), "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".avi"), "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".bat"), "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".bat"), "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".cmd"), "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".cmd"), "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".css"), "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".css"), "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".doc"), "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".doc"), "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".docx"), "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".docx"), "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".exe"), "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".exe"), "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".gif"), "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".gif"), "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".html"), "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".html"), "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jar"), "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jar"), "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".java"), "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".java"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpeg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jpg"), "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jss"), "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".jss"), "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".m4a"), "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".m4a"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp3"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp3"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp4"), "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".mp4"), "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".pdf"), "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".pdf"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".png"), "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".py"), "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".py"), "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".sh"), "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".sh"), "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".txt"), "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".txt"), "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == True:
            count += 1
            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".xml"), "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == False:
            count += 1
            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate, headers = user_agent)

            with open(os.path.join("data/all data", "file " + str(count)  + ".xml"), "wb") as file_writer:
                file_writer.write(data.content)

    end = time.time()
    print("\nTime: " + str(end - start) + " seconds.")
    url.close()
    pause = input()

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
    
def brute_force_dictionary():
    count = 0

    os.system("clear")
    
    user_input = input("Enter name of list: ")

    text_file = open(user_input, "r")
    tracker = text_file.readlines()

    os.system("clear")

    print("Enter password: ")
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

    pause = input()

while True:
    if change_tor_boolean == True:
        os.system("sudo service tor stop")
        os.system("sudo service tor start")
    
    os.system("clear")
    user_input = input("0 = security\n1 = data no log\n2 = data log\n3 = file\n4 = password generator\n5 = brute force (dictionary)\n6 = perceptual hash\n7 = generate password hash\ne = exit\n")

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

    if user_input == "6":
        os.system("clear")
        file_1 = input("name of file 1: ")
        file_2 = input("name of file 2: ")
        print(perceptual_hash(file_1, file_2))
        pause = input()

    if user_input == "7":
        os.system("clear")
        password = input("password: ")
        result = sha256(password.encode("utf-8")).hexdigest()
        print(result)

    if user_input == "e":
        exit()
