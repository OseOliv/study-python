# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre elas (desconsiderando o flag).


countDig = 0
soma = 0

while True:
    num = int(input("Digite um numero (digite 999 para parar): "))
    if num == 999:
        break
    soma += num
    countDig += 1

print(f"A soma dos {countDig} digitados e: {soma}")
