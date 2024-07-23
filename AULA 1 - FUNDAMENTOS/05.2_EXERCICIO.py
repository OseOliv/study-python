# Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome "SANTO".


city = input("Digite o nome de uma cidade: ").lower().strip()

citysplit = city.split()

cityres = "santo" in citysplit[0]

print(cityres)
