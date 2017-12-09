import yaml
from src.VoteSpammer import VoteSpammer
from src.Proxy import Proxy
from random import randint
from time import sleep

config = yaml.load(open('./config.yml'), Loader=yaml.BaseLoader)

skullbro = """ .-~~-.
(_^..^_)
  HHHH
  `--'"""

vs = VoteSpammer(config, True, skullbro)
proxy = Proxy()

while True:
    for out in proxy.start_proxy():
        print(out)
        if "Bootstrapped 100%: Done" in out:
            vs.start_vote()
            print "completely loaded; killing proxy"
            proxy.kill_proxy()
    if vs.successful_vote:
        print "request went through!"
        sleeptime = randint(0,60)
        print "sleeping for: " + str(sleeptime) + "s"
        sleep(sleeptime)
    else:
        print "error: trying again immediately"

