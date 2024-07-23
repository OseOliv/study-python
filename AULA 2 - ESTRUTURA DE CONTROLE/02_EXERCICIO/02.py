# Crie um programa que mostre na tela todos os
# números pares que estão no intervalo entre 1 e 50.

for c in range(1, 51):
    par = c % 2
    if par == 0:
        print(c)
print("ACABOU O LOOP")


# NUMERO MENOR DE ITERACOES
for n in range(2, 51, 2):
    print(n)
print("ACABOU O LOOP")
