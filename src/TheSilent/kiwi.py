import ipaddress
import json
import os
import random
import re
import socket
import ssl
import threading
import time
from ftplib import FTP,FTP_TLS
from TheSilent.beluga import beluga
from TheSilent.clear import clear
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.puppy_requests import text

CYAN = "\033[1;36m"

def kiwi_juice(dns_host,delay,scripts):
    global hits
    success = False

    # check reverse dns
    try:
        time.sleep(delay)
        hits.append(f"reverse dns {dns_host}: {socket.gethostbyaddr(dns_host)}")
        success = True
    except:
        pass

    # check if host is up
    try:
        time.sleep(delay)
        my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_socket.settimeout(10)
        my_socket.connect((dns_host,80))
        my_socket.close()
        hits.append(f"found {dns_host}")
        success = True
    except ConnectionRefusedError:
        hits.append(f"found {dns_host}")
        success = True
    except TimeoutError:
        hits.append(f"found {dns_host}")
        success = True
    except:
        pass
        

    if success:
        # check ssl cert info
        try:
            time.sleep(delay)
            context = ssl.create_default_context()
            context.check_hostname = True
            ssl_socket = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=dns_host)
            ssl_socket.settimeout(10)
            ssl_socket.connect((dns_host,443))
            data = ssl_socket.getpeercert()
            ssl_socket.close()
            hits.append(f"ssl cert info {dns_host}: {json.dumps(data,sort_keys=True,indent=4)}")
        except:
            pass
        try:
            time.sleep(delay)
            context = ssl.create_default_context()
            context.check_hostname = True
            ssl_socket = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=dns_host)
            ssl_socket.settimeout(10)
            ssl_socket.connect((dns_host,8443))
            data = ssl_socket.getpeercert()
            ssl_socket.close()
            hits.append(f"ssl cert info {dns_host}: {json.dumps(data,sort_keys=True,indent=4)}")
        except:
            pass

        if scripts == "all":
            # check for emails
            links = kitten_crawler(f"http://{dns_host}",delay,1000,False)
            for link in links:
                time.sleep(delay)
                try:
                    my_request = text(link)
                    results = re.findall("[a-zA-Z0-9\_\.]{3,}@[a-zA-Z0-9\_\.]{3,}\.[a-zA-Z0-9\_\.]+",my_request)
                    for result in results:
                        domain = ".".join(dns_host.split(".")[-2:])
                        if domain in result:
                            hits.append(result)
                except:
                    pass
            
            # check for anonymous ftp binds
            try:
                time.sleep(delay)
                ftp = FTP(dns_host,timeout=10)
                ftp.login()
                hits.append(f"anonymous ftp bind allowed on: {dns_host}")
            except:
                pass
            try:
                time.sleep(delay)
                ftps = FTP_TLS(dns_host,timeout=10)
                ftps.login()
                hits.append(f"anonymous ftp over tls bind allowed on: {dns_host}")
            except:
                pass

            # run beluga web vulnerability scanner
            time.sleep(delay)
            results = beluga(f"http://{dns_host}",delay,1000,False)
            for result in results:
                hits.append(f"{dns_host}- {result}")

        if scripts == "email":
            # check for emails
            links = kitten_crawler(f"http://{dns_host}",delay,1000,False)
            for link in links:
                time.sleep(delay)
                try:
                    my_request = text(link)
                    results = re.findall("[a-zA-Z0-9\_\.]{3,}@[a-zA-Z0-9\_\.]{3,}\.[a-zA-Z0-9\_\.]+",my_request)
                    for result in results:
                        domain = ".".join(dns_host.split(".")[-2:])
                        if domain in result:
                            hits.append(result)
                except:
                    pass

        if scripts == "ftp":
            # check for anonymous ftp binds
            try:
                time.sleep(delay)
                ftp = FTP(dns_host,timeout=10)
                ftp.login()
                hits.append(f"anonymous ftp bind allowed on: {dns_host}")
            except:
                pass
            try:
                time.sleep(delay)
                ftps = FTP_TLS(dns_host,timeout=10)
                ftps.login()
                hits.append(f"anonymous ftp over tls bind allowed on: {dns_host}")
            except:
                pass

        if scripts == "vuln":
            # run beluga web vulnerability scanner
            time.sleep(delay)
            results = beluga(f"http://{dns_host}",delay,1000,False)
            for result in results:
                hits.append(f"{dns_host}- {result}")

