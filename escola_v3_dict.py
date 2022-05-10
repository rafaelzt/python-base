#!/usr/bin/env python

"""Print report students per activity

Print a list of students grouped by class and activities.
"""
__version__ = "0.1.22"

# Dados
sala1 = ["Erik","Maia","Gustavo","Manuel","Sofia","Joana"]
sala2 = ["Joao","Antonio","Carlos","Maria","Isolda"]

atividades = {
    "ingles": ["Erik","Maia","Joana","Carlos","Antonio"],
    "musica": ["Erik","Carlos","Maria"],
    "danca": ["Gustavo","Sofia","Joana","Antonio"]
}

# Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades.items():
    print(nome_atividade)
    print(f"Sala 1 -> {set(sala1).intersection(atividade)}")
    print(f"Sala 2 -> {set(sala2).intersection(atividade)}")
    print("")
        
