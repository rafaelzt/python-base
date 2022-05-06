#!/usr/bin/env python

from colorama import Fore, Back, Style

"""Print a table with multiplication from 1 to 10

How to use:


Execution:

Result:
--- Tabuada do # ---
      1 x 1 = 1
      1 x 2 = 2
      1 x 3 = 3
        ...
....................
"""

for n1 in range(1, 11):
    print(f"{Fore.WHITE}{Back.RED}{' Tabuada do ' + str(n1) + ' '  :-^25}{Style.RESET_ALL}")
    for n2 in range(1, 11):
        resultado = n1 * n2
        print(
            f"{Fore.BLUE}{n1 : < 5} X {n2 : ^7} = {resultado : ^10}{Style.RESET_ALL}")
    print("\n")
