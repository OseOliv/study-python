# Faça um programa que leia um ano qualquer
# e mostre se ele é bissexto.

ano = int(input("Digite um ano por completo: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano {ano} e bisexto.")
else:
    print(f"O ano {ano} nao e bisexto")
