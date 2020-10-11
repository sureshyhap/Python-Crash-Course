rivers = {
    "nile" : "egypt",
    "mississippi" : "america",
    "ganges" : "india"
    }

for river, country in rivers.items():
    print("The {} runs through {}.".format(river.title(), country.title()))

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
