# Desenvolva um programa que pergunte a distância
# de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 parta viagens mais longas.


dis = float(input("Digite a distancia da viagem em KM: "))

p1 = 0.50
p2 = 0.45

if dis <= 200:
    pvia1 = dis * p1
    print(f"O preco dessa viagem mais curta e de {pvia1:.2f}")
else:
    pvia2 = dis * p2
    print(f"O valor dessa viagem mais longa e de: {pvia2:.2f}")
