import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/comments_42.html'
else:
    url = 'http://python-data.dr-chuck.net/comments_254429.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
x = []

for tag in tags:
    #print 'TAG:', tag
    #print 'Contents:', tag.contents[0]
    y = int(tag.contents[0])
    x.append(y)
#print sum(x)