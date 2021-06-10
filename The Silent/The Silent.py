#Documentation:
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
#https://www.w3schools.com/PYTHON/ref_requests_get.asp
#https://www.geeksforgeeks.org/python-check-url-string/
#https://www.w3schools.com/python/gloss_python_check_string.asp

import os
import random
import re
import requests
import time

def find_url(string):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)
	return [x[0] for x in url]

def the_silent():
	os.system("clear")

	print("1 = data no log\n2 = data log\n3 = file\n4 = password generator\n5 = brute force (dictionary)")
	user_input = input()

	if user_input == "1":
		no_log()

	if user_input == "2":
		log()

	if user_input == "3":
		os.system("clear")

		print("1 = image | 2 = pdf | 3 = html | 4 = all images | 5 = all data")
		user_file = input()

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
		
def no_log():
	os.system("clear")
	
	print("Secure? y/n")
	secure_input = input()
	
	os.system("clear")

	print("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url")
	user_input = input()
	
	if user_input == "1" and secure_input == "y":
		no_log_cookies_secure()
		
	if user_input == "1" and secure_input == "n":
		no_log_cookies_not_secure()
		
	if user_input == "2" and secure_input == "y":
		no_log_encoding_secure()
		
	if user_input == "2" and secure_input == "n":
		no_log_encoding_not_secure()
		
	if user_input == "3" and secure_input == "y":
		no_log_headers_secure()
		
	if user_input == "3" and secure_input == "n":
		no_log_headers_not_secure()
		
	if user_input == "4" and secure_input == "y":
		no_log_html_code_secure()
		
	if user_input == "4" and secure_input == "n":
		no_log_html_code_not_secure()
		
	if user_input == "5" and secure_input == "y":
		no_log_ok_secure()
		
	if user_input == "5" and secure_input == "n":
		no_log_ok_not_secure()
		
	if user_input == "6" and secure_input == "y":
		no_log_permanent_redirect_secure()
		
	if user_input == "6" and secure_input == "n":
		no_log_permanent_redirect_not_secure()
		
	if user_input == "7" and secure_input == "y":
		no_log_reason_secure()
		
	if user_input == "7" and secure_input == "n":
		no_log_reason_not_secure()
		
	if user_input == "8" and secure_input == "y":
		no_log_redirect_secure()
		
	if user_input == "8" and secure_input == "n":
		no_log_redirect_not_secure()
		
	if user_input == "9" and secure_input == "y":
		no_log_status_code_secure()
		
	if user_input == "9" and secure_input == "n":
		no_log_status_code_not_secure()
		
	if user_input == "10" and secure_input == "y":
		no_log_url_secure()
		
	if user_input == "10" and secure_input == "n":
		no_log_url_not_secure()
	
def no_log_cookies_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Cookies: " + str(final.cookies))

	final.close()

	pause = input()

	the_silent()

def no_log_cookies_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Cookies: " + str(final.cookies))

	final.close()

	pause = input()

	the_silent()

def no_log_encoding_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Encoding: " + str(final.encoding))

	final.close()

	pause = input()

	the_silent()

def no_log_encoding_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Encoding: " + str(final.encoding))

	final.close()

	pause = input()

	the_silent()

def no_log_headers_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Headers: " + str(final.headers))

	final.close()

	pause = input()

	the_silent()

def no_log_headers_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Headers: " + str(final.headers))

	final.close()

	pause = input()

	the_silent()

def no_log_html_code_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("HTML code: " + str(final.text))

	final.close()

	pause = input()

	the_silent()

def no_log_html_code_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("HTML code: " + str(final.text))

	final.close()

	pause = input()

	the_silent()

def no_log_ok_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Ok: " + str(final.ok))

	final.close()

	pause = input()

	the_silent()

def no_log_ok_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Ok: " + str(final.ok))

	final.close()

	pause = input()

	the_silent()

def no_log_permanent_redirect_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Permanent redirect: " + str(final.is_permanent_redirect))

	final.close()

	pause = input()

	the_silent()

