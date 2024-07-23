# Faça um programa que leia o peso de
# cinco pessoas. No final, mostre qual
# foi o maior e o menor peso lidos.

# maior_peso = float('-inf')
# menor_peso = float('inf')

# for p in range(1, 6):
#     peso = float(input(f"Digite o peso da {p}ª Pessoa: "))

#     if peso >= maior_peso:
#         maior_peso = peso

#     if peso < menor_peso:
#         menor_peso = peso

# print(menor_peso)
# print(maior_peso)


maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª Pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi {maior}")
print(f"O menor peso lido foi {menor}")