def kiwi(host,delay=0,scripts=None,cores=1):
    global hits
    clear()
    init_host = host
    hits = []
    if re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$",host):
        hosts = []
        for _ in ipaddress.ip_network(host,strict=False):
            hosts.append(str(_))
        hosts = random.sample(hosts,len(hosts))

    else:
        hosts = [host]

    if re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",host):
        subnet = True

    else:
        subnet = False
    
    subdomains = ["","aams","accent","accounts","acs-xs","acsamid01","acsids","acsnas","activeapplicant","activeresources","ad","adams","adfs","adm","admin","aes","aesdvr1","agenda","aggies","agsd520","ahs","ain-fortigate","airwatch","akhistory","akp-fortigate","akpk","alex2","alio","aliointel","alioportal","alltube","alpine","alt","alumni","ambler","ams","anc-fortigate","anc-opn","anchserv","angel","aovpn","apache","api","aplus","apple","appleid","apply","apps","apps2","apps3","aps","arabamid","arboretum","arc","archiver","asas","asburyhigh","asg","assessment","assets","atq-fortigate","atrium","atriuum","attalla","auth","auth1","auth2","autodiscover","av","aw","backup","barracuda","barracuda1","bbb","bbbsd-iv-1","bbcesmoodle","bbchsmoodle","bcbeiboss2","bcboefilewave","bcrobotics","bcsipmonitor","bear","believeyoucan","bensonsd","bes","bess-proxy","bet-vm-moodle4","beverlye","bibbcompass","bibbdestiny","bibbdocumentserver","bigbluebutton","bigboy","blackboard","block","blocker","blog","blogs","bm","bmon","bms-audioe","boe-emailsrv","books","bridgit","brindleemiddle","brindleemountainhigh","brw-ava-cctv-1","brw-fortigate","brw-opn","bsd-ps8","bsd-spam","bsl","buckhornhigh","busshop","butlerco","calendar","canvas","carver","casarry","casper","cassidy","catalog","causeyband","cbfw","ccctc","cchs","ccs","ccsd","ccssotraining","certifiedportal","cesmoodle","chinleusd","choice","chsmoodle","ciscoasa","citrix","cl","classlink","classweb","claysville","claysvillejuniorhigh","clearpass1","cloverdale","cms","cmsmoodle","cnp","cobalt","cochise","collab-edge","communityeducation","compass","compasslearning","conecuh","connect","connectdev","coronado","counseling","cov","covid19","cpanel","cpcalendars","cpcontacts","cpi","cppm1","cs-voip","csg","ctcsec","cusdextdns01","cusdextdns02","cusdntuamx1","cyberbase","cybernew","d2l","daleville","dare","darelementary","darhigh","darmiddle","dart","dartdemo","dartdemo2","dataservice","datavault","datsrv055","dcsamid01","dcsfws","dcsnamidcl","dcsxserve","ddi","decisioned","dell-learn","denali","des","designthefuture","desigo","destination","destiny","dev","dialin","dio","diocam","discovervideo","dlg","dlgconferences","dmm","dmsftp","dn","dns","dns1","dns2","docefill","docs","documentservices","domain","donat","donat2","donehoo","dothan","dothanhigh","dothantech","douglaselementary","douglashigh","douglasmiddle","dreamjob411","dsviewer","e2010","ebes","ebooks","eclass","eclass2","ecsinow","ecspowerschool","edulog","edutrax","edynamic","ees","eforms","eli","email","employeeportal","employees","engage","engage2","engagepd","enrollment","ens","eonline","es","eschool","eschoolhac","esmoodle","esms","ess","et","etcentral","etcontent","etsecurity","etsts","eurabrown","evans","excert","exchange","exchange-edge","expressway","faine","fairbanks-allworx","fairview","falcon1","familylink","fce","fea","fed","fes","filemaker","filewave","filter","finance","floyd","flp","fmpcal","follett","formcentral","forms","fortigate","fortis","four-peaks-elem","four-peaks-elem-2","frame","franklin","fs","ftp","fw","gadsdencity-hs","gam","gces","gchs","geo","gila","girard","girardms","gje","glennallenhonorsocieties","glv","gmail","gms","go","gpa","grades","grandview","greene","groups","grpwise","guac","guac-test","gw","gwguard","happytimes","hcs-ess","hct","hd","hdcsmtp1","hdctab","heard","hekla","help","helpdesk","henryclay","henryconnects","heritagehigh","hes","hhs","highlands","hms","home","homewood","honeysuckle","hs","hydaburg","iboss","ibossoc","ibossreporter","icl","icreports","idb","imail","info","infocus","infonowweb","inow","inowapi","inowhome","inowreports","inowtest","interventions","interweb","intranet","inventory","iparent","it","ivisions","jasper","jds","jds-ext","jhs","join","jrotc1","jsj-cam","jss","jupiter","k9spud","kak-fortigate","kb","kbox","kc","keklms","kellysprings","keynet","kgk","kgklms","kibsdenrollment","kibsdzendto","kka","kobuk","kronmobile","kronos","kts","lcs-amid01","ldap","lee","legacy","les","lesmoodle","lessonplans","lhs","lhsmoodle","lib","library","lightspeed","lightspeed2","links","listsrv","lms","lunch","maconexch","macpro","madisoncity","mahara","mail","mail1","mail2","mail4","mail7","mailserver","maintenance","maps","marengo","mars","math","matterhorn","mbsasa","mc","mcep","mcnary","mconline","mcpsnet","mcs-tools","mcsportal","mdm","mdm2","mealapp","mealapplication","mealapps","media","meet","meetme","mes","mesmoodle","mhsmoodle","micollab","midfield","mine","mitchell","mmsmoodle","mobile","mobilefilter","monroe","montage","montagebeta","montana","moodle","moodle17","moodle2","mps","mps-filewave","mps-powerschool","mps-rdp-01","mps-solarwinds","ms","msc-mobile","msc-print","msc7","mscs","mserve","mta","mta-sts","mts","mx","mx1","mx2","my","mydocs","myfiles","mypay","mystop","mytime","n2h2","naco","nactec","nagios","nas","nes","netview","newmail","nextcloud","nextgen","ng","ngweb","nms","noatak","northview","ns","ns1","ns2","ns3","nui-fortigate","nutrition","oaes","ocsad3","ocsarchive","ocsbo","ocscomm","ocsgwava","ocshelpdesk","ocslms","ocsmail","ocsweb","ocswww","odyssey","office","oldmail","oldregistration","onesync","onlinemealapp","opelika-ls","owa","packetview","pages","palmer","palominas","pandora","paperless","parent","parentportal","parentsurvey","passwordreset","passwordresetregistration","patriotpath","payday","paydocs","payroll","paystubs","pbx","pcmon","pcslibrary","pd","pdexpress","pdmoodle","pho-fortigate","piedmont","pinpoint","piz-fortigate","pl","pm","podcasts","polycom","pop","portal","powerschool","pres","preschool","proxy","proxy2","ps","ps-sandbox","ps-test","pssb","pstest","publicaccess","pulse","pwchange","quarantine","radius","randolph","rbhudson","rcs","rdp","rds","read","readydesk","records","registration","relay","relay1","relay2","remotesupport","renlearn","renplace","reporter","reportmax","request","res","reset","reveal","rise","roatws1","rock","rocket","rollcall","router","rp","rpad","rsapi","rta-app-a","rta-app-b","rvchs","s","safari","safariaves","sav4","sav5","sav6","school","schoolboard","schoolmax","schools","scim","score","scripting","scs","scsinfnow","scsmail","scsnxgnsvc","sdp","search","searchsoft","searchsoftauth","secure","securelink","security","securityportal","sedna","selawik","selmast","services","ses","sesmoodle","sets","setshome","setsser","setsti","setsweb","sftp","sftp2","sfw","shelbyed","shh","showcase","shssec","shungnak","sif","silverthrone","sis","siteproxy","sites","sjhs","skk","slingluff","slomanprimary","smk","sms","smtp","smtp-1","smtp1","smtp11","smtp2","sonicwallva","sophos","spam","spam2","spamtitan1","spamtitan2","spc","specialty","speedtest","sports","sresmoodle","sso","sspr","ssrpm","staff","staffportal","staffsurvey","status","sti","stidistrict","stisets","stisetsweb","striplin","sts","studentportal","studentvue","subfinder","subportal","sumter","support","supportportal","sva","swinstall","synergy","synergypsv","synergyweb","synldap","sysaid","szmcg","talk","tarrant","tbcparent","tcchsmoodle","tcm","tcs-docs","tcsd-ns-01","tcsd-ns-02","tcsdns","tcsfirewall","tcsscobia","teacherportal","teaching","technology","techweb","techwiki","temp","temptrak","tes","test","test5","testps","thompson","ths","tickets","timeclock","tla","tm","tools","trans","transelog","transportation","trend","triptracker","tserver","ttc-smb","ttc-spam","turn","tuscumbia","twa","tyler","tylerweb","ubnt","uc-exe","uc-exe-2","ugms","uisp","unifi","uniongrove","unk","updates","utm","view","view1","view2","visions","voip-expressway-e","vpec01","vpn","vpn-brw","waa","walnutpark","wanutil","wayfinder","wb","wbb","wboesfb","web","web2","webapps","webcentral","webcrd","webdisk","webmail","webmail2","websets","wes","wesmoodle","wessec","whsmoodle","wiki","wilcox","williamblount","windows-vs","winfield","workorder","workorders","wpes","www","www1","www2","wx","zendto"]
    
    kiwi_thread_list = []
    thread_count = 0
    for host in hosts:
        if subnet:
            subdomains = [""]
        else:
            subdomains = random.sample(subdomains,len(subdomains))
        for _ in subdomains:
            if _ == "":
                dns_host = host
            else:
                dns_host = f"{_}.{host}"

            print(CYAN + dns_host)
            kiwi_thread = threading.Thread(target=kiwi_juice,args=(dns_host,delay,scripts,))
            kiwi_thread_list.append(kiwi_thread)
            kiwi_thread.start()
            thread_count += 1
            if thread_count % cores == 0:
                for my_thread in kiwi_thread_list:
                    my_thread.join()
                kiwi_thread_list = []

    for my_thread in kiwi_thread_list:
        my_thread.join()

    clear()
    hits = list(set(hits[:]))
    hits.sort()
    with open(f"{init_host.replace('/','[]')}.txt","a") as file:
        for hit in hits:
            file.write(f"{hit}\n")

    clear()
    print(CYAN + f"{len(hits)} results written to {init_host.replace('/','[]')}.txt")
