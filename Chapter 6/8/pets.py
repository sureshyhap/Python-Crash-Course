rocky = {
    "kind" : "dog",
    "owner" : "Suraya"
    }

scooter = {
    "kind" : "cat",
    "owner" : "Suresh"
    }

pets = [rocky, scooter]

for pet in pets:
    print(pet["owner"] + " has a " + pet["kind"] + ".")
