import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
import sys
import pprint
import json

load_dotenv('../.env')
sys.path.insert(1, getenv('APP_HOME'))

from models import Post, Image
from bootstrap import AppConfig

conf = AppConfig('../.env')

print(conf.DATABASE_URI)

engine = create_engine(getenv('DATABASE_URI'), echo=True)
Session = sessionmaker(bind=engine)
session = Session()

API_ID = getenv('API_ID')
URL_BASE = getenv('URL_BASE')

headers = {'Authorization': 'Client-ID ' + API_ID}
r = requests.get(URL_BASE + 'gallery/hot/viral/0.json', headers=headers)
data = r.json()
pp = pprint.PrettyPrinter()
#pp.pprint(data)

posts = []

for el in data['data']:
    post = Post(imgur_id=el['id'], title=el['title'], created_at=el['datetime'])
    print('######### POST ########')
    print(el['id'])
    print(el['title'])
    print(el['datetime'])
    if 'mp4' in el.keys():
        #print('Length of mp4 data:' . len(el['mp4']))
        image = Image(link=el['link'], description=el['description'], imgur_id=el['id'])
        print(el['link'])
        print(el['description'])
        post.images.append(image)
    elif 'images' in el.keys():
        for img in el['images']:
            print(img['id'])
            image = Image(link=img['link'], description=img['description'], imgur_id=img['id'])
            print(img['link'])
            print(img['description'])
            post.images.append(image)
    else:
        image = Image(link=el['link'], description=el['description'], imgur_id=el['id'])
        pprint.print(el)

    try:
        session.add(post)
        session.commit()
    except:
        print('Tried to add post, assuming duplicate, continue..')


Session.close()
r = requests.get(URL_BASE + 'credits', headers=headers)
print(r.json())
