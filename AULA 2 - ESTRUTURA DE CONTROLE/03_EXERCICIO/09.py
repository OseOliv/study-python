# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

# Inicializa a variável 'resp' com "S" para entrar no loop
resp = "S"

# Inicializa a variável 'soma' com 0 para armazenar a soma dos números digitados
soma = 0

# Inicializa a variável 'quant' com 0 para contar a quantidade de números digitados
quant = 0

# Inicializa a variável 'media' com 0 para armazenar a média dos números (será calculada depois)
media = 0

# Inicializa a variável 'maior' com 0 para armazenar o maior número digitado
maior = 0

# Inicializa a variável 'menor' com 0 para armazenar o menor número digitado
menor = 0

# Inicia um loop que continua enquanto 'resp' estiver em "Ss" (ou seja, enquanto o usuário quiser continuar)
while resp in "Ss":
    # Solicita ao usuário que digite um número e converte a entrada para um inteiro
    num = int(input("Digite um numero: "))

    # Adiciona o número digitado à variável 'soma'
    soma += num

    # Incrementa a contagem de números digitados
    quant += 1

    # Se for o primeiro número digitado, inicializa 'maior' e 'menor' com esse número
    if quant == 1:
        maior = num
        menor = num
    else:
        # Se o número digitado for maior que 'maior', atualiza 'maior'
        if num > maior:
            maior = num
        # Se o número digitado for menor que 'menor', atualiza 'menor'
        if num < menor:
            menor = num

    # Pergunta ao usuário se ele quer continuar e lê a resposta
    resp = str(input("Voce que continuar [S/N] "))

# Calcula a média dos números digitados
media = soma / quant

# Exibe os resultados finais
print(f"\nResultados:")
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")
print(f"Maior número digitado: {maior}")
print(f"Menor número digitado: {menor}")
