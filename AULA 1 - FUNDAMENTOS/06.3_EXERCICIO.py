# Crie um programa que leia um número inteiro e
# mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um numero: "))

if num % 2 == 1:
    print(f"O numero {num} e IMPAR!")
else:
    print(f"O numero {num} e PAR!")
