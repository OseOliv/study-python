# Escreva um programa que pergunte o salário de um
# funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule
# um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.


salario = float(input("Digite o seu salario: R$ "))

aum = salario * 0.10
aum2 = salario * 0.15

if salario >= 1250:
    salarioTotal = salario + aum
    print(f"O salario superior com 10% fica: R${salarioTotal:.2f}")
else:
    salarioTotal = salario + aum2
    print(f"O salario inferior com 15% fica: R${salarioTotal:.2f}")
