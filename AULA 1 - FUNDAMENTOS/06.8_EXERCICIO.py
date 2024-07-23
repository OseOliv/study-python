# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

retaA = float(input("Digite o comprimento da primeira reta: "))
retaB = float(input("Digite o comprimento da segunda reta: "))
retaC = float(input("Digite o comprimento da terceira reta: "))

# A + B > C
# A + C > B
# B + C > A

if (retaA + retaB > retaC and retaA + retaC > retaB and retaB + retaC > retaA):
    print(f"Estas tres retas {retaA}, {retaB} e {
          retaC} podem forma um triangulo")
else:
    print(f"Estas tres retas {retaA}, {retaB} e {
          retaC} NAO podem formar um triangulo")
