# 01 DESAFIO - CRIE UM PROGRAMA QUE LEIA DOIS NUMEROS E MOSTRE A SOMA ENTRE ELES

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
soma = n1 + n2

print(f"A soma ente o numero {n1} e o numero {n2} e: {soma}")


print("")
print("==================")
print("")

# 02 DESAFIO - FACA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE
# NA TELA SEU TIPO PRIMITIVO E TODAS AS INFORMACOES POSIVEIS SOBRE ELE

f1 = input("Digite algo: ")

t1 = type(f1)
t2 = f1.isspace()
t3 = f1.isnumeric()
t4 = f1.isalpha()
t5 = f1.isalpha()
t6 = f1.isupper()
t7 = f1.islower()
t8 = f1[0].isupper()  # istitle

print(f"O tipo primitivo de {f1} e: {t1}")
print(f"Se {f1} tem espacos?: {t2}")
print(f"Se {f1} e um numero?: {t3}")
print(f"Se {f1} e um alfabetico?: {t4}")
print(f"Se {f1} e um alfanumerico?: {t5}")
print(f"Se {f1} esta em maiusculo?: {t6}")
print(f"Se {f1} esta em minusculo?: {t7}")
print(f"Se {f1} esta capitalizada?: {t8}")
