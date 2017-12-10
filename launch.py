from src.VoteSpammer import VoteSpammer
from src.Proxy import Proxy
from random import randint
from time import sleep
import requests
import sys
import yaml

config = yaml.load(open('./config.yml'), Loader=yaml.BaseLoader)

skullbro = """ .-~~-.
(_^..^_)
  HHHH
  `--'"""

vs = VoteSpammer(config, True, skullbro)
proxy = Proxy()
if len(sys.argv) > 1 and sys.argv[1] == 'purge':
    answer = raw_input("are you sure you want to purge the nodes? (y/n) > ")
    if answer.strip().lower() == "y":   
        proxy.purge_blocked_nodes()
    else:
        exit()
try:
    while True:
        for out in proxy.start_proxy():
            print(out)
            if "Bootstrapped 100%: Done" in out:
                vs.start_vote()
                
                if vs.successful_vote:
                    print "request went through!"
                    proxy.block_node(vs.get_ip())
                    sleeptime = randint(0,60)
                    print "sleeping for: " + str(sleeptime) + "s"
                    sleep(sleeptime)
                else:
                    print "error: trying again immediately"
                
                print "killing proxy and rotating IP"
                proxy.kill_proxy()

except KeyboardInterrupt:
    proxy.kill_proxy()

except Exception as e:
    proxy.kill_proxy()
    print e
