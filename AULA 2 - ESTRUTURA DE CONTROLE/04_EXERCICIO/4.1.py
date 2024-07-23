# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


# Inicializa os contadores para as três categorias que serão rastreadas
count18 = 0  # Contador para pessoas com mais de 18 anos
countM = 0   # Contador para homens cadastrados
count20 = 0  # Contador para mulheres com menos de 20 anos

# Loop principal do programa
while True:
    # Solicita e lê a idade da pessoa
    idade = int(input("Digite a idade: "))

    # Inicializa a variável sexo com um espaço vazio
    sexo = " "

    # Loop para garantir que a entrada do sexo seja válida
    while sexo not in "MF":
        sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

    # Atualiza os contadores com base na idade e sexo
    if idade >= 18:
        count18 += 1
    if sexo == "M":
        countM += 1
    if sexo == "F" and idade < 20:
        count20 += 1

    # Inicializa a variável continuar com um espaço vazio
    continuar = " "

    # Loop para garantir que a entrada para continuar seja válida
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]

    # Se o usuário escolher "N", o loop principal é interrompido
    if continuar == "N":
        break

# Exibe os resultados finais
print("-" * 20)
print(f"{count18} pessoas têm mais de 18 anos!")
print("-" * 20)
print(f"{countM} homens foram cadastrados!")
print("-" * 20)
print(f"{count20} mulheres menores de 20 anos foram cadastradas!")
