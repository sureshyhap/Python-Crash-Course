topping = ""
while topping != "quit":
    topping = input("Enter a topping: ")
    if topping != "quit":
        print("I will add " + topping + " to the pizza")

active = True
while active:
    topping = input("Enter a topping: ")
    if topping == "quit":
        active = False
    else:
        print("I will add " + topping + " to the pizza")

while True:
    topping = input("Enter a topping: ")
    if topping == "quit":
        break
    else:
        print("I will add " + topping + " to the pizza")
