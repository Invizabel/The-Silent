import os

os.system("apt update")
os.system("apt upgrade")
os.system("apt install termux-services")
os.system("apt install tor")
os.system("apt install libjpeg-turbo")

os.system("pip3 install wheel")

#twint modules
os.system("pip3 install aiohttp==3.7.0")
os.system("pip3 install aiohttp_socks")
os.system("pip3 install bs4")
os.system("pip3 install -r twint.txt")

os.system("pip3 install requests")
os.system("pip3 install pysocks")
os.system("pip3 install BeautifulSoup")

os.system("pip3 install matplotlib")
os.system("pip3 install pandas")
os.system("pip3 install imagehash")

os.system("pip3 install pillow")
