# CONDICOES ANINHADAS

nome = str(input("Qual e seu nome? "))
print("")
if nome == "Oseas":
    print("Que nome bonito!")
    print("")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome e bem popular no brasil")
    print("")
elif nome in 'Ana Claudia Jessica Juliana':
    print("Que belo nome feminino!")
    print("")
else:
    print("Seu nome e bem normal!")


print(f"Tenha um bom dia, {nome}")
print("")
