"""
Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""
prompt = '\nWhat topping?'
prompt += 'enter quit when complete:  '

while True:
    topping = input(prompt)
    if topping != 'quit':
        topping = input(f'{topping} added ')
    else:
       break

print('\n************************* normal termination *************************')

