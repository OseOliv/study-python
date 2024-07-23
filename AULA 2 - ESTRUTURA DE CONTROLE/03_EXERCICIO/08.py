# Crie um programa que leia vários números inteiros
# pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).


countDigitados = 0
somaNumeros = 0


while True:
    # Solicita ao usuário que digite um número e converte para inteiro
    num = int(input("Digite um número [999 para parar]: "))

    # Verifica se o número digitado é 999 (condição de parada)
    if num == 999:
        # Imprime a mensagem com o número de números digitados e a soma deles
        print(f"Você digitou {
              countDigitados} números e a soma entre eles foi {somaNumeros}.")
        # Sai do loop while
        break

    # Adiciona o número digitado à soma dos números
    somaNumeros += num

    # Incrementa o contador de números digitados
    countDigitados += 1

# Após sair do loop while, imprime "FIM"
print("FIM")
