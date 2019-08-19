import json

fav_number = int(input("What is your number? "))

with open("fav_number.json", "a") as file_obj:
    json.dump(fav_number, file_obj)
