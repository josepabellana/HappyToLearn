# lists

airport = ['heathrow', 'gatwick', 'stansted']

print(airport)
print(airport[0]) # indexing starts at 0

print(airport[3]) # force error

airport.extend(['oxford']) # use keyword extend to increase a list

airport.remove('gatwick') # use keyword remove to decrease a list

# generate a copy

airport_backup = airport[:]

wrong_airport = airport.pop()

print(airport,airport_backup)