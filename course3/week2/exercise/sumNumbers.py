import re
text = open('regex_sum_233208.txt')

numbers = list()
for line in text:
    lineNum = re.findall('[0-9]+', line)
    numbers = numbers + lineNum

sum = 0
for num in numbers:
    sum = sum + int(num)

print sum
