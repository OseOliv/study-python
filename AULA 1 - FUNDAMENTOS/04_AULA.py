# UTILIZANDO METODOS


from math import sqrt, ceil, floor
import math


# import math

num = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

raiz = math.sqrt(num)

print(f"A raiz de {num} e igual a {math.ceil(raiz)}")
print(f"A raiz de {num} e igual a {math.floor(raiz)}")
print(f"A raiz de {num} e igual a {raiz:.2f}")

print("")
print("==================")
print("")

# from math import sqrt, ceil, floor

raiz2 = sqrt(num)

print(f"A raiz de {num2} e igual a {ceil(raiz)}")
print(f"A raiz de {num2} e igual a {floor(raiz)}")
print(f"A raiz de {num2} e igual a {raiz:.2f}")

print("")
print("==================")
print("")
