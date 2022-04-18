import requests
import pprint
from flask import Flask, render_template
import sys
import os
from dotenv import load_dotenv
import pprint
import json

load_dotenv()

API_ID = os.getenv('API_ID')
URL_BASE = os.getenv('URL_BASE')

headers = {'Authorization': 'Client-ID ' + API_ID}
r = requests.get(URL_BASE + 'gallery/hot/viral/0.json', headers=headers)
data = r.json()
pp = pprint.PrettyPrinter()
#pp.pprint(data)
for el in data['data']:
    print('######### POST ########')
    print(el['title'])
    print(el['datetime'])
    if 'mp4' in el.keys():
        print(el['link'])
        print(el['description'])
    else:
        try:
            for image in el['images']:
                print(image['link'])
                print(image['description'])
        except:
            print('An exception occurred while processing data:')
            pp.pprint(el)

r = requests.get(URL_BASE + 'credits', headers=headers)
print(r.json())

