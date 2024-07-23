# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

import random
from time import sleep

num = random.randint(0, 5)

user = int(input("Digite um numero de 0 a 5. "))
print("PROCESSANDO...")
sleep(3)
if num == user:
    print("O usuario ganhou!")
else:
    print("O usuario perdeu!")

print(f"Numero aleatorio {num}")
print(f"Numero usuario {user}")
