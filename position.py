from bs4 import BeautifulSoup
import requests
import yaml

def extract_info_from_node(node): 
    data = node.div.div.a.findAll('span', recursive=True)
    return {
            'name' : data[1].text.encode('utf-8'),
            'votes' : data[4].text
    }

def output_info(info): 
    print """{}
    Votes: {}
    Position: {}
    """.format(info['name'], info['votes'], info['position'])

config = yaml.load(open('./config.yml'), Loader=yaml.BaseLoader)
required_name = config['contestant_name'].encode('utf-8')

r = requests.get(config["position_url"])

soup = BeautifulSoup(r.text, 'html.parser')
contestants = soup.find(id='page-item').findAll('div', recursive=False)

old = None
for index, cont in enumerate(contestants):
    info = extract_info_from_node(cont)
    
    if (info['name'].lower() == required_name.lower()):
        if old: 
            info = extract_info_from_node(old)
            info['position'] = index
            output_info(info)

        info = extract_info_from_node(cont)
        info['position'] = index+1
        output_info(info)
        
        if index+1 <= len(contestants):
            info = extract_info_from_node(contestants[index+1])
            info['position'] = index+2
            output_info(info)
        
        break
    old = cont
