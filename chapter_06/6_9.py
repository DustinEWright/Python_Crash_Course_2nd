"""
Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person.  Loop through the dictionary, and print
each person’s name and their favorite places.
"""

favePlaces = {'dave': ['camp', 'bar', 'work'],
              'john': ['columbia', 'work', 'bar'],
              'spratt': ['home', 'camp', 'pub']}

for name, places in favePlaces.items():
    print(f'{name.title()} like to be at:')
    for fave in places:
        print(f'\t{fave.title()}')
