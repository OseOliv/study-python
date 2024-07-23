# Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os
# 10 primeiros termos dessa progressão.


a = int(input("Digite um numero: "))
r = int(input("Digite a razao: "))

for c in range(10):
    termo = a + (c * r)
    print(termo)
print("ACABOU")
