from bs4 import BeautifulSoup
import requests
import yaml

config = yaml.load(open('./config.yml'), Loader=yaml.BaseLoader)
required_name = config['contestant_name']

r = requests.get(config["position_url"])

soup = BeautifulSoup(r.text, 'html.parser')
contestants = soup.find(id='page-item').findAll('div', recursive=False)

for index, cont in enumerate(contestants):
    received_name = cont.div.div.a.span.span.text
    if (received_name.lower() == required_name.lower()):
        print "\nName: {}\nPosition: {}\n".format(required_name, index+1)
        break
