# Crie um programa que tenha uma tupla com
# várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.


palavras = ('banana', 'carro', 'computador', 'lua', 'cachorro',
            'sol', 'girassol', 'chocolate', 'montanha', 'aventura')

vogais = 'aeiou'

for palavra in palavras:
    print(f'Vogais de "{palavra}": ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print()
