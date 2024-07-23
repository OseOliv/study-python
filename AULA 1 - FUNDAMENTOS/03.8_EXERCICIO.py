# FACA UM ALGORITIMO QUE LEIA O PRECO DE UM PRODUTO
# E MOSTRE O NOVO PRECO, COM 5% DE DESCONTO

p = float(input("Digite o preco do produto: "))

d = p * 0.05  # (p*5/100)

vd = p - d

print(f"O valor do produto e: R${p:.2f},  o valor do desconto de 5% e: R${
      d:.2f}, e o valor final com o desconte e: R${vd:.2f}")
