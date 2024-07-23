# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também
# deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNascimento = int(input("Digite o ano de nascimento: "))

anoAtual = date.today().year

idade = anoAtual - anoNascimento

tempoFaltaAlistar = 18 - idade

tempoPassouAlistar = idade - 18

if idade < 18:
    print("Ainda vai se Alistar")
    print(f"O tempo que falta para se alistar e: {tempoFaltaAlistar} anos")
elif idade == 18:
    print("Esta na hora certa de se Alistar")
elif idade > 18:
    print("Ja Passou da hora de se Alistar")
    print(f"O tempo que passeou para se alista e de: {
          tempoPassouAlistar} anos")
