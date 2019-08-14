magicians = ["Houdini", "Chris Angel"]

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

make_great(magicians)
show_magicians(magicians)
