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
# loops are later
#for key, value in person.items():
 #   print(f'\nKey: {key}')
  #  print(f'Value: {value}')

print(f"First Name: {person['first_name'].title()}")
print(f"Last Name: {person['last_name'].title()}")
print(f"City: {person['city'].title()}")
print(f"Age: {person['age']}")


