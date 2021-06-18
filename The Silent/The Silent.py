#Documentation:
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
#https://www.w3schools.com/PYTHON/ref_requests_get.asp
#https://www.geeksforgeeks.org/python-check-url-string/
#https://www.w3schools.com/python/gloss_python_check_string.asp
#https://stackoverflow.com/questions/38015537/python-requests-exceptions-sslerror-dh-key-too-small
#https://www.geeksforgeeks.org/create-a-directory-in-python/

import os
import random
import re
import requests
import time
import urllib3

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
valid_certificate = True

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
    global valid_certificate
    
    os.system("clear")

    user_input = input("1 = security status\n2 = edit security\n")

    if user_input == "1":
        os.system("clear")

        print("https =", https, "\nvalid certificate =", valid_certificate)

        pause = input()

    if user_input == "2":
        os.system("clear")

        user_https = input("https? y/n\n")

        if user_https == "y":
            https = True

        if user_https == "n":
            https = False

        os.system("clear")
        
        user_valid_certificate = input("valid certificate? y/n\n")

        if user_valid_certificate == "y":
            valid_certificate = True

        if user_valid_certificate == "n":
            valid_certificate = False
            
    the_silent()
    
def no_log():
    global website
    
    os.system("clear")

    website = input("enter website:\n")
    
    os.system("clear")

    user_input = input("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url\n")
    
    if user_input == "1" and https == True:
        no_log_cookies_secure()
            
    if user_input == "1" and https == False:
        no_log_cookies_not_secure()
            
    if user_input == "2" and https == True:
        no_log_encoding_secure()
            
    if user_input == "2" and https == False:
        no_log_encoding_not_secure()
            
    if user_input == "3" and https == True:
        no_log_headers_secure()
            
    if user_input == "3" and https == False:
        no_log_headers_not_secure()
            
    if user_input == "4" and https == True:
        no_log_html_code_secure()
            
    if user_input == "4" and https == False:
        no_log_html_code_not_secure()
            
    if user_input == "5" and https == True:
        no_log_ok_secure()
            
    if user_input == "5" and https == False:
        no_log_ok_not_secure()
            
    if user_input == "6" and https == True:
        no_log_permanent_redirect_secure()
            
    if user_input == "6" and https == False:
        no_log_permanent_redirect_not_secure()
            
    if user_input == "7" and https == True:
        no_log_reason_secure()
            
    if user_input == "7" and https == False:
        no_log_reason_not_secure()
            
    if user_input == "8" and https == True:
        no_log_redirect_secure()
            
    if user_input == "8" and https == False:
        no_log_redirect_not_secure()
            
    if user_input == "9" and https == True:
        no_log_status_code_secure()
            
    if user_input == "9" and https == False:
        no_log_status_code_not_secure()
            
    if user_input == "10" and https == True:
        no_log_url_secure()
            
    if user_input == "10" and https == False:
        no_log_url_not_secure()
	    
def no_log_cookies_secure():
    os.system("clear")
    
    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("cookies: " + str(final.cookies))

    final.close()

    pause = input()

    the_silent()

def no_log_cookies_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("cookies: " + str(final.cookies))

    final.close()

    pause = input()

    the_silent()

def no_log_encoding_secure():
    os.system("clear")
    
    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("encoding: " + str(final.encoding))

    final.close()

    pause = input()

    the_silent()

def no_log_encoding_not_secure():
    os.system("clear")
    
    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("encoding: " + str(final.encoding))

    final.close()

    pause = input()

    the_silent()

def no_log_headers_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("headers: " + str(final.headers))

    final.close()

    pause = input()

    the_silent()

def no_log_headers_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("headers: " + str(final.headers))

    final.close()

    pause = input()

    the_silent()

def no_log_html_code_secure():
    os.system("clear")
    
    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("html code: " + str(final.text))

    final.close()

    pause = input()

    the_silent()

def no_log_html_code_not_secure():
    os.system("clear")
    
    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("html code: " + str(final.text))

    final.close()

    pause = input()

    the_silent()

def no_log_ok_secure():
    os.system("clear")
    
    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("ok: " + str(final.ok))

    final.close()

    pause = input()

    the_silent()

def no_log_ok_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("ok: " + str(final.ok))

    final.close()

    pause = input()

    the_silent()

def no_log_permanent_redirect_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("permanent redirect: " + str(final.is_permanent_redirect))

    final.close()

    pause = input()

    the_silent()

def no_log_permanent_redirect_not_secure():
    os.system("clear")
    
    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("permanent redirect: " + str(final.is_permanent_redirect))

    final.close()

    pause = input()

    the_silent()

