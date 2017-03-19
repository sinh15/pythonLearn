# Get all different words from the text

fname = raw_input("Enter file name: ")
text = open(fname)
allWords = list()
for line in text:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        if word not in allWords : allWords.append(word)

allWords.sort()
print allWords