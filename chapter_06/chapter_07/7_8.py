"""
7-8. Deli: Make a list called sandwich_orders and fill it with
sandwiches.

make an empty list called finished_sandwiches. Loop through the
list of sandwich orders and print a message for each order, such
as I made your tuna sandwich.

As each sandwich is made, move it
to the list of finished sandwiches.

After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""

sandwich_orders = ['rubin', 'grilled cheese', 'burger', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'your {current_sandwich} sandwich is made.')
    finished_sandwiches.append(current_sandwich)

print('\n********** Finished Sandwiches **********')
for sandwich in finished_sandwiches:
    print(sandwich)


