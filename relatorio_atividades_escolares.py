#! /usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que
frequentam cada uma das atividades. 

//Exercício usando listas,tuplas, loops e condicionais
"""
__version__ = "0.1.0"

#Dados
sala1 = ["Caio", "Carlos", "Priscila", "Thais", "Juliana"]
sala2 = ["Sabrina", "Raquel", "Gabriel", "Marco", "Cauã"]

aula_natacao = ["Cauã", "Juliana", "Thais", "Carlos", "Marco"]
aula_musculacao = ["Caio", "Sabrina", "Raquel", "Priscila", "Gabriel"]
aula_danca = ["Sabrina", "Priscila", "Thais"]

atividades = [
    ("Natação", aula_natacao), 
    ("Música", aula_musculacao), 
    ("Dança", aula_danca)
]

#Otimizando a iteração do código /Listando alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print()
    print(f"Alunos da atividade {nome_atividade}!\n")
    print("-" * 5)

    atividade_sala1 = []
    atividade_sala2 = []

    for alunos in atividade:
        if alunos in sala1:
            atividade_sala1.append(alunos)
        elif alunos in sala2:
            atividade_sala2.append(alunos)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("────୨ৎ────" * 5)

#print("Listando alunos em cada atividade por sala!")

#aula_natacao_sala1 = []
#aula_natacao_sala2 = []

#for alunos in aula_natacao:
#    print(alunos)

#print("--------------------------------------------------------")    

#Adicionando os alunos das salas 1 e 2 na aula de natação
#aula_natacao_sala1 = []
#aula_natacao_sala2 = []


#print("Adicionando os alunos das salas 1 e 2 na aula de natação!")

#for alunos in aula_natacao:
#    if alunos in sala1:
#        aula_natacao_sala1.append(alunos)
#    elif alunos in sala2:
#        aula_natacao_sala2.append(alunos)

#print("Aula natação1 ", aula_natacao_sala1)
#print("Aula natação2 ", aula_natacao_sala2)

    
