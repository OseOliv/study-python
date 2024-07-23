# Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o
# nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.

media = 0
IdadeMaisVelho = 0
nomeMaisVelho = ""
countMulher = 0

for p in range(1, 5):
    nome = str(input("Digite o nome: "))
    sexo = str(input("Digite o sexo (M)/(F): "))
    idade = int(input("Digite o idade: "))

    # SOMAR TODAS AS IDADES E ARMAZENAR NA MEDIA
    if idade > 0:
        media += idade
        # ACHAR A MAIOR IDADE E ACHAR O NOME DO HOMEM MAIS VELHO
        if sexo == "M" and idade > IdadeMaisVelho:
            IdadeMaisVelho = idade
            nomeMaisVelho = nome
        # ACHAR QUANTAS FEMALE TEM IDADE MENOR QUE 20
        if sexo == "F" and idade < 20:
            countMulher += 1


print(f"A media de idade e: {media/4} anos")
print(f"O homem mais velhor e {nomeMaisVelho} e tem {IdadeMaisVelho} anos")
print(f"O numero de mulheres abaixo de 20 anos e {countMulher}")
