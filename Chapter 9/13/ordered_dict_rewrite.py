from collections import OrderedDict

definitions = OrderedDict()
definitions["String"] = "A series of characters."
definitions["Loop"] = "Functionality for repeating blocks of code."
definitions["Conditional Statement"] = "Functionality for choosing a path among many."
definitions["List"] = "A collection of data."
definitions["Variables"] = "Stores a certain value for later use."
definitions["Integer"] = "A signed number."
definitions["Set"] = "Hold unique data."
definitions["Dictionary"] = "Holds key value pairs."
definitions["Immutable"] = "Cannot be altered."
definitions["Tuple"] =  "An immutable list of data."

for word, definition in definitions.items():
    print(word + ": " + definition)
    
