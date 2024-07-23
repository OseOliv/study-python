# Crie um programa que leia o ano de nascimento
# de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e
# quantas já são maiores.

from datetime import datetime

anoAtual = datetime.today().year
countMaior = 0
countMenor = 0

for n in range(1, 8):

    anoNasc = int(input(f"E que ano a {n}ª pessoa nasceu? "))
    idade = anoAtual - anoNasc

    if idade >= 18:
        print("E MAIOR DE IDADE!")
        countMaior += 1
    else:
        print("E MENOR DE IDADE!")
        countMenor += 1
print(f"O numero de maior de idade e: {countMaior}")
print(f"O numero de menor de idade e: {countMenor}")
