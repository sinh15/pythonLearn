# Tuples are "immutable"
x = [9, 8, 7]
x[2] = 6 # WOULD NOT complaint

y = "ABC"
y[2] = "D" # WOULD complain

z = (5, 3, 3)
z[2] = 0 # WOULD complain

# Tuples also have som restrictions that WOULD NOT WORK
z.sort() # ERROR
z.append() # ERROR
z.reverse() # ERROR


# See what can you do with tuples
dir(z) # "count", "index"


# So why TUPLES?
## More efficiency
## Not need for them to be modifiable
## Temporary variables => tuples over lists

# Double assignments at the same time. You can remove lhand '()'
(x, y) = (4, "fred")
print y # fred
a, b = (99, 98)
print a # 99

# Touples are comparable: ">. == , <"
x = (0, 1, 2) < (5, 1, 2) # compare by positions. if draw, next

# Sort lists with Touples
d = {'a':10, 'b':1, 'c':22}
print d.items()
t = d.items()
print sorted(t)
t.sort(reverse=True)
print t


# You can use the reverse key=>value dict to find max & mins
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

# Hack to create lists given dictionaries
c = {'a':10, 'b':1, 'c':22}
print sorted( [ (v,k) for k, v in c.items() ] )
## [(1, 'b'), (10, 'a'), (22, 'c')]
