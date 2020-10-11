sandwich_orders = ["pastrami", "turkey", "pastrami", "ham", "pastrami", "chicken"]
finished_sandwiches = []

print("The deli is out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I finished your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)
