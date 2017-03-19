# Continue to skip iteration of loop
while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    elif line == "done":
        break
    print line
print 'End'