# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

name = input("Digite o nome completo: ").strip()

nmai = name.upper()
nmin = name.lower()
nlen = len(name)
nspl = name.split()
npri = len(nspl[0])

print(nmai)
print(nmin)
print(nlen)
print(npri)
