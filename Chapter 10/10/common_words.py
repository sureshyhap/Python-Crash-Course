def count_words(filename):
    try:
        with open(filename, "r") as file1:
            contents = file1.read().rstrip()
            the = contents.lower().count("the")
            print(the)
    except FileNotFoundError:
        pass

    
count_words("alice.txt")
count_words("moby_dick.txt")
