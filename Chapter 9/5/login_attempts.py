class User():
    """User profile"""
    def __init__(self, first, last, nick, country, age):
        self.first_name = first
        self.last_name = last
        self.nickname = nick
        self.country = country
        self.age = age
        self.login_attempts = 0
        
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() +
              ", a.k.a. " + self.nickname + " is from " +
              self.country + " and is " + str(self.age) + " years old.")

    def greet_user(self):
        print("Hello " + self.first_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Suresh", "Yhap", "SkyTree", "America", 26)
for i in range(5):
    user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
user2 = User("Joseph", "Michael", "fwesh", "America", 26)

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
