"""
Make several dictionaries, where each dictionary represents a different
pet. In each dictionary, include

kind of animal
owner’s name.

Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

pets = []

buddy = {'name': 'buddy', 'kind': 'cat', 'owner': 'dustin'}
pets.append(buddy)
trouble = {'name': 'trouble', 'kind': 'cat', 'owner': 'dustin'}
pets.append(trouble)
chris = {'name': 'chris', 'kind': 'cat', 'owner': 'dustin'}
pets.append(chris)

#    lastName = person['last_name'].title()

for pet in pets:
    name = pet['name'].title()
    kind = pet['kind'].title()
    owner = pet['owner'].title()

    print(f'{name} was a {kind} who was owned by {owner}.')




