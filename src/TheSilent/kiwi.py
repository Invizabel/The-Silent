import socket
from TheSilent.clear import clear

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def kiwi(host):
    clear()
    total = 0
    
    mal_subdomains = ["220-s1","ab-dns-cach1","ab-dns-cach2","accord-100","acs","adc","adc-03","adfs","afl","airwatch","alertus","alioweb","articles","atriuum","attachments","autodiscover","avl","bananajr6000","barracuda","bd","bele","bisd-vcse","bpemp","bullyreport","cameras","catalog","cereg","cip","citrixweb","ckf01","ckf02","ckf03","ckf04","ckm","ckm01","ckr01","cloudpath","cms","compass","compasslearning","contacts","content","cpmt","cv-teams","datatel","demo100","demo200","destiny","dev-sync-use","dls","dmm","dns1","dns101","dns102","dns2","dns4","duckduckbot-1","duckduckbot-2","duckduckbot-4","duckduckbot-5","duckduckbot-6","duckduckbot-7","duckduckbot-8","duckduckbot-9","ecisd-ns1","edu","eduphoria","efpeac-2021","elearn","email","emaildev","employeeinfo","enrollment","enteliweb","esb00","eschoolhac","eschoolplus","esp","esphac","espsms","eun-dng1","everyday","ex-san-and-switches-3","ex1","ex2","exchange","exchsrvr","expe","external-content","ezproxy","ffepurchasing","filter","finance","fod200","forms","ftp","ftp2","ftp201","gateway","gcs","gluu","google-proxy-66-249-80-0","google-proxy-74-125-211-0","gp","graduation","gs","gtm100","gtm200","hac","harhac","help","helpdesk","helpme","hip","home","hr","iboss","idauto-portal","idautoarms","iddesign","idp","idp00","iepplusnlb","iepptest","ipac","iron","ironport","itech","its10","its20","jobs","jpextfs","kltn","kronos","library","links","liquidoffice","ljisd","lp","mail","mailer","mailstream-central","mailstream-east","mailstream-eu1","mailstream-west","mcc-mpx1","mcc-ucxn1","mccmail","mccsim","mdm","meniola","midfp-eac1","miles","misdfsc","mlink","mobile","mobilelearning","moodle","msonlineppe2010","mx","mx-in-hfd","mx-in-mdn","mx-in-rno","mx-in-vib","my","mydispense","myinfo","mylocker","ns01","ns02","ns03","ns04","ns1","ns1-39","ns1vwx","ns2","ns2-39","ns27","ns28","ns2lns","ns3","ns3-39","ns3cfp","ns4","ns4-39","ns45","ns46","ns47","ns48","ns49","ns4gvx","ns5","ns50","ns53","ns54","ns69","ns70","ns75","ns76","odyssey2","old","open1","open2","pac","paspsites2010","pdns11","pdns12","pnn","portal","ppepaspsites2010","prime","prtg","purchasing","r3000","rate-limited-proxy-108-177-71-0","rate-limited-proxy-74-125-151-0","rdns1","rdns2","register","relayp","remote","reporter","reset","riverdeep","routing","s1","safe","schoology","secureforms","selfservice","sems","sharepoint","skysrv","skystu","skyward","skyweb","smtp","smtp00","smtp2","smtpmailer1","sped","speedtest","spqr","srironport","sso","staffldap","steam","subscriptions-dev","support","sync","tac","tc-prtg","tcp","tcptraining","tide500","timeclockplus","uisp","usb-smtp-inbound-1","usb-smtp-inbound-2","use-dng1","ussf56","ussf57","vault","vendorftp","versatrans","vm-stxdc","vpn","vpn-211-120","vpn-211-20","vpn2","warehouse","web","webadvisor","webadvisortest","webcast","webmail","webtest","whm","winapi","winapitest","ww3","www-dev00"]
        
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

    try:
        data = socket.gethostbyname_ex(host)
        print(CYAN + f"found: {data}")
        total += 1

    except:
        pass

    print(GREEN + f"found: {total} out of {2 * len(mal_subdomains) + 1} possible")
