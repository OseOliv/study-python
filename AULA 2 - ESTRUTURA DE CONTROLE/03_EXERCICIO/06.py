# Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.


# Solicita ao usuário para inserir o termo inicial da PA
termo = int(input("Digite o termo inicial da PA: "))

# Solicita ao usuário para inserir a razão da PA
razao = int(input("Digite a razão da PA: "))

# Imprime um separador para melhor visualização
print("-=" * 10)

# Inicializa o contador que controlará quantos termos já foram mostrados
contador = 1

# Inicializa a variável total que acumulará o número total de termos a serem mostrados
total = 0

# Inicializa novoTermo com um valor inicial diferente de zero para entrar no primeiro loop
novoTermo = 10

# Loop principal que continuará executando enquanto novoTermo for diferente de zero
while novoTermo != 0:
    # Acumula o número de termos que o usuário deseja mostrar
    total = total + novoTermo

    # Loop interno para calcular e imprimir os termos da PA até alcançar o total acumulado
    while contador <= total:
        # Imprime o termo atual da PA seguido por uma seta (➞)
        print(f"{termo}", end=" ➞ ")

        # Calcula o próximo termo da PA adicionando a razão ao termo atual
        termo = termo + razao

        # Incrementa o contador para controlar quantos termos já foram mostrados
        contador += 1

    # Após mostrar os termos desejados, imprime "PAUSA"
    print(" PAUSA ")

    # Pergunta ao usuário quantos termos adicionais ele deseja ver
    novoTermo = int(
        input("Quantos termos você quer mostrar mais? (Digite 0 para parar) "))

# Quando o usuário digitar 0 para novoTermo, o loop principal termina e o programa imprime a mensagem final
print(f"Programa encerrado. Total de {total} termos mostrados.")
