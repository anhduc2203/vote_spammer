import os
import signal
import requests
import subprocess
from time import sleep
from bs4 import BeautifulSoup
from random import randint
import yaml

config = yaml.safe_load(open('./config.yml'))

skullbro = """ .-~~-.
(_^..^_)
  HHHH
  `--'"""


class vote_spammer: 
    popen = 0
    successful_request = False

    def get_votes(self):
        r = requests.get("https://ceo.cancun.com/profile/mila-kasanda-5a29fd45137da",
                proxies=dict(
                    http='socks5://127.0.0.1:9050',
                    https='socks5://127.0.0.1:9050',
                )
        )
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.find(id="page-header-vote").span.text

    def submit_vote(self):
        r = requests.post("https://ceo.cancun.com/profile/mila-kasanda-5a29fd45137da",
                headers={
                    "Host": "ceo.cancun.com",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": "https://ceo.cancun.com/profile/mila-kasanda-5a29fd45137da",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Content-Length": "0",
                    "DNT": "1",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1"
                },
                proxies={
                    'http': 'socks5://127.0.0.1:9050',
                    'https': 'socks5://127.0.0.1:9050',
                }
        )

    def start_proxy(self):
        cmd =  ["tor"]
        self.popen = subprocess.Popen(cmd,
                    stdout=subprocess.PIPE,
                    universal_newlines=True,
                    shell=True,
                    preexec_fn=os.setsid
                )
        for stdout_line in iter(self.popen.stdout.readline, ""):
            yield stdout_line
        self.popen.stdout.close()
        return_code = self.popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)

    def kill_proxy(self):
        os.killpg(os.getpgid(self.popen.pid), signal.SIGTERM) 

    def start_vote(self):
        pre = self.get_votes()
        print("current votes: " + pre)
        print("sending vote request...")
        self.submit_vote()
        post = self.get_votes()
        print("current votes: " + post)
        
        print "*"*40
        if pre == post: 
            print "something went wrong :("
            self.successful_request = False
        else:
            self.successful_request = True
            print skullbro
            print "+1 vote :)"
        print "*"*40

vs = vote_spammer()

while True:
    for out in vs.start_proxy():
        print(out)
        if "Bootstrapped 100%: Done" in out:
            vs.start_vote()
            print "completely loaded; killing tor"
            vs.kill_proxy()
    if vs.successful_request:
        sleeptime = randint(0,60)
        print "sleeping for: " + str(sleeptime) + "s"
        sleep(sleeptime)
