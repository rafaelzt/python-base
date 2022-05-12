#!/usr/bin/env python3

""" Bloco de Notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Qualquer texto

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read","new")
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # leitura das notas
    with open("notes.txt", "r") as file_:
        if len(arguments) == 1:
            print(file_.read())
        else:
            for line in file_:
                selected_tag = (line.split("-")[0]).strip()
                if selected_tag == arguments[1].split("=")[1]:
                    print(line.replace("\n",""))

if arguments[0] == "new":
    # criacao da  nota
    tag = input("tag: ")
    text = input("text: \n") 
    open("notes.txt", "a").write(f"{tag} -> {text}\n")

