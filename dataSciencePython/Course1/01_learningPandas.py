'''
START CREATING SERIES IN PYTHON
'''

# Import pandas and check what it is about
import pandas as pd
pd.Series?

# Creating series with panda
animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)

numbers = [1, 2, 3]
pd.Series(numbers)

animals =  ['Tiger', 'Bear', None]
pd.Series(animals)

numbers = [1, 2, None]
pd.Series(numbers)

# Trying for inequality test of None
import numpy as np
np.nan == None # false!!!
np.nan == np.nan # false !!
np.isnan(np.nan) # TRUE!
np.isnan(None) # CRASH

# More series (now with dictionaries)
sports = {'Archery': 'Bhuthan',
          'Golf' : 'Scotland',
          'Sumo' : 'Japan',
          'Taekwondo' : 'Shouth Korea'}

s = pd.Series(sports)
s
s.index
s.index[2]

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s



'''
QUERYING SERIES
'''

sports = {'Archery': 'Bhuthan',
          'Golf' : 'Scotland',
          'Sumo' : 'Japan',
          'Taekwondo' : 'Shouth Korea'}

s = pd.Series(sports)
s.index

# Query location based on integer position or index name (not method, attributes iloc, loc)
s.iloc[3] # South Korea
s.loc['Golf'] # Scotland

# Shortcuts if you need it
s['Golf'] # Scotland
s[3]

# Quan passing a series, sometimes is better to use the attributes
sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
s.index
s[0] # This won't call s.iloc[0] as one might expect, it generates an error instead
s.iloc[0] # Bhutan

# Go through values in series (normal for vs pandas)
 s = pd.Series([100.00, 120.00, 101.00, 3.00])
 s
 
total = 0
for item in s:
     total += item
print(total)

total = np.sum(s)
total

s = pd.Series(np.random.randint(0, 1000, 10000))
s.index
s.head(n=20)
len(s)

%%timeit -n 100
summary = 0
for item in s:
    summary += item
print(total) #1,27ms per loop
 
%%timeit -n 100
summary = np.sum(s) #139 micro seconds

                
# Apply functions to whole series
s.head()
type(s.iloc[0])
s += 2
s.head()


# Use loc & iloc to add values to series with unexisting indexes
s = pd.Series([1, 2, 3])
s.index
s.loc['Animal'] = 'Bears'
s
s.loc['Animal'] = 'Turtle'
s

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia', 'Barbados', 'Pakistan', 'England'], 
                                   index=['Cricket', 'Cricket', 'Cricket', 'Cricket'])
cricket_loving_countries

all_sports = original_sports.append(cricket_loving_countries)
all_sports


'''
THE PANDAS DATA FRAME
'''









