usernames = ["fwesh", "fweshpwince", "Forte", "SkyTree", "Gospel", "admin"]
del usernames[:]

if usernames:
    for name in usernames:
        if name == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + name + ", thank you for logging in again.")
else:
    print("We need to find some users!")
        
            
