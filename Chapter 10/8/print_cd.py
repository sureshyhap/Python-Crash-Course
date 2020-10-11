try:
    with open("cats.txt", "r") as file1:
        for line in file1:
            print(line.rstrip())
except FileNotFoundError:
    print("There is no file!")

try:
    with open("dogs.txt", "r") as file2:
        for line in file2:
            print(line.rstrip())
except FileNotFoundError:
    print("There is no file!")
