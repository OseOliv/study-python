# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print(f"O primeiro numero {num1} e maior que o segundo numero {num2}")
elif num2 > num1:
    print(f"O segundo numero {num2} e maior que o primeiro numero {num1}")
else:
    print("Não existe valor maior, os dois são iguais")
