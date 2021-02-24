"""
Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""

cities = {'omaha': {
    'country': 'united states',
    'pop': '1_000_000',
    'fun': 'zoo',
    },
    'columbia': {
        'country': 'united states',
        'pop': '65_000',
        'fun': 'olde un',
    },
    'eldon': {
        'pop': '5_000',
        'country': 'united states',
        'fun': 'gravel roadn',
    }
}

for city, city_info in cities.items():
    population = city_info['pop']
    location = city_info['country']
    fun_fact = city_info['fun']

    print(f'{city.title()} is located in {location.title()}.\n\tIt has a population of {population}.\n\tFor fun you can try the {fun_fact.title()}.\n')

