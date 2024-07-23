# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# Solicita ao usuário a quantidade de termos da sequência de Fibonacci que deseja mostrar e converte para inteiro.
num = int(input("Digite quantos termos quer mostrar: "))

# Inicializa os primeiros dois termos da sequência de Fibonacci.
ini = 0  # Primeiro termo da sequência de Fibonacci
seg = 1  # Segundo termo da sequência de Fibonacci
# Contador para controlar o número de termos já mostrados (começa em 2 pois já imprimimos os dois primeiros termos)
count = 2

# Loop para calcular e mostrar os termos da sequência de Fibonacci até o número desejado pelo usuário.
while count < num:
    # Calcula o próximo termo da sequência de Fibonacci somando os dois termos anteriores.
    prox = ini + seg
    # Imprime o próximo termo da sequência de Fibonacci seguido de um " ➞ " no final (end=" ➞ " evita quebra de linha).
    print(prox, end=" ➞ ")
    # Atualiza os valores dos termos anteriores para o próximo passo da sequência.
    ini = seg
    seg = prox
    # Incrementa o contador para controlar quantos termos já foram mostrados.
    count += 1
