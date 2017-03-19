## Word Counter
name = raw_input("Enter File:")
handle = open(name, "r")
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print "Big Count:", bigCount, "Big Word:", bigWord


## Word Counter Alternate
## Read line by line
handle = open(name, "r")
counts = dict()

for line in handle:
    words = line.rstrip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    bigCount = None
    bigWord = None
    for word, count in counts.items():
        if bigCount is None or count > bigCount:
            bigWord = word
            bigCount = count

print "Big Count:", bigCount, "Big Word:", bigWord
