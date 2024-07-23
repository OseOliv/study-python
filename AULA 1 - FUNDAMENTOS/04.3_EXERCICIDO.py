# FACA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER
# E MOSTRE NA TELA O VALOR DO SENO, COSSENO E
# TANGENTE DESSE ANGULO

from math import sin, cos, tan, radians

ang = float(input("Digite um angulo qualquer: "))

angr = radians(ang)

se = sin(angr)

co = cos(angr)

ta = tan(angr)


print(f"O Seno do angulo {ang}° e: {se:.2f}°")
print(f"O Cosseno do angulo {ang}° e: {co:.2f}°")
print(f"A Tangente do angulo {ang}° e: {ta:.2f}°")
