#import print
from __future__ import print_function

# Read files and create if it doesn't exist
entry = open("results.txt", 'U')
output = open("selectedPositions.csv", 'w+')

# Create dictionary
positions = dict()

# iterate through entry
for line in entry:
    # rstrip end of Line
    line = line.rstrip()

    # split reuslts by ';'
    params = line.split(";")

    # get position and quantity
    position = int(params[0].split("_")[2])
    quantity = int(params[1])

    # add to dictionary
    positions[position] = positions.get(position, 0) + quantity

# print column headers
print("Position", "Selections", sep=";", file = output)

# print dictionary in csv format
keys = positions.keys()
for key, value in positions.items():
    print(key, value, sep=";", file = output)
