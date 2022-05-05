#!/usr/bin/env python

"""Imprime a tabuada do 1 ao 10

Tabuada do 1
1
2
3
...
----
Tabuada do 2
1
2
3
...
"""

__version__ = "0.1.0"
__author__ = "Rafael"

# numero = [1,2,3,4,5,6,7,8,9,10]

numeros = list(range(1,11))

# Iterable
for numero in numeros:
    print(f"Tabuada do {numero}")
    for outro_numero in numeros:
        print(f"{numero} X {outro_numero} = {numero*outro_numero}")
#       print(numero.__mul__(outro_numero))

    print("-"*20)
