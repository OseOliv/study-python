# Crie um programa que leia o nome e o preço
# de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.


somaPrecos = 0  # Variável para armazenar o total gasto na compra
prodMil = 0     # Variável para contar quantos produtos custam mais de R$1000
quantidade = 0  # Variável para contar a quantidade total de produtos inseridos
menorPreco = 0  # Variável para armazenar o menor preço encontrado até o momento
produtoMaisBarato = ""  # Variável para armazenar o nome do produto mais barato

while True:
    # Solicita ao usuário o nome do produto
    produtos = str(input("Digite o nome do produto: "))
    # Solicita ao usuário o preço do produto
    preco = int(input("Digite o preco do produto: "))
    quantidade += 1  # Incrementa a quantidade total de produtos inseridos
    somaPrecos += preco  # Adiciona o preço do produto ao total gasto na compra

    if preco > 1000:
        prodMil += 1  # Incrementa o contador de produtos que custam mais de R$1000

    if quantidade == 1 or preco < menorPreco:
        # Atualiza o menor preço encontrado se for o primeiro produto ou se for menor que o atual
        menorPreco = preco
        produtoMaisBarato = produtos  # Atualiza o nome do produto mais barato encontrado

    continuar = " "
    while continuar not in "SN":
        # Pergunta se o usuário quer continuar
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break  # Se o usuário digitar 'N', sai do loop

# Após sair do loop, exibe as informações coletadas
print(f"O total gasto é: R${somaPrecos}")
print(f"{prodMil} produtos custam mais de R$1000")
print(f"{produtoMaisBarato} é o produto mais barato e custa R${menorPreco}")
