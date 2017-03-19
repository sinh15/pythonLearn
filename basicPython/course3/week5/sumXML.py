import urllib
import xml.etree.ElementTree as ET

# Read URL
url = raw_input("Enter Location: ")
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_42.xml'
elif int(url) == 1 : url = 'http://python-data.dr-chuck.net/comments_233210.xml'

# Retrieve Data from URL
print "Retrieving", url
data = urllib.urlopen(url).read()
print "Retrieved", len(data)
tree = ET.fromstring(data)

# Search for numbers and sum them
totalSum = 0
numbers = tree.findall('.//count')
for number in numbers:
    totalSum = totalSum + int(number.text)

# Print Solution
print "Count:", len(numbers)
print "Sum:", totalSum