def no_log_permanent_redirect_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Permanent redirect: " + str(final.is_permanent_redirect))

	final.close()

	pause = input()

	the_silent()

def no_log_reason_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Reason: " + str(final.reason))

	final.close()

	pause = input()

	the_silent()

def no_log_reason_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Reason: " + str(final.reason))

	final.close()

	pause = input()

	the_silent()
	
def no_log_redirect_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Redirect: " + str(final.is_redirect))

	final.close()

	pause = input()

	the_silent()

def no_log_redirect_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Redirect: " + str(final.is_redirect))

	final.close()

	pause = input()

	the_silent()

def no_log_status_code_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Status code: " + str(final.status_code))

	final.close()

	pause = input()

	the_silent()

def no_log_status_code_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Status code: " + str(final.status_code))

	final.close()

	pause = input()

	the_silent()

def no_log_url_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("URL: " + str(final.url))

	final.close()

	pause = input()

	the_silent()

def no_log_url_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("URL: " + str(final.url))

	final.close()

	pause = input()

	the_silent()

def log():
	os.system("clear")
	
	print("Secure? y/n")
	secure_input = input()
	
	os.system("clear")

	print("1 = cookies\n2 = encoding\n3 = headers\n4 = html code\n5 = ok\n6 = permanent redirect\n7 = reason\n8 = redirect\n9 = status code\n10 = url")
	user_input = input()

	if user_input == "1" and secure_input == "y":
		log_cookies_secure()
		
	if user_input == "1" and secure_input == "n":
		log_cookies_not_secure()
		
	if user_input == "2" and secure_input == "y":
		log_encoding_secure()
		
	if user_input == "2" and secure_input == "n":
		log_encoding_not_secure()
		
	if user_input == "3" and secure_input == "y":
		log_headers_secure()
		
	if user_input == "3" and secure_input == "n":
		log_headers_not_secure()
		
	if user_input == "4" and secure_input == "y":
		log_html_code_secure()
		
	if user_input == "4" and secure_input == "n":
		log_html_code_not_secure()
		
	if user_input == "5" and secure_input == "y":
		log_ok_secure()
		
	if user_input == "5" and secure_input == "n":
		log_ok_not_secure()
		
	if user_input == "6" and secure_input == "y":
		log_permanent_redirect_secure()
		
	if user_input == "6" and secure_input == "n":
		log_permanent_redirect_not_secure()
		
	if user_input == "7" and secure_input == "y":
		log_reason_secure()
		
	if user_input == "7" and secure_input == "n":
		log_reason_not_secure()
		
	if user_input == "8" and secure_input == "y":
		log_redirect_secure()
		
	if user_input == "8" and secure_input == "n":
		log_redirect_not_secure()
		
	if user_input == "9" and secure_input == "y":
		log_status_code_secure()
		
	if user_input == "9" and secure_input == "n":
		log_status_code_not_secure()
		
	if user_input == "10" and secure_input == "y":
		log_url_secure()
		
	if user_input == "10" and secure_input == "n":
		log_url_not_secure()

