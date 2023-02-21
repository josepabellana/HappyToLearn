# lists

airport = ['heathrow', 'gatwick', 'stansted']

print(airport)
print(airport[0]) # indexing starts at 0

#print(airport[3]) # force error

airport.extend(['oxford']) # use keyword extend to increase a list

airport.remove('gatwick') # use keyword remove to decrease a list

# generate a copy

airport_backup = airport[:]

wrong_airport = airport.pop()

print(airport,airport_backup)


for a in airport:
    print(a.upper())



# numerical list
nums = list(range(1,6))
print(nums)

for x in list(range(5)):
    print(x**2)

import math # sqrt, log, exp, etc

for x in list(range(5)):
    print(math.sqrt(x))

#Lists are useful for when you need to do some sort of repetitive task whether it is to modify, 
# parse or even extract some sort of signal from a data set. 
# However, the tuple object cannot be modified once it has been created.

#Tuples
# Tuples cannot be modified after it has been created

airport_tuple = tuple(airport)

airport[0]