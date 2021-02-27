"""
A movie theater charges different ticket prices depending on
a person’s age.
If a person is under the age of 3, the ticket is free;
if they are between 3 and 12, the ticket is $10
if they are over age 12, the ticket is $15

Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""
prompt = 'How old are you? \nEnter quit to stop  '

while True:
    age = input(prompt)
    if age != 'quit':
        age = int(age)

        if age < 3:
            print('pay $0')
        elif age < 13:
            print('pay $10')
        else:
            print('pay $15')
    else:
        break


print('\n********** normal termination **********')





