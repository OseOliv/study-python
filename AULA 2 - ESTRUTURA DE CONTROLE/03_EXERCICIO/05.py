# Refaça o DESAFIO 051, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razao: "))
print("-=" * 10)

contador = 1


while contador <= 10:
    print(f"{termo}", end=" ➞ ")
    termo = termo + razao
    contador += 1


print(f" FIM")
