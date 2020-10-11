def city_country(city, country, population=0):
    formatted = city.title() + ", " + country.title()
    if population:
        formatted += " - population " + str(population)
    return formatted
