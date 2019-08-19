with open("learning_python.txt") as file_object:
    lines = file_object.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("Python", "C")

for line in lines:
    print(line.rstrip())


