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

# Listar alunos em cada atividade por sala
atividades = [
                ("Inglês",aula_ingles),
                ("Música", aula_musica),
                ("Dança", aula_danca),
            ]

for nome, atividade in atividades:

    atividade_sala_1 = []
    atividade_sala_2 = []

    print(nome)

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala_1.append(aluno)
        elif aluno in sala2:
            atividade_sala_2.append(aluno)

    print('Sala 1 ---> ', atividade_sala_1)
    print('Sala 2 ---> ', atividade_sala_2)

