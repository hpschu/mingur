import requests
import config
import pprint

print(config.ID)
print(config.SECRET)

headers = {'Authorization': 'Client-ID ' + config.ID}
r = requests.get(config.url_base + 'gallery/hot/viral/0.json', headers=headers)
data = r.json()
for el in data['data']:
    print(el['title'])
    print(el['datetime'])
    for image in el['images']:
        print(image['link'])
        print(image['description'])


r = requests.get(config.url_base + 'credits', headers=headers)
print(r.json())

