# Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.


# num = int(input("Digite um numero inteiro: "))


# if num <= 1:
#     print(f"{num} NAO E NUMERO PRIMO")
# elif num == 2:
#     print(f"{num} E NUMERO PRIMO")
# elif num > 2 and num % 2 == 0:
#     print(f"{num} NAO E NUMERO PRIMO")
# else:
#     print(f"{num} E NUMERO PRIMO")


num = int(input("Digite um numero inteiro: "))

if num <= 1:
    print(f"{num} NAO E NUMERO PRIMO")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} E NUMERO PRIMO")
    else:
        print(f"{num} NAO E NUMERO PRIMO")
