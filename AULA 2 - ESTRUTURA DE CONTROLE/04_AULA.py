# LACOS DE REPETICAO
# INTERROMPER LACOS
# BREAK

# cont = 1

# while cont <= 10:
#     print(cont, " -> ", end="")
#     cont += 1
# print("Acabou!")

n = 0
soma = 0

while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    soma += n
print(f"A soma vale {soma}")
