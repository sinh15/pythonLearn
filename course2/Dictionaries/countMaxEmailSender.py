# Count who's the guy who has sent more emails
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name, "r")

# Generate the key=>value pairs
senders = dict()
for line in text:
    if line.startswith('From '):
        words = line.split()
        senders[words[1]] = senders.get(words[1], 0) + 1

# Go through the values and get the higher one
maxSender = None
maxSend = None
for name, total in senders.items():
    if maxSend is None or total > maxSend:
        maxSend = total
        maxSender = name

# Print Result
print maxSender, maxSend
