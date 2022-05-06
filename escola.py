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
lista_classes = [aula_ingles, aula_musica, aula_danca]
lista_classes_txt = ["Aula de Inglês","Aula de Música","Aula de Dança"]

for classe in range(len(lista_classes)):

    alunos_sala_1 = []
    alunos_sala_2 = []
    aluno_ausentes = []

    print("-->",lista_classes_txt[classe])

    for aluno in lista_classes[classe]:
        if aluno in sala1:
            alunos_sala_1.append(aluno)
        elif aluno in sala2:
            alunos_sala_2.append(aluno)

    print('Sala 1 ---> ', alunos_sala_1)
    print('Sala 2 --->', alunos_sala_2)

