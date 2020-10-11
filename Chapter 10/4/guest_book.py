while True:
    name = input("Please enter your name ('q' to quit): ")
    if name == "q":
        break
    print("Welcome ", name + "!")
    with open("guest_book.txt", "a") as file_object:
        file_object.write(name + "\n")
