import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
pos = input('Enter position: ')
count = int(count)
pos = int(pos)
#i = 0;
c = 0;
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print('Retrieving: ',url)

# Retrieve all of the anchor tags
tags = soup('a')

#I am still going to submit this implementation, but the commented code below
#is a very inefficient implementation until I figured out a better one.
#while c < count:
#    while i < pos:
#        if (i == 2):
#            url = tags[i].get('href', None)
#            print('Retrieving: ',url)
#            html = urllib.request.urlopen(url, context=ctx).read()
#            soup = BeautifulSoup(html, 'html.parser')
#            tags = soup('a')
#        i = i + 1
#    c = c + 1
#    i = 0;

#I realized that I am given the position, so I just grab the url straight from the position instead of loop.
while c < count:
    url = tags[pos-1].get('href', None)
    print('Retrieving: ',url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    c = c + 1
