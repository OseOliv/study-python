

print("Oi"*5)
print("="*20)

print("")
print("==================")
print("")

name = input("Qual o seu nome? ")
print(f"Prazer em te conhecer {name:20}!")
print(f"Prazer em te conhecer {name:>20}!")
print(f"Prazer em te conhecer {name:<20}!")
print(f"Prazer em te conhecer {name:^20}!")
print(f"Prazer em te conhecer {name:=^20}!")

print("")
print("==================")
print("")

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f"A soma vale {s}")
print(f"A multiplicacao vale {m}")
print(f"A divisao vale {d:.3f}")
print(f"A divisao inteira vale {di}")
print(f"A potencia vale {e}")
