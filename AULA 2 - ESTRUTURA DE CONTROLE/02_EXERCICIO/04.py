# Refaça o DESAFIO 009, mostrando a tabuada de
# um número que o usuário escolher, só que agora
# utilizando um laço for.

num = int(input("Digite um numero: "))

print("== MULTIPLICACAO ==")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("")

print("== DIVISAO ==")
for i in range(1, 10):
    print(f"{num} / {i} = {num / i:.2f}")
print("")

print("== ADICAO==")
for i in range(1, 11):
    print(f"{num} + {i} = {num + i}")
print("")

print("== SUBTRACAO ==")
for i in range(1, 10):
    print(f"{num} - {i} =  {num - i}")
