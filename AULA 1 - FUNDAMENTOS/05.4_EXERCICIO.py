# Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez.

# O seu programa funciona bem para números que
# possuem exatamente 4 dígitos, mas pode gerar erros ou não funcionar
# como esperado para números com menos de 4 dígitos. Vamos melhorar isso para lidar
# com números de qualquer quantidade de dígitos dentro do intervalo de 0 a 9999.


frase = input("Digite uma frase: ").upper().strip()

fraseA = frase.count("A")
print(f"Quantidade de vezes que 'A' aparece: {fraseA}")

fraseP = frase.find("A")+1
print(f"Posição da primeira ocorrência de 'A': {fraseP}")

fraseU = frase.rfind("A")+1
print(f"Posição da última ocorrência de 'A': {fraseU}")
