#!/usr/bin/env python

"""Print report students per activity

Print a list of students grouped by class and activities.
"""
__version__ = "0.1.0"

# Dados
sala1 = ["Erik","Maia","Gustavo","Manuel","Sofia","Joana"]
sala2 = ["Joao","Antonio","Carlos","Maria","Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo","Sofia","Joana","Antonio"]

atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança", aula_danca)]
# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:
    print(nome_atividade)
    print(f"Sala 1 -> {set(sala1).intersection(atividade)}")
    print(f"Sala 2 -> {set(sala2).intersection(atividade)}")
    print("")
        
