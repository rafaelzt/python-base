#!/usr/bin/env python3


import sys

# EAFP - Easy to Ask Forgiveness than permission
# É mais fácil pedir perdão do que permissão)

try:
    raise RuntimeError
except RuntimeError:
    print("Generic Error")


try:
    names = open("names.txt").readlines() # FileNotFoundError

except FileNotFoundError as e:
    print(f"{str(e)}")

    sys.exit(1)
    # TODO: Usar retry
else:
    print("Success!")
finally:
    print("Always execute this!")

try:
    print(names[3])

except: # Bare except
    print("[Error] Missing name in the list")
    sys.exit(4)
