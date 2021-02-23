rivers = {'nile': 'egypt', 'tigres': 'iraq', 'missouri': 'north america'}

for river, country in rivers.items():
    print(f'The {river.title()} river runs through {country.title()}.')