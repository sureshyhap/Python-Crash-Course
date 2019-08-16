class User():
    """User profile"""
    def __init__(self, first, last, nick, country, age):
        self.first_name = first
        self.last_name = last
        self.nickname = nick
        self.country = country
        self.age = age
        
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() +
              ", a.k.a. " + self.nickname + " is from " +
              self.country + " and is " + str(self.age) + " years old.")

    def greet_user(self):
        print("Hello " + self.first_name.title())


class Privileges():
    def __init__(self, privileges= ["can add post", "can delete post",
                                    "can ban user"]):
        self.privileges = privileges
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title())


class Admin(User):
    def __init__(self, first, last, nick, country, age):
        super(Admin, self).__init__(first, last, nick, country, age)
        self.privileges = Privileges()


user1 = User("Suresh", "Yhap", "SkyTree", "America", 26)
user2 = User("Joseph", "Michael", "fwesh", "America", 26)

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()

"""
privileges = ["can add post", "can delete post", "can ban user"]
admin = Admin("Suresh", "Yhap", "Forte", "Japan", 26, privileges)
admin.show_privileges()
"""
admin = Admin("Suresh", "Yhap", "Forte", "Japan", 26)
admin.privileges.show_privileges()
