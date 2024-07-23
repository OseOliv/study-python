# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a
# base de conversão:
# 1 para binário,
# 2 para octal,
# 3 para hexadecimal.

num = int(input("Digite um numero: "))
base = int(input("Escolha  a base de conversao ente 1 e 3: "))


if base == 1:
    numBin = bin(num)  # bin(num)[2:]  # Remove o prefixo
    print(f"O numero binario de {num} e: {numBin}")

elif base == 2:
    numOct = oct(num)  # oct(num)[2:]  # Remove o prefixo '0o'
    print(f"O numero Octadecimal de {num} e: {numOct}")
elif base == 3:
    numHex = hex(num)  # hex(num)[2:]  # Remove o prefixo '0x'
    print(f"O numero Hexdecimal de {num} e: {numHex}")
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
