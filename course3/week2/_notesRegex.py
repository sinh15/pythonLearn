# Notes on regex python
import re #we need to import the library to use regex

# re.search() => See if string matches regex
# re.findall() => extract portions of string that match regex

text = open('mbox-short.txt')
for line in text:
    line = line.rstrip()
    if re.search('^From: ', line) : print line

x = 'My 2 favourite numbers are 15 and 42'
y = re.findall('[0-9]+', x)
print type(y), len(y), y


# ? => greedy matching for '*' and '+'
# if not used we try to match as forward as possible. Prefer the larger
## 'From: Using the :'
## '^F.+:' => greedy matching will match full string
## '^F.+?:' => non-greedy. Would match until from:
x = 'From: Using the : character'
print re.findall('^F.+:', x)
print re.findall('^F.+?:', x)

# We can select with '(' and ')' what we want to extract
# even more than one match
x = 'From stepehen.marquard@uct.ac.za Sat Jan'
print re.findall('\S+@\S+', x)
print re.findall('^From (\S+@\S+)', x)
print re.findall('^(From) (\S+@\S+)', x)
