pizzas = ["cheese", "extra cheese", "supreme"]
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza!")
friend_pizzas = pizzas[:]
pizzas.append("veggie")
friend_pizzas.append("stuffed crust")
print("My favorite pizzas are: ", end="")
for pizza in pizzas:
    print(pizza + " ", end="")
print()
print("My friend's favorite pizzas are: ", end="")
for pizza in friend_pizzas:
    print(pizza + " ", end="")
