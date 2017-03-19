# Notes on dictionaries session
purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75

print purse
print "Candy in purse:", purse["candy"]


## Problem what happens when we try to access
## a memory value that doesn't exist
## we solve with the get and df value

### Clean solution
purse["shit"] = purse.get("shit", 0) + 1
print "Shit Value:", purse["shit"]

### Dirty solution
if "shit" in purse : purse["shit"] = purse["shit"] + 1
else : purse["shit"] = 1
print "Shit Value:", purse["shit"]


## Loop
for keyword in purse:
    print keyword, ":", purse[keyword]

## Check things inside a dictionary
print purse.items() # returns pairs key=>value
print purse.keys() # returns the keys
print purse.values() # returns the values inside the keys

## use the keys as list
x = purse.keys()
print type(x), x[0], x[2]


# Double iteration variables
for aaa, bbb in purse.items():
    print aaa, bbb
