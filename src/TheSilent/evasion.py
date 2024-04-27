import random
import string
import urllib.parse

def append_random_string(mal):
    length = random.randint(35, 101)
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    
    return [mal + random_string]

def directory_self_reference(mal):
    gather = []

    gather.append(f"./{mal}")
    gather.append(f"../{mal}")
    gather.append(f"././{mal}")
    gather.append(f"../../{mal}")
    gather.append(f"./././{mal}")
    gather.append(f"../../../{mal}")

    return gather

def percent_encoding(mal):
    gather = []

    gather.append(urllib.parse.quote(mal))
    gather.append(urllib.parse.quote(urllib.parse.quote(mal)))
    gather.append(urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(mal))))

    gather = list(set(gather[:]))
    return gather

def prepend_random_string(mal):
    length = random.randint(35, 101)
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    
    return [random_string + mal]

def random_case(mal):
    my_random = ""
    for char in mal:
        if random.choice([True, False]):
            my_random += char.upper()
        else:
            my_random += char.lower()
    
    return [my_random]

def utf8_encoding(mal):
    gather = []
    gather.append("".join([f"&#{ord(char)};" for char in mal]))
    gather.append("".join([f"\\x{ord(char)}" for char in mal]))

    return gather
