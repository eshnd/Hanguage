#!/usr/bin/env python3

letters = { "Hhhhh": "a", "h": "b", "hh": "c", "Hh": "d", "HH": "e", "hH": "f", "hhh": "g", "Hhh": "h", "HHh": "i", "HhH": "j", "HHH": "k", "hHH": "l", "hHh": "m", "Hhhh": "n", "hhHh": "o", "hhH": "p", "hHhH": "q", "HhHH": "r", "hhhh": "s", "hHhhh": "t", "HhHh": "u", "hhhH": "v", "hhHH": "w", "HhhH": "x", "hhhhh": "y", "HHHHH": "z", "H": " "}

numbers = { "-h-": "1", "-hh-": "2", "-Hh-": "3", "-HH-": "4", "-hhh-": "5", "-hHh-": "6", "-Hhh-": "7", "-HHh-": "8", "-HHH-": "9", "-HHHH-": "0" }

symbols = { "~h~": "@", "~hh~": "#", "~Hh~": "$", "~hH~": "_", "~HH~": "&", "~hhh~": "+", "~hHh~": "-", "~Hhh~": "×", "~hhH~": "÷", "~hhhhh~": "π", "~HhHh~": "*", "~hhhH~": '"', "~HHHH~": "=", "~HhHHh~": "?", "~HhHhH~": "!" "~HHhHh~": ":"} #I added : for :V and for :D  


m = {}
m.update(letters)
m.update(numbers)
m.update(symbols)

def to_h(inp):
    o = []
    for c in inp:
        c = c.lower()
        if c in m:
            o.append(m[c])
        else:
            o.append(c)
    return ".".join(o)

def from_h(i):
    s = {v: k for k, v in m.items()}
    o = []
    for c in i.split("."):
        if c in s:
            o.append(s[c])
        else:
            o.append(c)
    return "".join(o)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--to-hanguage", type=str, help="Converts english to hanguage")
    group.add_argument("-f", "--from-hanguage", type=str, help="Converts english to hanguage")
    
    args = parser.parse_args()
    
    if args.to_hanguage:
        print(to_h(args.to_hanguage))
    elif args.from_hanguage:
        print(from_h(args.from_hanguage))
    else:
        print("Examples:")
        print("    Hello guys -> " + to_h("Hello guys"))
        print("    541 -> " + to_h("541"))
        print("    " + to_h("5 4 1") + " -> 5 4 1")
        print("    " + to_h("!!!@@!") + " -> !!!@@!")
        while True:
            i = input("Do you want to 1. convert to hanguage, 2. convert from hanguage, or 3. exit?: ")
            if "1" in i:
                print(to_h(input("Input: ")))
            elif "2" in i:
                print(from_h(input("Input: ")))
            elif "3" in i:
                break