def log_cookies_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Cookies: " + str(final.cookies))
	file.write("\n\nCookies: " + str(final.cookies))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_cookies_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Cookies: " + str(final.cookies))
	file.write("\n\nCookies: " + str(final.cookies))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_encoding_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Encoding: " + str(final.encoding))
	file.write("\n\nEncoding: " + str(final.encoding))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_encoding_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Encoding: " + str(final.encoding))
	file.write("\n\nEncoding: " + str(final.encoding))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_headers_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Headers: " + str(final.headers))
	file.write("\n\nHeaders: " + str(final.headers))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_headers_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Headers: " + str(final.headers))
	file.write("\n\nHeaders: " + str(final.headers))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_html_code_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("HTML code: " + str(final.text))
	file.write("\n\nHTML code: " + str(final.text))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_html_code_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("HTML code: " + str(final.text))
	file.write("\n\nHTML code: " + str(final.text))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_ok_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Ok: " + str(final.ok))
	file.write("\n\nOk: " + str(final.ok))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_ok_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Ok: " + str(final.ok))
	file.write("\n\nOk: " + str(final.ok))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_permanent_redirect_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Permanent redirect: " + str(final.is_permanent_redirect))
	file.write("\n\nPermanent redirect: " + str(final.is_permanent_redirect))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_permanent_redirect_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Permanent redirect: " + str(final.is_permanent_redirect))
	file.write("\n\nPermanent redirect: " + str(final.is_permanent_redirect))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_reason_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Reason: " + str(final.reason))
	file.write("\n\nReason: " + str(final.reason))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_reason_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Reason: " + str(final.reason))
	file.write("\n\nReason: " + str(final.reason))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_redirect_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Redirect: " + str(final.is_redirect))
	file.write("\n\nRedirect: " + str(final.is_redirect))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_redirect_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Redirect: " + str(final.is_redirect))
	file.write("\n\nRedirect: " + str(final.is_redirect))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_status_code_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("Status code: " + str(final.status_code))
	file.write("\n\nStatus code: " + str(final.status_code))

	final.close()
	file.close

	pause = input()

	the_silent()

def log_status_code_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)

	print("")
	print("Status code: " + str(final.status_code))
	file.write("\n\nStatus code: " + str(final.status_code))

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_url_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "https://" + user_input
	
	final = requests.get(output, verify = True)

	print("")
	print("URL: " + str(final.url))
	file.write("\n\nURL: " + str(final.url) + "\n\n")

	final.close()
	file.close()

	pause = input()

	the_silent()

def log_url_not_secure():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	start = time.time()

	output = "http://" + user_input
	
	final = requests.get(output, verify = False)
	file.write("\n\nURL: " + str(final.url) + "\n\n")

	print("")
	print("URL: " + str(final.url))

	final.close()
	file.close()

	pause = input()

	the_silent()
	
def image():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nEnter desired name:")
	name = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	picture = str(output)

	data = requests.get(picture, verify = True)

	with open(name, "wb") as file_writer:
		file_writer.write(data.content)

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	data.close()

	the_silent()

def pdf():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nEnter desired name:")
	name = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	pdf = output

	data = requests.get(pdf, stream = True, verify = True)

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

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	final = requests.get(output, verify = True)

	file = open(user_input + ".html", "w+")
	file.write(final.text)

	final.close()
	file.close()

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	the_silent()

def all_images():
	count = 0
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	url = requests.get(output, verify = True)
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
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".jpeg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpeg == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".jpeg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpg == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".jpg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpg == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".jpg", "wb") as file_writer:
				file_writer.write(data.content)

		if png == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".png", "wb") as file_writer:
				file_writer.write(data.content)

		if png == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".png", "wb") as file_writer:
				file_writer.write(data.content)

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	url.close()

	the_silent()

