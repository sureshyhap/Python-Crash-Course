import json

try:
    with open("fav_number.json", "r") as file_obj:
        fav_number = json.load(file_obj)
except FileNotFoundError:
    fav_number = int(input("What is your number? "))
    with open("fav_number.json", "a") as file_obj:
        json.dump(fav_number, file_obj)
    print("I'll say your favorite number next time!")
else:
    print("I know your favorite number! It's " + str(fav_number) + ".")
