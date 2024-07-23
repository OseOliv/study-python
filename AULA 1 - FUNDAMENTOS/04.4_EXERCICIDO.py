# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS
# PARA APAGAR O QUADRO. FACA UM PROGRAMA QUE AJUDA ELE.
# LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.

from random import choice

a1 = input("Digite o nome do primero aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")

alunos = [a1, a2, a3, a4]

alsort = choice(alunos)

print(alsort)
