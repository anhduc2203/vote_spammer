import os
import signal
import requests
import subprocess
from time import sleep
from bs4 import BeautifulSoup

popen = 0
skullbro = """ .-~~-.
(_^..^_)
  HHHH
  `--'"""

def get_votes():
    r = requests.get("",
            proxies=dict(
                http='socks5://127.0.0.1:9050',
                https='socks5://127.0.0.1:9050',
            )
    )
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find(id="page-header-vote").span.text

def submit_vote():
    r = requests.post("",
            headers={
            },
            proxies={
                'http': 'socks5://127.0.0.1:9050',
                'https': 'socks5://127.0.0.1:9050',
            }
    )

def start_proxy():
    global popen
    cmd =  ["tor"]
    popen = subprocess.Popen(cmd,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                shell=True,
                preexec_fn=os.setsid
            )
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def kill_proxy():
    global popen
    os.killpg(os.getpgid(popen.pid), signal.SIGTERM) 

def start_vote():
    pre = get_votes()
    print("current votes: " + pre)
    print("sending vote request...")
    submit_vote()
    post = get_votes()
    print("current votes: " + post)
    print "completely loaded; killing tor"
    kill_proxy()
    
    print "*"*40
    if pre == post: 
        print "something went wrong :("
    else:
        print skullbro
        print "+1 vote :)"
    print "*"*40

for out in start_proxy():
    print(out)
    if "Bootstrapped 100%: Done" in out:
        start_vote()

