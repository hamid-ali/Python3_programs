import json
from difflib import get_close_matches

data = json.load(open("076 data.json"))


def translate(w):
    if w in data.keys():
        return "meaningig is %s" % data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        print("Did yo mean instead of " + get_close_matches(w, data.keys())[0])
        cmd = input("Enter y for yes or nfor exit: \n ")
        if cmd == "y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return
    else:
        return "Entered word does not exist."


word = input("Entera a word to get itsmeaning:  ")
print(translate(word))
