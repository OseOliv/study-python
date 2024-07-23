# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente
# até ter um valor correto.

# sexo = ""

# while sexo == "":
#     sexo = str(input("Informe seu sexo: [M/F] ")).upper().strip()[0]
#     if sexo == "M" or sexo == "F":
#         print(f"Sexo {sexo} registrado com sucesso!")
#         print("Obrigado por informar seu sexo.")

#     else:
#         print("Dados invalidos. Por favor, informe seu sexo:")


# Solicita ao usuário que informe seu sexo e converte a entrada
# para maiúsculas, remove espaços em branco nas extremidades e
# pega apenas o primeiro caractere.
sexo = str(input("Informe seu sexo [M/F]: ")).upper().strip()[0]

# Inicia um loop while que continuará executando enquanto a
# entrada do usuário não estiver entre 'M' ou 'F' (maiúsculas ou minúsculas).
while sexo not in "MmFf":
    # Se a entrada não for válida, solicita novamente ao usuário que
    # informe seu sexo, aplicando as mesmas transformações
    # (maiúsculas, remover espaços e pegar o primeiro caractere).
    sexo = str(input("Dados invalidos. Por favor, informe seu sexo: ")
               ).upper().strip()[0]

# Quando uma entrada válida for recebida, imprime uma mensagem de sucesso.
print(f"Sexo {sexo} registrado com sucesso!")
