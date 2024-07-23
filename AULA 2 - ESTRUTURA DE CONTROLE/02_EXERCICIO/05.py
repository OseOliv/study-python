#  Desenvolva um programa que leia seis números
# inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.

# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite um numero: "))
# num3 = int(input("Digite um numero: "))
# num4 = int(input("Digite um numero: "))
# num5 = int(input("Digite um numero: "))
# num6 = int(input("Digite um numero: "))

# numeros = [num1, num2, num3, num4, num5, num6]
# soma = 0

# for n in numeros:
#     if n % 2 == 0:
#         soma += n
# print(soma)

soma = 0
count = 0

for c in range(1, 7):
    num = int(input("Digite um numero: "))

    if num % 2 == 0:
        soma += num
        count += 1


print("========================")
print(f"O total de numeros pares somados foi: {count}")
print("========================")

print(f"A soma do numero para e: {soma}")
