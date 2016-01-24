# Read file and print each line in caps
fname = raw_input("Enter file name: ")
text = open(fname)

for line in text:
    print line.upper().rstrip()