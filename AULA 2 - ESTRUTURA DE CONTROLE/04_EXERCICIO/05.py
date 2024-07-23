# Crie um programa que leia o nome e o preço
# de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

somaPrecos = 0
prodMil = 0
quantidade = 0
menorPreco = 0
produtoMaisBarato = ""

while True:
    produtos = str(input("Digite o nome do produto: "))
    preco = int(input("Digite o preco do produto: "))
    quantidade += 1
    somaPrecos += preco

    if preco > 1000:
        prodMil += 1

    if quantidade == 1 or preco < menorPreco:
        menorPreco = preco
        produtoMaisBarato = produtos

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

print(f"O total e: R${somaPrecos}")
print(f"{prodMil} produtos custam mais de R$1000 ")
print(f"{produtoMaisBarato} e o produto mais barato e custa R${menorPreco}")
