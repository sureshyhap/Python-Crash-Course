favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
    }

should_take_poll = ['mike', 'edward', 'priscilla', 'jen', 'sarah']
"""
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
"""

for name in favorite_languages.keys():
    if name not in should_take_poll:
        print("Thank you for taking the poll " + name.title() + "!")
    else:
        print("You should take the poll " + name.title() + "!")
