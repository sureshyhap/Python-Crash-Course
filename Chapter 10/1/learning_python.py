with open("learning_python.txt", "r") as file_object:
    contents = file_object.read()
print(contents)

with open("learning_python.txt", "r") as file_object:
    for line in file_object:
        print(line.rstrip())
print()

with open("learning_python.txt", "r") as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
