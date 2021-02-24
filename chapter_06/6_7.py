"""

Make two new dictionaries representing different people, and store all three
dictionaries in a list called people.

Loop through your list of people. As you loop through the list,
print everything you know about each person.

"""

dave = {'first_name': 'dave', 'last_name': 'laney', 'age': 5, 'city': 'eldon'}
john = {'first_name': 'john', 'last_name': 'mcneely', 'age': 7, 'city': 'eldon'}
spratt = {'first_name': 'jeremy', 'last_name': 'spratt', 'age': 2, 'city': 'eldon'}

people = [dave, john, spratt]

for person in people:
    firstName = person['first_name'].title()
    lastName = person['last_name'].title()
    age = person['age']
    city = person['city'].title()

    print(f'{firstName} {lastName} is {age} years old and lives in {city}' )

