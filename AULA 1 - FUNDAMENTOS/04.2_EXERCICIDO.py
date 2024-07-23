# FACA UM PROGRAMA QUE LEIA O COMPRIMENTO
# DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM
# TRIANGULO RETANGULO, CALCULE E MOSTRE
# O COMPRIMENTO DA HIPOTENUSA

from math import pow, sqrt, hypot

co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))

coca = (pow(co, 2)) + (pow(ca, 2))

hip = sqrt(coca)

# OU

hip2 = hypot(co, ca)

print(f"A hipotenusa de do triangulo com CO {co} e CA {ca} e: {hip:.2f}")
print(hip2)
