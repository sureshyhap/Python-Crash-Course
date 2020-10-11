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
