responses = {}
active = True

while active:
    name = input("What is your name? ")
    where = input("IF you could visit one place in the world, " +
                  "where would you go? ")
    responses[name] = where
    again = input("Poll again? (yes/no) ")
    if again == "no":
        active = False

for name, where in responses.items():
    print(name, "would like to travel to", where + ".")