def no_log_reason_secure():
    os.system("clear")
    
    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("reason: " + str(final.reason))

    final.close()

    pause = input()

    the_silent()

def no_log_reason_not_secure():
    os.system("clear")
    
    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("reason: " + str(final.reason))

    final.close()

    pause = input()

    the_silent()
	
def no_log_redirect_secure():
    os.system("clear")
    
    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("redirect: " + str(final.is_redirect))

    final.close()

    pause = input()

    the_silent()

def no_log_redirect_not_secure():
    os.system("clear")
    
    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("redirect: " + str(final.is_redirect))

    final.close()

    pause = input()

    the_silent()

def no_log_status_code_secure():
    os.system("clear")
    
    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("status code: " + str(final.status_code))

    final.close()

    pause = input()

    the_silent()

def no_log_status_code_not_secure():
    os.system("clear")
    
    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("status code: " + str(final.status_code))

    final.close()

    pause = input()

    the_silent()

def no_log_url_secure():
    os.system("clear")
    
    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("url: " + str(final.url))

    final.close()

    pause = input()

    the_silent()

def no_log_url_not_secure():
    os.system("clear")
    
    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("url: " + str(final.url))

    final.close()

    pause = input()

    the_silent()

def log():
    global file
    file = open("log.txt", "a")
    
    global website
    
    os.system("clear")

    website = input("enter website:\n")
    
    os.system("clear")

    print("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url")
    user_input = input()

    if user_input == "1" and https == True:
        log_cookies_secure()
            
    if user_input == "1" and https == False:
        log_cookies_not_secure()
            
    if user_input == "2" and https == True:
        log_encoding_secure()
            
    if user_input == "2" and https == False:
        log_encoding_not_secure()
            
    if user_input == "3" and https == True:
        log_headers_secure()
            
    if user_input == "3" and https == False:
        log_headers_not_secure()
            
    if user_input == "4" and https == True:
        log_html_code_secure()
            
    if user_input == "4" and https == False:
        log_html_code_not_secure()
            
    if user_input == "5" and https == True:
        log_ok_secure()
            
    if user_input == "5" and https == False:
        log_ok_not_secure()
            
    if user_input == "6" and https == True:
        log_permanent_redirect_secure()
            
    if user_input == "6" and https == False:
        log_permanent_redirect_not_secure()
            
    if user_input == "7" and https == True:
        log_reason_secure()
            
    if user_input == "7" and https == False:
        log_reason_not_secure()
            
    if user_input == "8" and https == True:
        log_redirect_secure()
            
    if user_input == "8" and https == False:
        log_redirect_not_secure()
            
    if user_input == "9" and https == True:
        log_status_code_secure()
            
    if user_input == "9" and https == False:
        log_status_code_not_secure()
            
    if user_input == "10" and https == True:
        log_url_secure()
            
    if user_input == "10" and https == False:
        log_url_not_secure()
        
def log_cookies_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("cookies: " + str(final.cookies))
    file.write("\n\ncookies: " + str(final.cookies))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_cookies_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("cookies: " + str(final.cookies))
    file.write("\n\ncookies: " + str(final.cookies))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_encoding_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("encoding: " + str(final.encoding))
    file.write("\n\nencoding: " + str(final.encoding))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_encoding_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("encoding: " + str(final.encoding))
    file.write("\n\nencoding: " + str(final.encoding))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_headers_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("headers: " + str(final.headers))
    file.write("\n\nheaders: " + str(final.headers))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_headers_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("headers: " + str(final.headers))
    file.write("\n\nheaders: " + str(final.headers))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_html_code_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("html code: " + str(final.text))
    file.write("\n\nhtml code: " + str(final.text))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_html_code_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("html code: " + str(final.text))
    file.write("\n\nhtml code: " + str(final.text))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_ok_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("ok: " + str(final.ok))
    file.write("\n\nok: " + str(final.ok))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_ok_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("ok: " + str(final.ok))
    file.write("\n\nok: " + str(final.ok))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_permanent_redirect_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("permanent redirect: " + str(final.is_permanent_redirect))
    file.write("\n\npermanent redirect: " + str(final.is_permanent_redirect))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_permanent_redirect_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("permanent redirect: " + str(final.is_permanent_redirect))
    file.write("\n\npermanent redirect: " + str(final.is_permanent_redirect))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_reason_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("reason: " + str(final.reason))
    file.write("\n\nreason: " + str(final.reason))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_reason_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("reason: " + str(final.reason))
    file.write("\n\nreason: " + str(final.reason))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_redirect_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("redirect: " + str(final.is_redirect))
    file.write("\n\nredirect: " + str(final.is_redirect))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_redirect_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("redirect: " + str(final.is_redirect))
    file.write("\n\nredirect: " + str(final.is_redirect))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_status_code_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("status code: " + str(final.status_code))
    file.write("\n\nstatus code: " + str(final.status_code))

    final.close()
    file.close

    pause = input()

    the_silent()

