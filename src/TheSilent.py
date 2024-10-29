import argparse
import json
import ssl
import socket
from clear import clear

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

def TheSilent():
    clear()
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", required = True, type = str, help = "host to scan | string")
    parser.add_argument("-filename", required = False, type = str, help = "file to output | string")
    args = parser.parse_args()

    context = ssl.create_default_context()
    count = -1
    hits = {}
    hosts = [args.host]
    
    while True:
        count += 1
        try:
            json_data = []
            hosts = list(dict.fromkeys(hosts[:]))
            print(f"{CYAN}checking: {GREEN}{hosts[count]}")

            # fqdn
            fqdn = socket.getfqdn(hosts[count])
            json_data.append(fqdn)

            # dns
            dns = socket.gethostbyname_ex(hosts[count])
            json_data.append(dns[0])
            for i in dns[1]:
                json_data.append(i)
            for i in dns[2]:
                json_data.append(i)

            # reverse dns
            reverse_dns = socket.gethostbyaddr(hosts[count])
            json_data.append(reverse_dns[0])
            for i in reverse_dns[1]:
                json_data.append(i)
            for i in reverse_dns[2]:
                json_data.append(i)

        except IndexError:
            break

        except:
            pass

        try:
            # ssl cert dns
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(10)
            tcp_socket.connect((hosts[count], 443))
            ssl_socket = context.wrap_socket(tcp_socket, server_hostname = hosts[count])
            cert = ssl_socket.getpeercert()
            tcp_socket.close()
            for dns_cert in cert["subject"]:
                if "commonName" in dns_cert[0]:
                    json_data.append(dns_cert[1].replace("*.", ""))

        except:
            pass

        try:
            # ssl cert dns
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(10)
            tcp_socket.connect((hosts[count], 443))
            ssl_socket = context.wrap_socket(tcp_socket, server_hostname = hosts[count])
            cert = ssl_socket.getpeercert()
            tcp_socket.close()    
            for dns_cert in cert["subjectAltName"]:
                if "DNS" in dns_cert[0]:
                    json_data.append(dns_cert[1].replace("*.", ""))

        except:
            pass
        
        json_data = list(dict.fromkeys(json_data[:]))
        json_data.sort()
        for i in json_data:
            hosts.append(i)

        results = {}
        results.update({"RELATIONSHIPS": json_data})
        hits.update({hosts[count]: results})
        
        
    clear()

    hits = json.dumps(hits, indent = 4, sort_keys = True)

    if args.filename:
        with open(f"{args.filename}.json", "w") as json_file:
            json_file.write(hits)

        with open(f"{args.filename}.txt", "w") as text_file:
            for line in json.loads(hits).keys():
                text_file.write(f"{line}\n")

    print(f"{RED}{hits}")

if __name__ == "__main__":
    TheSilent()
