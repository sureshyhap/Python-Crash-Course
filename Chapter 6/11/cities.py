cities = {
    "New York" : {
        "country" : "America",
        "population" : 8623000,
        "fact" : "New York City is known as the Big Apple!"
        },
    "Tokyo" : {
        "country" : "Japan",
        "population" : 9273000,
        "fact" : "Tokyo is the largest metropolitan area in the world!"
        },
    "Chicago" : {
        "country" : "America",
        "population" : 2716000,
        "fact" : "Spray paint was invented in Chicago!"
        }
    }

for city, info in cities.items():
    print(city + " is located in " + info["country"] + ". " +
          "It has a population of " + str(info["population"]) +
          ". " + info["fact"])
