import urllib
#from bs4 import BeautifulSoup
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/comments_42.html'
#else:
#    url = 'http://python-data.dr-chuck.net/comments_254429.h'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
#print tags

for tag in tags:
    #print 'TAG:', tag
    #print 'URL:', tag.get('href', None)
    print 'Contents:', tag.contents[0]
    #print 'Attrs:', tag.attrs
    #print tag.get('href', None)
    #print 'Span:', tag.get('comments', None)

