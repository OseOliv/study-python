# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.

# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("="*30)
print("^^^^^^^ CAIXA BANCO ^^^^^^")
print("="*30)

# Solicita ao usuário que insira o valor que deseja sacar e converte para inteiro
valor = int(input("Que valor você quer sacar? R$"))

# Inicializa a variável total com o valor solicitado pelo usuário
total = valor

# Define o valor da cédula inicial como R$50
ced = 50
# Inicializa a contagem de cédulas como 0
totalced = 0

# Inicia um loop infinito que só será interrompido por um comando break
while True:
    # Se o total restante for maior ou igual ao valor da cédula atual
    if total >= ced:
        # Subtrai o valor da cédula do total
        total -= ced
        # Incrementa a contagem de cédulas do valor atual
        totalced += 1
    else:
        # Se houver cédulas contadas para o valor atual, imprime a quantidade
        if totalced > 0:
            print(f"O total de {totalced} cédula(s) de R${ced}")
        # Muda o valor da cédula para a próxima denominação menor
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        # Reseta a contagem de cédulas para o novo valor de cédula
        totalced = 0
        # Se o total restante for 0, termina o loop
        if total == 0:
            break
