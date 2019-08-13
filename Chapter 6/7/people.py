mom = {
    "first_name" : "Seelochnie",
    "last_name" : "James",
    "age" : 59,
    "city" : "New York"
    }

dad = {
    "first_name" : "James",
    "last_name" : "Yhap",
    "age" : 60,
    "city" : "New York"
    }

me = {
    "first_name" : "Suresh",
    "last_name" : "Yhap",
    "age" : 26,
    "city" : "New York"
    }

people = [mom, dad, me]

"""
print(f"My mother's name is {mom['first_name']} {mom['last_name']}. " +
      "She is " + str(mom['age']) + f" years old and lives in {mom['city']}.")
"""

for person in people:
    print(person["first_name"] + " " + person["last_name"] +
          " is " + str(person["age"]) + " years old and lives in " +
          person["city"] + ".")
