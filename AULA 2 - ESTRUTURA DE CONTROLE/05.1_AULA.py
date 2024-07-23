lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")

for count in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[count]} na posicao {count}")

print("<>"*10)

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicao {pos}")

print("Comi pra caramba!")
