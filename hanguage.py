#!/bin/python

letters = {
    "a": "h",
    "b": "hh",
    "c": "Hh",
    "d": "HH",
    "e": "hH",
    "f": "hhh",
    "g": "Hhh",
    "h": "HHh",
    "i": "HhH",
    "j": "HHH",
    "k": "hHH",
    "l": "hHh",
    "m": "Hhhh",
    "n": "hhHh",
    "o": "hhH",
    "p": "hHhH",
    "q": "HhHH",
    "r": "hhhh",
    "s": "hHhhh",
    "t": "HhHh",
    "u": "hhhH",
    "v": "hhHH",
    "w": "HhhH",
    "x": "hhhhh",
    "y": "HHHHH",
    "z": "hHHH",
    " ": "H"
}

numbers = {
    "1": "-h-",
    "2": "-hh-",
    "3": "-Hh-",
    "4": "-HH-",
    "5": "-hhh-",
    "6": "-hHh-",
    "7": "-Hhh-",
    "8": "-HHh-",
    "9": "-HHH-",
    "0": "-HHHH-"
}

symbols = {
    "@": "~h~",
    "#": "~hh~",
    "$": "~Hh~",
    "_": "~hH~",
    "&": "~HH~",
    "+": "~hhh~",
    "-": "~hHh~",
    "×": "~Hhh~",
    "÷": "~hhH~",
    "π": "~hhhhh~",
    "*": "~HhHh~",
    '"': "~hhhH~",
    "=": "~HHHH~",
    "?": "~HhHHh~",
    "!": "~HhHhH~"
}



m = {}
m.update(letters)
m.update(numbers)
m.update(symbols)

def convert(inp):
    o = []
    for c in inp:
        c = c.lower()
        if c in m:
            o.append(m[c])
        else:
            o.append(c)
    return ".".join(o)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs=argparse.REMAINDER, help="all words after script name")
    
    args = parser.parse_args()
    
    full_text = " ".join(args.text)
    

    if full_text.strip() == "":
        while True:
            print("Examples:")
            print("Hello guys -> " + convert("Hello guys"))
            print("541 -> " + convert("541"))
            print("5 4 1 -> " + convert("5 4 1"))
            print("!!!@@! -> " + convert("!!!@@!"))
            i = input("Hanguage converter: ")
            if i != "exit":
                print(convert(i))
            else:
                break
print(convert(full_text))
