"""
Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

favNum = {'dave': [44, 69, 13], 'spratt': [14, 22, 29], 'kv': [1776, 1861, 1945], 'john': [2, 3, 4], 'sean': [19, 25]}
for key, value in favNum.items():
    if len(key) < 3:
        print(f'\nKey: {key.upper()}')
    else:
        print(f'\nKey: {key.title()}')

    for num in value:
        print(f'\t{num}')
