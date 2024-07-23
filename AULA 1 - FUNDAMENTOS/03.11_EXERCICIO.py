# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

kmp = float(input("Quantos KM foram percorridos? "))
qtd = int(input("Por quantos DIAS o carro foi alugado? "))

dia = 60
km = 0.15

tp = (dia*qtd)+(kmp*km)

print(f"O total a pagar e de : R$ {tp:.2f}")
