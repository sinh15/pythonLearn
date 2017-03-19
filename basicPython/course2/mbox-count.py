# Count lines that start with 'From '
fname = raw_input("Enter file name: ")
if len(fname) < 1 : name = "mbox-short.txt"
text = open(fname)

count = 0
for line in text:
    if line.startswith('From '):
        words = line.split()
        print words[1]
        count = count+1

print "There were", count, "lines in the file with From as the first word"
