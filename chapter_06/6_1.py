"""
6-1. Person: Use a dictionary to store information about a person
you know. Store their

first name
last name
age
city

in which they live. You should have keys such as first_name,
last_name, age, and city. Print each piece of information
stored in your dictionary.
"""

person = {'first_name': 'dave', 'last_name': 'laney', 'age': 5, 'city': 'eldon'}
for key, value in person.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

