import socket
from TheSilent.clear import clear

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def kiwi(host):
    clear()
    total = 0
    
    mal_subdomains = ["ab-dns-cach1",
                      "ab-dns-cach2",
                      "accord-100",
                      "acs",
                      "ad",
                      "adc",
                      "adc-03",
                      "adfs",
                      "adns"
                      "admin",
                      "aer-6024",
                      "aitp",
                      "alertus",
                      "alumni",
                      "ansb-ctrl01",
                      "ansb-ctrl02",
                      "ansb-eda02",
                      "apm",
                      "appshare",
                      "autodiscover",
                      "axisweb1",
                      "backup",
                      "barracuda",
                      "baylor",
                      "bele",
                      "bk-dns-cach1",
                      "bk-dns-cach2",
                      "blog",
                      "br-dns-cach1",
                      "br-dns-cach2",
                      "bv",
                      "bv-control",
                      "cab-air",
                      "cab-air",
                      "camera",
                      "cameras",
                      "cctv",
                      "ccx01",
                      "ccx02",
                      "cdn",
                      "cereg",
                      "cf-apps",
                      "cgvica",
                      "citrixweb",
                      "cl-ethosapi-prd",
                      "cl-ethosapi-tst",
                      "cl-msg-prod",
                      "cl-msg-test",
                      "cloudpath",
                      "cl-stss-prod",
                      "cl-stss-test",
                      "cl-ui-prod",
                      "cl-wa-prod",
                      "cl-wa-test",
                      "cms",
                      "cmt",
                      "cmtsm",
                      "cns",
                      "cns323",
                      "cnscopier",
                      "cnsoff2",
                      "cnsoffice",
                      "cnssql",
                      "cnsterm",
                      "col-prod",
                      "col-test",
                      "cors",
                      "cscluster",
                      "csnnt",
                      "cst",
                      "cstad",
                      "cstaix",
                      "cstnt",
                      "cstnt2",
                      "cten-6506",
                      "cuc02",
                      "cuseeme",
                      "cv-teams",
                      "cw2k",
                      "cxm",
                      "datatel",
                      "db",
                      "dc",
                      "ddt",
                      "de",
                      "demo",
                      "denodo-dev",
                      "denodo-prd",
                      "denodo-sm",
                      "denodo-stg",
                      "denodo-vcs",
                      "destiny",
                      "dev",
                      "distance",
                      "dl",
                      "dmm",
                      "dns",
                      "dns-cach2",
                      "ectn",
                      "eduphoria",
                      "eduuploader",
                      "emas3",
                      "enteliweb",
                      "enterprise",
                      "entuity-ha",
                      "entuity-wa",
                      "extranet",
                      "extricom",
                      "ezproxy",
                      "farmer",
                      "fb-dns-cach2",
                      "fc",
                      "fcis2",
                      "fcsync",
                      "fcsync2",
                      "fcws",
                      "firstclass",
                      "flightsim",
                      "fod-infobase-com",
                      "fog",
                      "forms",
                      "frontend-480",
                      "fs",
                      "ftp",
                      "ftp2",
                      "games",
                      "gatekeeper",
                      "gateway",
                      "gateway-mars",
                      "gateway-s1",
                      "geeks",
                      "gis",
                      "git",
                      "gitlab",
                      "glowpoint-2621",
                      "gluu",
                      "gms",
                      "goforit",
                      "gw",
                      "ha-ava",
                      "ha-ava-idrac",
                      "ha-ddom",
                      "hac",
                      "help",
                      "helpdesk",
                      "helpme",
                      "hip",
                      "horizon",
                      "idautoarms",
                      "idp",
                      "internal",
                      "intranet",
                      "ipac",
                      "ironport",
                      "kbox",
                      "ldap",
                      "local",
                      "login",
                      "lokai",
                      "mail",
                      "mail2",
                      "mail3",
                      "mccmail",
                      "mcc-mpx1",
                      "mccsim",
                      "mcc-ucxn1",
                      "midfp-eac1",
                      "misdfsc.midwayisd.org",
                      "mlink",
                      "mobile",
                      "mx",
                      "mylocker",
                      "ns01",
                      "ns1",
                      "ns2",
                      "ns3",
                      "okta-ad-adns1",
                      "okta-ad-adns2",
                      "okta-ad-adnstst",
                      "oldwww",
                      "pnn",
                      "portal",
                      "rdp",
                      "relayp",
                      "remote",
                      "rodc-01",
                      "secureforms",
                      "selfservice",
                      "sharepoint",
                      "smtp",
                      "smtp2",
                      "speedtest",
                      "sso",
                      "stdc-01",
                      "st-dc1",
                      "st-dc2",
                      "support",
                      "tac",
                      "test",
                      "uisp",
                      "vault",
                      "vpn",
                      "vpn2",
                      "web",
                      "webadvisor",
                      "webadvisortest",
                      "webtest",
                      "webmail",
                      "winapi",
                      "winapitest",
                      "ww3",
                      "www"]

    for mal in mal_subdomains:
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
