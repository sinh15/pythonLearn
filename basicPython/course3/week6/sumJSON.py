# Sum numbers from JSON
import json
import urllib

# Read URL
url = raw_input("Enter Location:" )
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_42.json'
elif int(url) == 1 : url = 'http://python-data.dr-chuck.net/comments_233214.json'

# Retrieve data from URL
print "Retrieveing", url
data = urllib.urlopen(url).read()
print "Retrieved", len(data)
data = json.loads(data)

# print json.dumps(data, indent=4)
# Surf through comments
totalSum = 0
for comment in data["comments"]:
    totalSum = totalSum + int(comment["count"])

print "Count:", len(data["comments"])
print "Sum:", totalSum
