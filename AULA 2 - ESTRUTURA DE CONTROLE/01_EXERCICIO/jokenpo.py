import random

print("""
ESCOLHA:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
      """)

opcao = ["Pedra", "Papel", "Tesoura"]

computador = random.randint(0, 2)

jogador = int(input("Qual a sua jogada? "))

jogadaJogador = opcao[jogador]

jogadaComputador = opcao[computador]

print(f"O Jogador escolheu {jogadaJogador}")
print(f"O Computador escolheu {jogadaComputador}")
print("=====================================")


if computador == 0:  # PEDRA
    if jogador == 0:  # PEDRA
        print("EMPATE!!!")
    elif jogador == 1:  # PAPEL
        print("JOGADOR VENCEU!")
    elif jogador == 2:  # TESOURA
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADA INVALIDA!!")
elif computador == 1:  # PAPEL
    if jogador == 0:  # PEDRA
        print("COMPUTADOR VENCEU")
    elif jogador == 1:  # PAPEL
        print("EMPATE!!!")
    elif jogador == 2:  # TESOURA
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVALIDA!!")
elif computador == 2:  # TESOURA
    if jogador == 0:  # PEDRA
        print("JOGADOR VENCEU")
    elif jogador == 1:  # PAPEL
        print("COMPUTADOR VENCEU")
    elif jogador == 2:  # TESOURA
        print("EMPATE!!!")
    else:
        print("JOGADA INVALIDA!!")
print("=====================================")
