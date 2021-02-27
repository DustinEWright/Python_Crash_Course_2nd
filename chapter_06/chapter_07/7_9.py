"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times.

Add code near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""

sandwich_orders = ['pastrami', 'rubin', 'pastrami', 'grilled cheese', 'pastrami', 'burger', 'pastrami', 'chicken', 'pastrami']
finished_sandwiches = []

print('No more pastrami.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'your {current_sandwich} sandwich is made.')
    finished_sandwiches.append(current_sandwich)

print('\n********** Finished Sandwiches **********')
for sandwich in finished_sandwiches:
    print(sandwich)

print('\n********** All Sandwiches Complete **********')