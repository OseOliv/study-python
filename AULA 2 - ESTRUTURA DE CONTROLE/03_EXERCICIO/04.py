#  Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120


#     print(resultado)


# Solicita ao usuário que digite um número e o converte para um inteiro
num = int(input("Digite um número para calcular o seu fatorial: "))

# Verifica se o número é 0 ou 1, casos especiais cujo fatorial é 1
if num == 0 or num == 1:
    # Se o número for 0 ou 1, imprime diretamente que o fatorial é 1
    print(f"O fatorial de {num} é 1")
else:
    # Inicializa a variável contador com o valor de num
    contador = num
    # Inicializa a variável fatorial com 1, que armazenará o resultado do fatorial
    fatorial = 1
    # Inicializa a string resultado com a representação inicial do fatorial
    resultado = f"{num}! = "

    # Calcula o fatorial usando um loop while
    while contador > 0:
        # Multiplica o valor atual de fatorial pelo valor de contador
        fatorial *= contador
        # Verifica se o contador é igual a 1
        if contador == 1:
            # Se for o último número (1), adiciona à string resultado a última parte da multiplicação e o resultado final
            resultado += f"{contador} = {fatorial}"
        else:
            # Caso contrário, adiciona à string resultado o valor atual de contador seguido de " x "
            resultado += f"{contador} x "
        # Decrementa o valor de contador em 1
        contador -= 1

    # Após o loop, imprime a string resultado, que mostra toda a sequência de multiplicações e o resultado final
    print(resultado)
