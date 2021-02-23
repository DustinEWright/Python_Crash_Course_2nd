favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'{name.title()}.')

    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language}!")
