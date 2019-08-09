cubes = [x ** 3 for x in range(1, 11)]
for cube in cubes:
    print(cube)
print("The first three items in the list are: ", end="")
for cube in cubes[:3]:
    print(str(cube) + " ", end="")
print()
print("Three items from the middle of the list are: ", end="")
for cube in cubes[3:6]:
    print(str(cube) + " ", end="")
print()
print("The last three items in the list are: ", end="")
for cube in cubes[-3:]:
    print(str(cube) + " ", end="")
