"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.

"""
destinations = {}
active = True

prompt = 'If you could visit one place in the world, where would you go?  '


while active:
    name = input('What is your name?  ') # prompts for the key
    destination = input(prompt) # prompts for the value
    destinations[name] = destination # adds the key and value to the dictionary

    repeat = input('Go again?  (yes/no)  ')
    if repeat == 'no':
        active = False

print('\n************ Poll Complete ************')

for name, destination in destinations.items():
    print(f'{name.title()} wants to go to {destination.title()}.')
