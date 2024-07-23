num = int(input("Digite um número para calcular o seu fatorial: "))
con = num
fac = 1
print(f"O fatorial de {num}! = ", end="")
while con > 0:
    print(f"{con}", end="")
    print(" x " if con > 1 else " = ", end="")
    fac = fac * con
    con -= 1
print(f"{fac}")
