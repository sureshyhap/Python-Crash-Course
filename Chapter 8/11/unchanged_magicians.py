magicians = ["Houdini", "Chris Angel"]

def make_great(magicians):
    new_magic = []
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]
        new_magic.append(magicians[i])
    return new_magic

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

new_m = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_m)
