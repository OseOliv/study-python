# FACA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS,
# CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA,
# SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2 METROS QUADRADO

n = input("Digite seu nome: ")
l = float(input("Digite uma largura: "))
a = float(input("digite um altura: "))

ar = l * a

tn = ar / 2

print(f"{n} voce ira precisa de {tn:.2f}L de tinta para pintar a parede")
