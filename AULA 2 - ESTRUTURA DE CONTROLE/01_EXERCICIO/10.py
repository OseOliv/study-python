#  Crie um programa que faça o computador jogar Jokenpô com você.

import random

print(
    """
OPCOES:
PEDRA
PAPEL
TESOURA

          
""")

opcoes = ["Pedra", "Papel", "Tesoura"]

computador = random.choice(opcoes).lower()

jogador = input("Escolha um opcao: ").lower()


print(f"O Computador escolheu {computador}")
print(f"O Jogador escolheu {jogador}")

if computador == jogador:
    print("EMPATOU!!!")
elif (jogador == "papel" and computador == "pedra") or \
     (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "tesoura" and computador == "papel"):
    print("O Jogador GANHOU!")
else:
    print("O Computador GANHOU!")
