people = ["Albert Einstein", "Isaac Newton", "James Maxwell", "Stephen Hawking"]

print("Welcome to dinner, " + people[0] + ".")
print("Welcome to dinner, " + people[1] + ".")
print("Welcome to dinner, " + people[2] + ".")

print("I'm sorry you couldn't make it, " + people[-1] + ".")
people[-1] = "Max Planck"

print("Welcome to dinner, " + people[0] + ".")
print("Welcome to dinner, " + people[1] + ".")
print("Welcome to dinner, " + people[2] + ".")
print("Welcome to dinner, " + people[3] + ".")

print("Alas, I've found a bigger table!")
people.insert(0, "Richard Feynman")
people.insert(2, "Michael Faraday")
people.append("Carl Gauss")

print("Welcome to dinner, " + people[0] + ".")
print("Welcome to dinner, " + people[1] + ".")
print("Welcome to dinner, " + people[2] + ".")
print("Welcome to dinner, " + people[3] + ".")
print("Welcome to dinner, " + people[4] + ".")
print("Welcome to dinner, " + people[5] + ".")
print("Welcome to dinner, " + people[-1] + ".")

