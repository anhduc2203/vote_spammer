import os
import signal
import requests
import subprocess
from time import sleep
from bs4 import BeautifulSoup

class VoteSpammer: 
    config = []
    new_votes = None
    old_votes = None
    stamp = None
    successful_request = False
    verbose = False

    def __init__(self, config, verbose=False, stamp=None):
        self.config = config
        self.verbose = verbose
        self.stamp = stamp

    def get_votes(self):
        r = requests.get(
                self.config['urls']['get_votes'], 
                proxies=self.config['proxies']
        )
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.find(id="page-header-vote").span.text

    def submit_vote(self):
        r = requests.post(
                self.config['urls']['post_vote'],
                headers=self.config['post_vote_headers'],
                proxies=self.config['proxies']
        )

    def start_vote(self):
        self.old_votes = self.get_votes()
        
        if self.verbose: 
            print "current votes: " + str(self.old_votes)
            print "submitting request..."

        self.submit_vote()
        self.new_votes = self.get_votes()
        
        if self.verbose: 
            print 'current votes: ' + str(self.new_votes)
        
        self.successful_vote = False
        if self.old_votes < self.new_votes: 
            self.successful_vote = True
            if self.stamp is not None: 
                print self.stamp
        return self.successful_vote

