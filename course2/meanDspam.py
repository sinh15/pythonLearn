# Extrat floating numbers of end of Line and compute mean
fname = raw_input("Enter file name: ")
text = open(fname)

# Variables to compute mean
totalSum = 0
totalCounted = 0
for line in text:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    # Extract floating number
    sPos = line.find(' ')
    length = len(line)
    number = float(line[sPos:length].strip())
    
    # Add number
    totalSum = totalSum + number
    totalCounted = totalCounted + 1

print "Average spam confidence:", totalSum/totalCounted
