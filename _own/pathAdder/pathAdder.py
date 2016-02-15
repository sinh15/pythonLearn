# import print
from __future__ import print_function

# Read files and create if it doesnt exist
fname = raw_input("Enter file name: ")
oname = raw_input("Select desired output name: ")
extraPath = raw_input("Enter the desired extra path (HIT ENTER if you want to use the one in the code): ")
text = open(fname, 'U')
output = open(oname, 'w+')

# ================================================== #
# Introduce on the next var the value you want added #
# ================================================== #
extraPathCode = "PATH_ADDED_FOR_REFERENCE_"
# ================================================== #

# Select which extra path should be Used
if not extraPath:
    extraPath = extraPathCode

# Code to modify files
read = 0
modified = 0
for line in text:
    read = read + 1
    line = line.rstrip()
    if line:
        modified = modified + 1
        print (extraPath + line, file = output)

# Print Stats
print ("Lines Read", read)
print ("Lines Modified", modified)
