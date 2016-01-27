# Read numbers from an HTML page
import urllib
from BeautifulSoup import *

#http://python-data.dr-chuck.net/comments_42.html
#http://python-data.dr-chuck.net/comments_233213.html
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

# Retrieve all of the span tags
soup = BeautifulSoup(html)
tags = soup("span")
totalSum = 0
count = 0
for tag in tags:
    totalSum = totalSum + int(tag.contents[0])
    count = count+1

print "Count", count
print "Sum", totalSum
