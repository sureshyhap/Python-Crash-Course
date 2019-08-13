sandwich_orders = ["turkey", "ham", "chicken"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I finished your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)
