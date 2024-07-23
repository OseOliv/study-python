# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.

# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


while True:

    sacar = int(input("Digite o valor que deseja sacar: R$ "))

    cinquenta = 0
    vinte = 0
    dez = 0
    um = 0

    if sacar == 0:
        print("Saindo do programa")
        break

    cinquenta = sacar // 50
    sacar = sacar % 50

    vinte = sacar // 20
    sacar = sacar % 20

    dez = sacar // 10
    sacar = sacar % 20

    um = sacar // 1
    sacar % 1

    print(f"Serão entregues:")
    print(f"{cinquenta} cédulas de R$50")
    print(f"{vinte} cédulas de R$20")
    print(f"{dez} cédulas de R$10")
    print(f"{um} cédulas de R$1")
    break
