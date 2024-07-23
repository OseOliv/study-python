# Faça um programa que calcule a soma entre
# todos os números impares que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.

total = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        total = total + 1
        soma += n

print(soma)
print(total)
