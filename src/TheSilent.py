import re

class TheSilent:
    def __init__(self,content):
        self.content = content
    def api(self):
        return dict((key,value) for key,value in {"dsa_private_key":list(dict.fromkeys(re.findall(r"-----BEGIN DSA PRIVATE KEY-----[\s\S]+-----END DSA PRIVATE KEY-----",self.content))),"ec_private_key":list(dict.fromkeys(re.findall(r"-----BEGIN EC PRIVATE KEY-----[\s\S]+-----END EC PRIVATE KEY-----",self.content))),"pgp_private_key":list(dict.fromkeys(re.findall(r"-----BEGIN PGP PRIVATE KEY BLOCK-----[\s\S]+-----END PGP PRIVATE KEY-----",self.content))),"pypi_api":list(dict.fromkeys(re.findall(r"pypi-[a-zA-Z0-9-_]{85,}",self.content))),"rsa_private_key":list(dict.fromkeys(re.findall(r"-----BEGIN RSA PRIVATE KEY-----[\s\S]+-----END RSA PRIVATE KEY-----",self.content))),"tailscale_api":list(dict.fromkeys(re.findall(r"tskey-api-[a-zA-Z0-9]+|tskey-auth-[a-zA-Z0-9]+|tskey-client-[a-zA-Z0-9]+|tskey-scim-[a-zA-Z0-9]+|tskey-webhook-[a-zA-Z0-9]+",self.content)))}.items() if value)
    def classified(self):
        return True if re.search("not for public release",self.content.lower()) else False
    def email(self):
        return [i.rstrip(".") for i in list(dict.fromkeys(re.findall(r"[a-z0-9][a-z0-9\.]+@[a-z][a-z0-9]+\.[a-z0-9]+[a-z0-9\.]+|[a-z0-9][a-z0-9\.]+[\(\{\[\<]at[\)\}\]|>][a-z][a-z0-9]+\.[a-z0-9]+[a-z0-9\.]+",self.content.lower())))]
    def ipaddress(self):
        return list(dict.fromkeys(re.findall(r"\b(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2[0-9]|3[0-1])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})\b",self.content)))
    def ipcamera(self):
        return True if re.search(r"camera live image|webcamxp \d",self.content.lower()) else False
    def links(self):
        return [i.rstrip("/") for i in list(dict.fromkeys(re.findall(r"<.+href\s*=\s*[\"\'](\S+?)(?=[\"\'\\])",self.content)))] + [i.rstrip("/") for i in list(dict.fromkeys(re.findall(r"<.+src\s*=\s*[\"\'](\S+?)(?=[\"\'\\])",self.content)))]
    def phone(self):
        return list(dict.fromkeys(re.findall(r"tel:\+?\d{10,11}|\(\d{3}\)-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}",self.content)))
    def ssn(self):
        return list(dict.fromkeys(re.findall(r"(?!000|666)[0-8]\d{2}-(?!00)\d{2}-(?!0000)\d{4}",self.content)))
    def subnet(self):
        return list(dict.fromkeys(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}",self.content)))
    def webforms(self):
        return [{f"METHOD":re.findall(r"method\s*=\s*[\"\'](\S+?)(?=[\"\'\\])",value)[0].upper(),f"ACTION": re.findall(r"action\s*=\s*[\"\'](\S+?)(?=[\"\'\\])", value)[0],f"INPUT": [re.findall(r"\b(?:type|name|value)\s*=\s*[\"\']([^\"\']+)[\"\']", field) for field in re.findall(r"<input[^>]+>", value)]}for key,value in enumerate(list(dict.fromkeys(re.findall(r"<form[\S\s\n]+?(?=form>)", self.content))))]
