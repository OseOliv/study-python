# DESAFIO  onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.


import random

num = random.randint(0, 10)
count = 1

print("Acabei de pensar em um numero entre 0 e 10")
print("Sera que voce consegue adivinha qual foi?")

user = int(input("Qual e o seu palpite? "))

while user != num:
    count += 1
    if user > num:
        user = int(input("O numero e menor. De outro palpite: "))
    elif user < num:
        user = int(input("O numero e maior. De outro palpite: "))

print(f"Voce acertou!\n Palpite do computador: {
      num}\n Palpite do Usuario: {user}\n Voce tentou {count} vezes ate acertar")
