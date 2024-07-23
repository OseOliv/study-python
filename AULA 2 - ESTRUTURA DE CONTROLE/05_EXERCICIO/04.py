# Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


num = int(input("Digite um numero: "))
num2 = int(input("Digite mais numero: "))
num3 = int(input("Digite outro numero: "))
num4 = int(input("Digite o ultimo numero: "))

numeros = (num, num2, num3, num4)

vezes9 = numeros.count(9)
print(f"O numero 9 apareceu {vezes9}")

posicao3 = numeros.index(3)
print(f"o valor 3 apareceu primeiro na posicao {posicao3 + 1}")

for par in numeros:
    if par % 2 == 0:
        print(f"O valores pares digitado foram {par}")
