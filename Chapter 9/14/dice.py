import random

class Die():
    """Simulates a pair of dice"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


die = Die()
for i in range(10):
    die.roll_die()

print()

die = Die(10)
for i in range(10):
    die.roll_die()

print()
    
die = Die(20)
for i in range(10):
    die.roll_die()
