
# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo,
# desconsiderando os espaços.


frase = str(input("Digite uma frase: ")).lower()

# fraseArr = frase.split()

# frasef = "".join(fraseArr)

# for n in fraseArr:
#     if frasef[0] == frasef[-1]:
#         print("E UM PALINDROMO")
#         break
#     else:
#         print("NAO E UMA PALINDROMO")
#         break

print("===================================================")

# Os espaços são removidos utilizando o método split()
# para dividir a frase em palavras e join() para juntá-las sem espaços.
novaFrase = "".join(frase.split())


if novaFrase == novaFrase[::-1]:
    print("É UM PALÍNDROMO")
else:
    print("NÃO É UM PALÍNDROMO")
