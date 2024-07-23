# FACA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO
# QUALQUER E MOSTRE NA TELA A SUA TABUADA


n = int(input("Digite um numero: "))

# print(f"{n} + 0 =", n + 0)
# print(f"{n} + 1 =", n + 1)
# print(f"{n} + 2 =", n + 2)
# print(f"{n} + 3 =", n + 3)
# print(f"{n} + 4 =", n + 4)
# print(f"{n} + 5 =", n + 5)
# print(f"{n} + 6 =", n + 6)
# print(f"{n} + 7 =", n + 7)
# print(f"{n} + 8 =", n + 8)
# print(f"{n} + 9 =", n + 9)
# print("")
# print("==================")
# print("")
# print(f"{n} - 0 =", n - 0)
# print(f"{n} - 1 =", n - 1)
# print(f"{n} - 2 =", n - 2)
# print(f"{n} - 3 =", n - 3)
# print(f"{n} - 4 =", n - 4)
# print(f"{n} - 5 =", n - 5)
# print(f"{n} - 6 =", n - 6)
# print(f"{n} - 7 =", n - 7)
# print(f"{n} - 8 =", n - 8)
# print(f"{n} - 9 =", n - 9)
# print("")
# print("==================")
# print("")
# print(f"{n} * 0 =", n * 0)
# print(f"{n} * 1 =", n * 1)
# print(f"{n} * 2 =", n * 2)
# print(f"{n} * 3 =", n * 3)
# print(f"{n} * 4 =", n * 4)
# print(f"{n} * 5 =", n * 5)
# print(f"{n} * 6 =", n * 6)
# print(f"{n} * 7 =", n * 7)
# print(f"{n} * 8 =", n * 8)
# print(f"{n} * 9 =", n * 9)
# print("")
# print("==================")
# print("")
# print(f"{n} / 1 = {n / 1:.1f}")
# print(f"{n} / 2 = {n / 2:.1f}")
# print(f"{n} / 3 = {n / 3:.1f}")
# print(f"{n} / 4 = {n / 4:.1f}")
# print(f"{n} / 5 = {n / 5:.1f}")
# print(f"{n} / 6 = {n / 6:.1f}")
# print(f"{n} / 7 = {n / 7:.1f}")
# print(f"{n} / 8 = {n / 8:.1f}")
# print(f"{n} / 9 = {n / 9:.1f}")
# print(f"{n} / 10 = {n / 10:.1f}")


print("Tabuada de Adição:")
for i in range(1, 10):
    print(f"{n} + {i} = {n + i}")

print("\n==================\n")

print("Tabuada de Subtração:")
for i in range(1, 10):
    print(f"{n} - {i} = {n - i}")

print("\n==================\n")

print("Tabuada de Multiplicação:")
for i in range(1, 10):
    print(f"{n} * {i} = {n * i}")

print("\n==================\n")

print("Tabuada de Divisão:")
for i in range(1, 11):
    print(f"{n} / {i} = {n / i:.1f} ")
