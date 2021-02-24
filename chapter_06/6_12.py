"""
We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs
from this chapter, and extend it by adding new keys and values, changing
the context of the program or improving the formatting of the output.
"""
pets = []

buddy = {'name': 'buddy', 'kind': 'cat', 'owner': 'dustin', 'quirk': 'scardy cat'}
pets.append(buddy)
trouble = {'name': 'trouble', 'kind': 'cat', 'owner': 'dustin', 'quirk': 'true predator'}
pets.append(trouble)
chris = {'name': 'chris', 'kind': 'cat', 'owner': 'dustin', 'quirk': 'loved to run'}
pets.append(chris)

#    lastName = person['last_name'].title()

for pet in pets:
    name = pet['name'].title()
    kind = pet['kind'].title()
    owner = pet['owner'].title()
    quirk = pet['quirk'].title()


    print(f'{name} was a {kind} who had the oddest quirk.  He was a real {quirk} and was owned by {owner}.')




