from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = 0
s = 0
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Converts the contents which are of type string
    # into int and adds it to the sum
    s = s + int(tag.contents[0])
    count = count + 1
print('Count ',count)
print('Sum ',s)
