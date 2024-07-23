# Crie um programa que leia o nome de uma
# pessoa e diga se ela tem "SILVA" no nome.


name = input("Digite seu nome completo: ").lower().strip()

namesilva = "silva" in name

print(f"Seu nome tem Silva? {namesilva}")
