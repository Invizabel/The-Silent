import hashlib
import os
import re
import time
import urllib.parse
from itertools import *
from TheSilent.clear import clear
import TheSilent.kitten_crawler as kitten
import TheSilent.puppy_requests as puppy

CYAN = "\033[1;36m"

def panda(init_hash=None,brute=None,create=None,delay=0,dictionary=None,mask=None):
    print(CYAN + "")
    clear()
    words = []
    if brute != None:
        for _ in range(1,36):
            words = product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()",repeat=_)
            print(CYAN + f"attempting to crack {init_hash} with brute force using length {_}")
            for word in words:
                new_word = "".join(word)
                if hashlib.md5(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha1(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha224(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha256(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha384(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha512(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha3_224(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha3_256(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha3_384(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha3_512(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

    if create != None:
        create = create.rstrip("/")
        word_list = []
        hosts = kitten.kitten_crawler(create,delay)
        for host in hosts:
            print(f"checking {host}")
            time.sleep(delay)
            try:
                data = puppy.text(host)
            except:
                continue
            words = re.findall("\w{4,}",data)
            for word in words:
                word_list = list(set(word_list[:]))
                word_list.append(word)
        word_list = list(set(word_list[:]))
        word_list.sort()
        with open(urllib.parse.urlparse(create).netloc + ".txt","a") as file:
            for word in word_list:
                file.write(f"{word}\n")
        clear()
        return f"found {len(word_list)} unique words"

    if dictionary != None:
        print(CYAN + f"attempting to crack {init_hash} with dictionary")
        if os.path.isfile(dictionary):
            with open(dictionary,"r") as f:
                for _ in f:
                    words.append(_.replace("\n",""))

        if not os.path.isfile(dictionary):
            files = os.listdir(dictionary)
            for ff in files:
                with open(dictionary + "/" + ff,"rb") as f:
                    for _ in f:
                        words.append(_.decode(errors="ignore").replace("\n",""))

        for word in words:
            if hashlib.md5(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha1(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha224(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha256(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha384(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha512(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha3_224(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha3_256(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha3_384(word.encode()).hexdigest() == init_hash:
                return word

            if hashlib.sha3_512(word.encode()).hexdigest() == init_hash:
                return word

    if mask != None:
        for _ in range(1,36):
            words = product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()",repeat=_)
            print(CYAN + f"attempting to crack {init_hash} with mask using length {_}")
            for word in words:
                new_word = "".join(word)
                new_word = mask + new_word
                if hashlib.md5(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha1(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha224(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha256(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha384(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha512(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha3_224(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha3_256(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha3_384(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word

                if hashlib.sha3_512(new_word.encode()).hexdigest() == init_hash:
                    clear()
                    return new_word
