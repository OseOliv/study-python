# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que
# ele conquistou no final do jogo.

from random import randint

totalVitorias = 0

while True:
    escolha = str(input("Escolha par ou impar [P/I]: ")).upper().strip()
    numJog = int(input("Digite um numero [entre 0 e 10]: "))
    numComp = randint(0, 10)

    print("-="*10)

    soma = numJog + numComp
    par = soma % 2 == 0
    impar = soma % 2 == 1
    print(f"O compuador escolhueu {numComp} e a soma dos numeros foi: {soma}")
    print("-="*10)

    if par == True and escolha == "P":
        print("O JOGADOR GANHOU!")
        totalVitorias += 1
    elif impar == True and escolha == "I":
        print("O JOGADOR GANHOU!")
        totalVitorias += 1
    else:
        print("O COMPUTADOR GANHOU!")
        break
    print("-="*10)
    print("Vamos jogar novamente...")

print(f"O jogador ganhou {totalVitorias} vezes. ")
