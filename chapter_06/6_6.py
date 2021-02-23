favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

mustPoll = ['dave', 'john', 'jen', 'phil', 'spratt']

for name in favorite_languages.keys():
    print(f'Thanks {name.title()} for polling.')

for staff in mustPoll:
    if staff not in favorite_languages.keys():
        print(f'Hey {staff}, take the poll.')
    else:
        print(f'\tThanks {staff}, you are the example to learn from.')



