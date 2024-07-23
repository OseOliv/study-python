
# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA
# TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR
# CONSIDERE = US$1,00 = R$3,27

n = input("Digite seu nome: ")
d = float(input("Digite a quantidade de dinheiro: R$"))

usd = 3.27

dc = d / 3.27

print(f"{n:.2f
         } pode comprar U${dc:.2f}")
