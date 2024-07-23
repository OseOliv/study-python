#  Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

nums = [n1, n2, n3]

maior = max(nums)
menor = min(nums)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
