# Make a program that follows links and find names
import urllib
from BeautifulSoup import *

# Enter Parameters
## https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
## https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Isaa.html
url = raw_input("Ener URL: ")
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

# Retrieve pages
iteration = 0
while iteration <= count:
    if iteration != count : print "Retrieving:", url
    else : print "Last Url", url
    html = urllib.urlopen(url).read()

    # Retrieve 'Position' A tag
    soup = BeautifulSoup(html)
    tags = soup("a")
    url = tags[position-1].get('href', None)

    # Increase iteration
    iteration = iteration + 1
