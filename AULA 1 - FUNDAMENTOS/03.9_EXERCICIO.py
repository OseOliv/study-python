# FACA UM ALGORITIMO QUE LEIA O SALARIO DE
# UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO,
# COM 15% DE AUMENTO


s = float(input("Digite o salario do funcionario: "))

a = s * 0.15  # (s * 15/100)

ns = s + a

print(f"O valor do salario e: {s:.2f}, o valor do aumento de 15% sera: {
      a:.2f}, o valor do salario final com o aumento sera de: {ns:.2f}")
