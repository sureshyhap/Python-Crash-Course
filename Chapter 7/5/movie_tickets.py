while True:
    age = int(input("Enter your age: "))
    if age == 0:
        break
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print("Your ticket will cost $" + str(price) + ".")
