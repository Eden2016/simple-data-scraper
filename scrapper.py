import dryscrape
import json
from bs4 import BeautifulSoup


path_to_json = './response.json'

dryscrape.start_xvfb()
session = dryscrape.Session()
session.visit('https://developers.onederful.co/payers')
response = session.body()
soup = BeautifulSoup(response, 'html.parser')

payers = []

for tr in soup.find('tbody'):
    tr_list = {}
    for td in tr:
        if isinstance(td.contents[0], str):
            tr_list['label'] = td.string
        else:
            tr_list['value'] = td.string
        tr_list['free'] = 'true'
    payers.append(tr_list)

file = open(path_to_json, 'r+')
file.truncate(0)
file.write(json.dumps(payers))
file.close()

