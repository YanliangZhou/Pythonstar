# """show tha city"""
# def city_name(city, country, population):
#     """Generate a neatly formatted full name."""
#     full_name = city + ', ' + country + " - population " + population
#     return full_name.title()

"""show tha city"""
def city_name(city, country, population=''):
    """Generate a neatly formatted full name."""
    if population:
        full_name = city.title() + ', ' + country.title() + " - population " + str(population)
    else:
        full_name = city.title() + ', ' + country.title()
    return full_name