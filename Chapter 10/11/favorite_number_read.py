import json

with open("fav_number.json", "r") as file_obj:
    fav_number = json.load(file_obj)

print("I know your favorite number! It's " + str(fav_number) + ".")
