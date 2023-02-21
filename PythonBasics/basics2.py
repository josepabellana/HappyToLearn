# dictionary

capital = {'brasil': 'brasilia', 'uk': 'london', 'germany': 'berlin'}

print(capital)

capital['brasil']

## works like in javascript

del capital['germany']
for k in capital:
    print(k)


text = 'The quick brown fox jumps over the lazy dog'

tokens = text.lower().split(' ')
print(tokens)

counter = dict()
for w in tokens:
    if(w in counter):
        counter[w]+= 1
    else:
        counter[w] = 1
print(counter)

plant_height = 5
if plant_height < 3:
    print('keep it')
elif (3<plant_height<15):
    print(plant_height)
else:
    print('nothing')


#functions
def count_word(text, characters_to_remove):
    return

