# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

while True:

    print("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
""")
    opcao = int(input("Escolha uma opcao do menu: "))

    if opcao == 1:
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} e: {soma}")
        print("\n" + "-" * 30)
        sleep(1.5)

    elif opcao == 2:
        multi = num1 * num2
        print(f"A multiplicacao de {num1} e {num2} e: {multi}")
        print("\n" + "-" * 30)
        sleep(1.5)

    elif opcao == 3:
        maior = max(num1, num2)
        print(f"O maior numero entre {num1} e {num2} e: {maior}")
        print("\n" + "-" * 30)
        sleep(1.5)

    elif opcao == 4:
        sleep(1.5)
        num1 = int(input("Digite um novo numero: "))
        num2 = int(input("Digite outro novo numero: "))
        print("\n" + "-" * 30)

    elif opcao == 5:
        print("\n" + "-" * 30)
        print("Saindo do programa...")
        sleep(1.5)

        break

    else:
        print("Opcao invalida, tente novamente!")
        print("\n" + "-" * 30)
        continue

print("\n" + "-" * 30)
print("Obrigado volte sempre!")
print("\n" + "-" * 30)
