import socket
from TheSilent.clear import clear

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def kiwi(host):
    clear()
    total = 0
    
    mal_subdomains = ["ab-dns-cach1","ab-dns-cach2","accord-100","acs","adc","adc-03","adfs","alertus","autodiscover","bananajr6000","barracuda","bele","cameras","cereg","citrixweb","cloudpath","cms","cv-teams","datatel","demo100","demo200","destiny","dmm","eduphoria","enteliweb","esphac","espsms","ex-san-and-switches-3","ezproxy","ffepurchasing","fod200","forms","ftp2","ftp201","gateway","gluu","google-proxy-66-249-80-0","google-proxy-74-125-211-0","gtm100","gtm200","hac","help","helpdesk","helpme","hip","idautoarms","iddesign","idp","ipac","ironport","its10","its20","jpextfs","library","mail","mcc-mpx1","mcc-ucxn1","mccmail","mccsim","midfp-eac1","misdfsc","mlink","mobile","mx","mx-in-hfd","mx-in-mdn","mx-in-rno","mx-in-vib","mylocker","ns01","ns1","ns2","ns3","ns4","ns45","ns46","ns75","ns76","pdns11","pdns12","pnn","prime","rate-limited-proxy-108-177-71-0","rate-limited-proxy-74-125-151-0","relayp","schoology","secureforms","selfservice","sharepoint","smtp","smtp2","speedtest","sso","staffldap","support","tac","uisp","vault","vpn","vpn-211-120","vpn-211-20","vpn2","web","webadvisor","webadvisortest","webtest","winapi","winapitest","ww3"]

    for mal in mal_subdomains:
        if host.count(".") > 1:
            try:
                data = socket.gethostbyname_ex(mal + "." + ".".join(host.split(".")[1:]))
                print(CYAN + f"found: {data}")
                total += 1

            except:
                pass

        try:
            data = socket.gethostbyname_ex(mal + "." + host)
            print(CYAN + f"found: {data}")
            total += 1

        except:
            pass

    print(GREEN + f"found: {total} out of {2 * len(mal_subdomains)} possible")
