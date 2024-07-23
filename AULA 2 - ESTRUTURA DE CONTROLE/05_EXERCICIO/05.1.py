# Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

listagem = ("Lapis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livros", 34.90)

print("-" * 40)  # Imprime uma linha de 40 caracteres "-"
# Imprime o título centralizado em uma linha de 40 caracteres
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)  # Imprime outra linha de 40 caracteres "-"

# Loop para iterar sobre os elementos da tupla listagem
for pos in range(0, len(listagem)):
    if pos % 2 == 0:  # Verifica se a posição é par (nome do produto)
        # Imprime o nome do produto alinhado à esquerda em 30 caracteres seguido de pontos (.)
        print(f"{listagem[pos]:.<30}", end="")
    else:  # Caso contrário (preço do produto)
        # Imprime o preço do produto alinhado à direita em 7 caracteres, com duas casas decimais e precedido por "R$"
        print(f"R${listagem[pos]:>7.2f}")

print("-" * 40)  # Imprime outra linha de 40 caracteres "-"
