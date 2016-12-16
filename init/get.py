import json
import urllib
import sys 

url = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'
print url
r = urllib.urlopen(url) 
f = json.loads(r.read())
id = f['latest']['snapshot']
url = None
for o in f['versions']:
    if o['id'] == id: 
        url = o['url']

if url:
    r = urllib.urlopen(url)
    f = json.loads(r.read())
    print f['downloads']['server']['url'] 

