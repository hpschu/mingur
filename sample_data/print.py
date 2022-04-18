import json
import pprint

fil = open('output.json')
data = json.load(fil)

pprint.pprint(data)
