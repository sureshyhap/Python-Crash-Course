current_users = ["fwesh", "fweshpwince", "forte", "skytree", "gospel"]

new_users = ["Applejack", "SkyTree", "Celestia", "Patrick", "fweshpwince"]

for user in new_users:
    if user.lower() in current_users:
        print("You need to enter a new username.")
    else:
        print("Username available.")
