import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
json_url = urllib.request.urlopen(url)
data = json_url.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
#print(json.dumps(info, indent=4))

s = 0
for item in info['comments']:
    s = s + int(item['count'])
print('Count ',len(info['comments']))
print('Sum ',s)
