"""
Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
"""

# 7-5 redo
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

active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print('pay $0')
        elif age < 13:
            print('pay $10')
        else:
            print('pay $15')
    
print('\n********** normal termination **********')