# A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

anoNascimento = int(input("Digite o ano: "))

anoAtual = date.today().year

idade = anoAtual - anoNascimento

print(f"A idade do atleta e: {idade}")

if idade <= 9:

    print("A Categoria e: MIRIM")
elif idade <= 14:

    print("A Categoria: INFANTIL")
elif idade <= 19:

    print("A Categoria: JÚNIOR")
elif idade <= 25:

    print("A Categoria: SÊNIOR")
else:

    print("A Categoria: MASTER")
