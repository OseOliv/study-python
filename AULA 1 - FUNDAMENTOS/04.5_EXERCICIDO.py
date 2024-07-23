# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR
# A ORDEM DE APRESENTACAO DE TRABALHOS DOS ALUNOS.
# FACA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS
# E MOSTRE A ORDEM SORTEADA.


from random import shuffle

a1 = input("Digite o nome do primero aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")

alunos = [a1, a2, a3, a4]

print(f"A ordem sorteado dos aluno: {alunos} foi: ")

shuffle(alunos)


for i, aluno in enumerate(alunos, start=1):
    print(f"{i} - {aluno}")
