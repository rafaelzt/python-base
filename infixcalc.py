#!/usr/bin/env python3

""" Calculadora infix

Funcionamento:
[operacao] [n1] [n2]

Operacoes:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operacao: sum
n1: 5
n2: 4
9
"""

__author__ = "Rafael Tanganelli"
__version__ = "0.0.1"
__license__ = "Unlicense"

import sys

def main():
    args = sys.argv[1:]
    if len(args) != 3:
        args.append(input("Digite uma operação: "))
        args.append(int(input("Digite um numero [n1]: ")))
        args.append(int(input("Digite um numero [n2]: ")))
    else:
        args[0] = (args[0])
        args[1] = (int(args[1]))
        args[2] = (int(args[2]))
    calcula(args[0],args[1],args[2])




def calcula(operacao, n1, n2):
    match operacao:
        case "sum": 
            print(n1+n2)
        case "sub" :
            print(n1-n2)
        case "mul":
            print(n1*n2)
        case "div":
            print(n1/n2)
        case default:
            print("Invalid data!")

if __name__ == "__main__":
    main()
