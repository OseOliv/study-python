# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS
# E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS


n = float(input("Digite uma quantidade de metros: "))

c = n * 100
m = n * 1000

print(f"O número de {n}m convertido em centímetros é: {
      c}cm\nE o número de {n}m convertido em milímetros é: {m}mm")
