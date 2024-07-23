# CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL
# QUALQUER PELO TECLADO E MOSTRE SUA PORCAO INTEIRA
# EX: DIGITE UM NUMERO: 6127
# O NUMERO 6.123 TEM A PARTE INTEIRA 6

from math import trunc

num = float(input("Digite um numero: "))

res = trunc(num)

print(f"A porcao inteira de {num} e: {res}")
