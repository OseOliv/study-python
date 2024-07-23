# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado
# (entre 0 e 20) e mostrá-lo por extenso.


# Define uma tupla com as representações textuais dos números de 0 a 20
count = ("zero", "um", "dois", "três", "quatro", "cinco",
         "seis", "sete", "oito", "nove", "dez", "onze",
         "doze", "treze", "quatorze", "quinze", "dezesseis",
         "dezessete", "dezoito", "dezenove", "vinte")

# Inicia um loop infinito que continuará até ser interrompido
while True:
    # Solicita ao usuário que insira um número entre 0 e 20
    numero = int(input("Digite um número de 0 a 20: "))

    # Verifica se o número está no intervalo de 0 a 20
    if 0 <= numero <= 20:
        # Se o número estiver no intervalo, imprime a representação textual do número
        print(f"Você digitou o número {count[numero]}")

        # Solicita ao usuário que informe se deseja continuar, convertendo a resposta para maiúscula
        cont = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]

        # Verifica se a resposta do usuário não é 'S' (Sim)
        if cont != "S":
            # Se a resposta não for 'S', interrompe o loop
            break
    else:
        # Se o número estiver fora do intervalo, pede ao usuário para tentar novamente
        print("Tente novamente. ", end="")
