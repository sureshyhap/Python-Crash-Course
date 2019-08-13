fav_nums = {
    "Rebecca" : [63, 22, 56],
    "Mike" : [57],
    "Willis" : [2, 10, 25, 50],
    "Robert" : [10, 100, 1000],
    "Andrea" : [12, 144, 11, 121]
    }

"""
print("Rebecca likes", str(fav_nums["Rebecca"]))
print("Mike likes", str(fav_nums["Mike"]))
print("Willis likes", str(fav_nums["Willis"]))
print("Robert likes", str(fav_nums["Robert"]))
print("Andrea likes", str(fav_nums["Andrea"]))
"""

for name, numbers in fav_nums.items():
    print(name + " likes the following numbers:")
    for number in numbers:
        print(str(number) + " ", end="")
    print()

    
