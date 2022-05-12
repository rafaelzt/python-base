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
    valid_operations = ("sum", "sub", "mul", "div") 

    if not args:
        operation = args.append(input("Digite uma operação: "))
        n1 = args.append(int(input("Digite um numero [n1]: ")))
        n2 = args.append(int(input("Digite um numero [n2]: ")))
    elif len(args) != 3:
        print("Numero de argumentos invalidos")
        print("ex: `sum 5 5`")
        sys.exit(1)

    operation, n1, n2 = args

    if operation not in valid_operations:
        print("Operacao invalida")
        print(valid_operations)
        sys.exit(1)
    else:
        calcula(operation, int(n1), int(n2))


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

    sys.exit(0)

if __name__ == "__main__":
    main()
