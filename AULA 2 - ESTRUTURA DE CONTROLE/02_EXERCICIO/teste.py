# Inicializando variáveis
IdadeMaisVelho = 0
nomeMaisVelho = ""

# Simulando a entrada de dados para 4 pessoas
for p in range(1, 5):
    # Simulando a entrada de dados
    nome = input(f"Digite o nome da pessoa {p}: ")
    sexo = input(f"Digite o sexo da pessoa {p} (M/F): ").upper()
    idade = int(input(f"Digite a idade da pessoa {p}: "))

    # Imprimindo informações para debug (opcional)
    print(f"Debug - Pessoa {p}: nome={nome}, sexo={sexo}, idade={idade}")

    # Verificando se é um homem e se é mais velho que o homem mais velho registrado até agora
    if sexo == "M" and idade > IdadeMaisVelho:
        print(
            f"Debug - Novo homem mais velho encontrado: nome={nome}, idade={idade}")
        IdadeMaisVelho = idade
        nomeMaisVelho = nome

# Exibindo o resultado final
print(f"O homem mais velho é {nomeMaisVelho} com {IdadeMaisVelho} anos.")
