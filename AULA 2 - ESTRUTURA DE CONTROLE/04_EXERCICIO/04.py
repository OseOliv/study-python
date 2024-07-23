# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


count18 = 0
countM = 0
count20 = 0

while True:
    print("-"*20)
    print("CASDASTRAR PESSOA")
    print("-"*20)
    idade = int(input("Digite a idade: "))
    sexo = str(input("Sigite o sexo [M/F] ")).strip().upper()[0]

    if idade > 18:
        count18 += 1
        if sexo == "M":
            countM += 1
    elif idade < 20 and sexo == "F":
        count20 += 1
    continuar = str(input(("Deseja continuar? [S/N] "))).strip().upper()[0]
    if continuar != "S":
        break

print("-"*20)
print(f"{count18} pessoas tem mais de 18 anos!")
print("-"*20)
print(f"{countM} homens foram cadastrados!")
print("-"*20)
print(f"{count20} mulheres menores de 20 anos foram cadastradas!")
