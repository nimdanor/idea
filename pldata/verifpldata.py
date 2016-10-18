
import requests

import json

d=dict()

d["key"]='clef'

d["cvalue"]=" Donnée a effacer"

sval = json.dumps(d)

r = requests.get('http://pl.univ-mlv.fr/pldata/add',data = sval)

for u in r:
	print(str(u))

