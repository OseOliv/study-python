# Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


num = (int(input("Digite um numero: ")), int(input("Digite mais numero: ")),
       int(input("Digite outro numero: ")), int(input("Digite o ultimo numero: ")))

print(f"Voce digitou os valores {num}")

print(f"O valor 9 apareceu {num.count(9)} vezes")

if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1} posicao")
else:
    print("O valor 3 nao foi digitado em nenhuma posicao.")

print(f"Os valores pares digitados foram ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
