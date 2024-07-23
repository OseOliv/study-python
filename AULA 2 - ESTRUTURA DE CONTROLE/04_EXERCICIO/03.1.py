# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que
# ele conquistou no final do jogo.

from random import randint

v = 0

while True:
    jogador = int(input("Digite um numero: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou impar [P/I]")).strip().upper()[0]
    print(f"Voce jogou {jogador} e computador {computador}. Total de {total}")
    if tipo == "P":
        if total % 2 == 0:
            print("JOGADOR GANHOU!")
            v += 1
        else:
            print("COMPUTADOR GANHOU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("JOGADOR GANHOU!")
            v += 1
        else:
            print("COMPUTADOR GANHOU!")
            break
    print("Vamos jogar novamente...")

print(f"Voce venceu {v} vezes seguidas!")
