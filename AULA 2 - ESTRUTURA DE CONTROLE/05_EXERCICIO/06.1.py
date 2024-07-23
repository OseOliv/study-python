# Crie um programa que tenha uma tupla com
# várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

# Definição da tupla com as palavras
palavras = ('banana', 'carro', 'computador', 'lua', 'cachorro',
            'sol', 'girassol', 'chocolate', 'montanha', 'aventura')

# Itera sobre cada palavra na tupla palavras
for p in palavras:
    # Imprime o início da linha com a palavra atual
    print(f"\nNa palavra {p} temos: ", end="")

    # Itera sobre cada letra na palavra atual
    for letra in p:
        # Verifica se a letra é uma vogal (está presente em "aeiou")
        if letra in "aeiou":
            # Imprime a vogal encontrada, seguida de um espaço
            print(letra, end=" ")

# Imprime uma linha em branco no final para melhorar a formatação
print()
