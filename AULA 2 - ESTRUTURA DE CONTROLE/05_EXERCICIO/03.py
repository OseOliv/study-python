# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na tupla.

from random import randint

nums = []

for _ in range(5):
    nums.append(randint(0, 10))
nums = tuple(nums)

numsorted = sorted(nums)

print(f"Os numeros sorteados sao: {nums}")

print(f"O maior numero e {numsorted[-1]}")
print(f"O menor numero e {numsorted[0]}")
