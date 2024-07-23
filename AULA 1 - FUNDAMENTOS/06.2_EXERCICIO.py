# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada
# Km acima do limite.


velcar = float(input("Digite a velocia do carro: "))

multa1km = 7.00

multatotal = (velcar - 80) * 7


if velcar > 80:
    print(f"Voce foi multado em R${multatotal:.2f}")
else:
    print("Voce esta dentro do limite de velocidade")
