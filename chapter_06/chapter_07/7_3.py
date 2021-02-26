multiple = input('What number is a multiple of 10?  ')
multiple = int(multiple)

if multiple % 10 == 0:
    print(f'{multiple} is a multiple of 10.')
else:
    print(f'{multiple} is NOT a multiple of 10.')
