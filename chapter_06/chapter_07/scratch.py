prompt = '\nSay when to quit.'
prompt += '\nEnter quite to...quit!  '

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

print('\n********* normal termination *********')