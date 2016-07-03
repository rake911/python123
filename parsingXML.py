import urllib
import xml.etree.ElementTree as ET
url = raw_input('Enter - ')
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/comments_42.xml'
else:
    url = 'http://python-data.dr-chuck.net/comments_254426.xml'

uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
z = []

for x in results:
    y = x.find('count').text
    w = int(y)
    z.append(w)

#print sum(z)
