#!/usr/bin/env python3

"""
Calculadora infix

Funcionamento:
[operacao] [n1] [n2]

Operações:
sum, sub, mul, div

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py
operacao: sum
n1: 3
n2: 4
7

O histórico dos resultados ficarão salvos no arquivo `infixcalc.log`
"""

__version__ = "0.2.0"
__author__ = "Rafael"

import sys
import os
import logging
from datetime import datetime

#------------------------------------------------
# Boilerplate
#Create logger
logger = logging.getLogger("infixcalc")
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add formatter to ch
ch.setFormatter(formatter)

# Add ch to logger
logger.addHandler(ch)
#------------------------------------------------

arguments = sys.argv[1:]

if not arguments:
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos!")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum","sub","mul","div")
if operation not in valid_operations:
    print("Operação inválida!")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

match operation:
    case "sum":
        result = n1 + n2
    case "sub":
        result = n1 - n2
    case "mul":
        result = n1 * n2
    case "div":
        result = n1 / n2

path = '/'
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")



print(f"O resultado da operação {operation} é {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} / {user} -> {operation},{n1},{n2} = {result}\n")
except PermissionError as e:
    logger.error("You don't have permission to write in this folder/file\n %s",str(e))
    sys.exit(1)


