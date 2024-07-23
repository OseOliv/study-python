# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.


valorCasa = float(input("Qual o valor da casa? "))
salarioComprador = float(input("Qual o salario do comprador? "))
anosParaPagar = float(input("Quantos anos ele vai pagar? "))

salario30 = salarioComprador * 0.30

parcelas = anosParaPagar * 12

valorPagarMes = valorCasa / parcelas

if valorPagarMes > salario30:
    print("O emprestimo foi negado!")
else:
    print("O emprestimo foi aprovado!")

print(f"O valor de 30% do salario: {salario30:.2f}")
print(f"O numero de parcelas: {parcelas:.0f}")
print(f"O valor a ser pago todo mes {valorPagarMes:.2f}")
