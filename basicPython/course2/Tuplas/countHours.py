# Count how many emails have been sent on each hour
name = raw_input("Enter File:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name, "r")

# compute counts
lst = dict()
for line in text:
    if line.startswith('From '):
        hour = line.split()[5].split(":")[0]
        lst[hour] = lst.get(hour, 0) + 1

# Sort (can't sort at the same lane as assignments)
listItems = lst.items()
listItems.sort()

# Print
for k, v in listItems cmd : print k, v
