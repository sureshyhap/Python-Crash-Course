from user import User

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
