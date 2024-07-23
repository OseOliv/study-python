# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

name = input("Digite seu nome completo: ")  # Digita o nome

nomes = name.split()  # Tranforma o nome em Array
# Sinaliza o ultimo indice do array, que e o tamnho do array - 1
ultnome = len(nomes)-1

print(nomes)


print(f"O primeiro nome e: {nomes[0]}")  # print no nome no indico 0 (primeiro)
print(f"O ultimo nome e: {nomes[ultnome]}")  # print o indice do ultimo array