def all_data():
	count = 0
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	url = requests.get(output, verify = True)
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
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".app", "wb") as file_writer:
				file_writer.write(data.content)

		if app == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".app", "wb") as file_writer:
				file_writer.write(data.content)

		if avi == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".avi", "wb") as file_writer:
				file_writer.write(data.content)

		if avi == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".avi", "wb") as file_writer:
				file_writer.write(data.content)

		if bat == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".bat", "wb") as file_writer:
				file_writer.write(data.content)

		if bat == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".bat", "wb") as file_writer:
				file_writer.write(data.content)

		if cmd == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".cmd", "wb") as file_writer:
				file_writer.write(data.content)

		if cmd == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".cmd", "wb") as file_writer:
				file_writer.write(data.content)

		if css == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".css", "wb") as file_writer:
				file_writer.write(data.content)

		if css == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".css", "wb") as file_writer:
				file_writer.write(data.content)

		if doc == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".doc", "wb") as file_writer:
				file_writer.write(data.content)

		if doc == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".doc", "wb") as file_writer:
				file_writer.write(data.content)

		if docx == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".docx", "wb") as file_writer:
				file_writer.write(data.content)

		if docx == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".docx", "wb") as file_writer:
				file_writer.write(data.content)

		if exe == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".exe", "wb") as file_writer:
				file_writer.write(data.content)

		if exe == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".exe", "wb") as file_writer:
				file_writer.write(data.content)

		if gif == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".gif", "wb") as file_writer:
				file_writer.write(data.content)

		if gif == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".gif", "wb") as file_writer:
				file_writer.write(data.content)

		if html == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".html", "wb") as file_writer:
				file_writer.write(data.content)

		if html == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".html", "wb") as file_writer:
				file_writer.write(data.content)

		if jar == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".jar", "wb") as file_writer:
				file_writer.write(data.content)

		if jar == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".jar", "wb") as file_writer:
				file_writer.write(data.content)

		if java == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".java", "wb") as file_writer:
				file_writer.write(data.content)

		if java == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".java", "wb") as file_writer:
				file_writer.write(data.content)

		if jpeg == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".jpeg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpeg == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".jpeg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpg == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".jpg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpg == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".jpg", "wb") as file_writer:
				file_writer.write(data.content)

		if jss == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".jss", "wb") as file_writer:
				file_writer.write(data.content)

		if jss == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".jss", "wb") as file_writer:
				file_writer.write(data.content)

		if m4a == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".m4a", "wb") as file_writer:
				file_writer.write(data.content)

		if m4a == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".m4a", "wb") as file_writer:
				file_writer.write(data.content)

		if mp3 == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".mp3", "wb") as file_writer:
				file_writer.write(data.content)

		if mp3 == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".mp3", "wb") as file_writer:
				file_writer.write(data.content)

		if mp4 == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".mp4", "wb") as file_writer:
				file_writer.write(data.content)

		if mp4 == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".mp4", "wb") as file_writer:
				file_writer.write(data.content)

		if pdf == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".pdf", "wb") as file_writer:
				file_writer.write(data.content)

		if pdf == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".pdf", "wb") as file_writer:
				file_writer.write(data.content)

		if png == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".png", "wb") as file_writer:
				file_writer.write(data.content)

		if png == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".png", "wb") as file_writer:
				file_writer.write(data.content)

		if py == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".py", "wb") as file_writer:
				file_writer.write(data.content)

		if py == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".py", "wb") as file_writer:
				file_writer.write(data.content)

		if sh == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".sh", "wb") as file_writer:
				file_writer.write(data.content)

		if sh == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".sh", "wb") as file_writer:
				file_writer.write(data.content)

		if txt == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".txt", "wb") as file_writer:
				file_writer.write(data.content)

		if txt == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".txt", "wb") as file_writer:
				file_writer.write(data.content)

		if xml == True and y == True:
			count += 1

			data_file = str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".xml", "wb") as file_writer:
				file_writer.write(data.content)

		if xml == True and y == False:
			count += 1

			data_file = secure + str(i)
			data = requests.get(data_file, verify = True)

			with open("file " + str(count)  + ".xml", "wb") as file_writer:
				file_writer.write(data.content)

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	url.close()

	the_silent()

def password_generator():
	os.system("clear")
	
	output = ""
	
	password_storage = [""]
	password_storage.clear()
	
	password_characters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
	
	print("What is the password length?")
	password_length = int(input())

	for i in range (0,password_length):
		rand = random.randint(0,len(password_characters) - 1)

		password_storage.append(password_characters[rand])

	for i in password_storage:
		output += i

	print("Password:",output)

	pause = input()

	the_silent()

def brute_force_dictionary():
	count = 0

	os.system("clear")
	
	print("Enter name of list:")
	user_input = input()

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
			print("The password is: "+ check)
			text_file.close()
			exit()

		if str(tracker[count]) != check and count != len(tracker):
			count += 1

	the_silent()
			
the_silent()
