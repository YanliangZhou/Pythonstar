from collections import OrderedDict

favorite_languages = OrderedDict()

languages = {"print": "print the message", "int": "a data type", "str": "a data type",
             "dict": "a data format", "list": "a data list"}
languages["while"] = "a loop"
languages["if"] = "conditional check"
languages["input"] = "input data"
languages["function"] = "a way to solve a problem"
languages["sort"] = "a collection"

for words, meanings in languages.items():
    print(words.title() + ": " + meanings + ".")