"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value
in your dictionary. Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.
"""

favNum = {'dave': 44, 'spratt': 14, 'kv': 1776, 'john': 2, 'sean': 19}
# loops are later
#for key, value in favNum.items():
 #   if len(key) > 2:
  #      print(f'\nKey: {key.title()}')
   # else:
    #    print(f'\nKey: {key.upper()}')

    #print(f'Value: {value}')

name = 'dave'
print(f"Dave's favnum is: {favNum[name]}")

name = 'spratt'
print(f"Spratt's favnum is: {favNum[name]}")

name = 'kv'
print(f"KV's favnum is: {favNum[name]}")

name = 'john'
print(f"John's favnum is: {favNum[name]}")

name = 'sean'
print(f"Sean's favnum is: {favNum[name]}")
