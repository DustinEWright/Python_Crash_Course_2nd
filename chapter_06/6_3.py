"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""

glossary = {
    '01 - integer': 'An integer is a whole number (not a fraction) that can be positive, negative, or zero. Integers are a commonly used data type in computer programming. ... For example, whenever a number is being incremented, such as within a "for loop" or "while loop," an integer is used.',
    '02 - comment': 'In computer programming, a comment is a programmer-readable explanation or annotation in the source code of a computer program. They are added with the purpose of making the source code easier for humans to understand, and are generally ignored by compilers and interpreters',
    '03 - float': 'Float () is a built-in Python function that converts a number or a string to a float value and returns the result.',
    '04 - string': 'A sequence of Unicode characters.',
    '05 - char': 'The chr () method returns a string representing a character whose Unicode code point is an integer.',
    '06 - dictionary': 'Similar to a HashMap in Java',
    '07 - set': 'Similar to a list',
    '08 - tuple': 'TBD',
    '09 - list': 'TBD',
    '10 - array': 'Does this exist in Python?'}


for word in glossary:
    print("\n" + word.title() + ":\n\t" + glossary[word])