def log_status_code_not_secure():
    os.system("clear")

    output = "http://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("status code: " + str(final.status_code))
    file.write("\n\nstatus code: " + str(final.status_code))

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_url_secure():
    os.system("clear")

    output = "https://" + website
    
    final = requests.get(output, verify = valid_certificate)
    
    print("url: " + str(final.url))
    file.write("\n\nurl: " + str(final.url) + "\n\n")

    final.close()
    file.close()

    pause = input()

    the_silent()

def log_url_not_secure():
    os.system("clear")

    output = "http://" + website
    
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

    with open(name, "wb") as file_writer:
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

    with open(name, "wb") as pdf:
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

    file = open(user_input + ".html", "w+")
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

            with open("image " + str(count)  + ".jpeg", "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == False:
            count += 1

            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open("image " + str(count)  + ".jpeg", "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == True:
            count += 1

            picture = str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open("image " + str(count)  + ".jpg", "wb") as file_writer:
                file_writer.write(data.content)
                
        if jpg == True and y == False:
            count += 1

            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open("image " + str(count)  + ".jpg", "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == True:
            count += 1

            picture = str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open("image " + str(count)  + ".png", "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == False:
            count += 1

            picture = secure + str(i)
            data = requests.get(picture, verify = valid_certificate)

            with open("image " + str(count)  + ".png", "wb") as file_writer:
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

    file = open(user_input + ".html", "w+")
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

            with open("file " + str(count)  + ".app", "wb") as file_writer:
                file_writer.write(data.content)

        if app == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".app", "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".avi", "wb") as file_writer:
                file_writer.write(data.content)

        if avi == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".avi", "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".bat", "wb") as file_writer:
                file_writer.write(data.content)

        if bat == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".bat", "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".cmd", "wb") as file_writer:
                file_writer.write(data.content)

        if cmd == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".cmd", "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".css", "wb") as file_writer:
                file_writer.write(data.content)

        if css == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".css", "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".doc", "wb") as file_writer:
                file_writer.write(data.content)

        if doc == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".doc", "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".docx", "wb") as file_writer:
                file_writer.write(data.content)

        if docx == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".docx", "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".exe", "wb") as file_writer:
                file_writer.write(data.content)

        if exe == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".exe", "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".gif", "wb") as file_writer:
                file_writer.write(data.content)

        if gif == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".gif", "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".html", "wb") as file_writer:
                file_writer.write(data.content)

        if html == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".html", "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".jar", "wb") as file_writer:
                file_writer.write(data.content)

        if jar == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".jar", "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".java", "wb") as file_writer:
                file_writer.write(data.content)

        if java == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".java", "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".jpeg", "wb") as file_writer:
                file_writer.write(data.content)

        if jpeg == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".jpeg", "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".jpg", "wb") as file_writer:
                file_writer.write(data.content)

        if jpg == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".jpg", "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".jss", "wb") as file_writer:
                file_writer.write(data.content)

        if jss == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".jss", "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".m4a", "wb") as file_writer:
                file_writer.write(data.content)

        if m4a == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".m4a", "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".mp3", "wb") as file_writer:
                file_writer.write(data.content)

        if mp3 == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".mp3", "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".mp4", "wb") as file_writer:
                file_writer.write(data.content)

        if mp4 == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".mp4", "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".pdf", "wb") as file_writer:
                file_writer.write(data.content)

        if pdf == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".pdf", "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".png", "wb") as file_writer:
                file_writer.write(data.content)

        if png == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".png", "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".py", "wb") as file_writer:
                file_writer.write(data.content)

        if py == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".py", "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".sh", "wb") as file_writer:
                file_writer.write(data.content)

        if sh == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".sh", "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".txt", "wb") as file_writer:
                file_writer.write(data.content)

        if txt == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".txt", "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == True:
            count += 1

            data_file = str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".xml", "wb") as file_writer:
                file_writer.write(data.content)

        if xml == True and y == False:
            count += 1

            data_file = secure + str(i)
            data = requests.get(data_file, verify = valid_certificate)

            with open("file " + str(count)  + ".xml", "wb") as file_writer:
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
