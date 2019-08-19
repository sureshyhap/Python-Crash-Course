while True:
    reason = input("Why do you like programming?('q' to quit) ")
    if reason == 'q':
        break
    with open("responses.txt", "a") as file_object:
        file_object.write(reason + "\n")
