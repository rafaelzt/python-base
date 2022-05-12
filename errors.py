#!/usr/bin/env python3


import sys

# EAFP - Easy to Ask Forgiveness than permission
# É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines() # FileNotFoundError
    1 / 0 # ZeroDivisionError
    print(names.banana) # AttributeError
except FileNotFoundError:
    print(f"[Err] File names.txt not found.")
    sys.exit(1)
except ZeroDivisionError:
    print(f"[Err] You can not divide by zero")
    sys.exit(2)
except AttributeError:
    print(f"Attribute does not exists!")
    sys.exit(3)

try:
    print(names[3])
except: # Bare except
    print("[Error] Missing name in the list")
    sys.exit(4)
