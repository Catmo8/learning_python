import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
xml = urllib.request.urlopen(url)
data = xml.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
s = 0
for count in counts:
    s = s + int(count.text)
print('Count: ',len(counts))
print('Sum: ',s)
