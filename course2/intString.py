#String Functions
## string methods https://docs.python.org/2/library/stdtypes.html#string-methods

x = "BANANA"

print len(x)

print x[2:4]

x = x.lower()
print x

x = x.upper()
print x

## To ask for all the functions applicable to a type
print type(x)
#print dir(x) ##b etter ask in python interpreter

fruit = "banana"
pos = fruit.find("na")
print pos

aa = fruit.find("z")
print aa

greet = "Hello Bob"
nstr = greet.replace('Bob', 'Jane')
print nstr

## Strip functions
greet = "   Hello Bob   "
print greet.lstrip()
print greet.rstrip()
print greet.strip()

line = 'Please have a nice day'
print line.startswith('Please')
print line.startswith('p')


