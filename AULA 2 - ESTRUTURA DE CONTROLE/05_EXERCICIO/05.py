# Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

# Tupla com nomes de produtos e seus preços
produtos = (
    ("Produto A", 29.90),
    ("Produto B", 49.99),
    ("Produto C", 99.50),
    ("Produto D", 149.99),
    ("Produto E", 199.00)
)

# Imprime o cabeçalho da tabela
print("Lista de Preços")
print("-" * 20)
print(f"{"Produto":<15} {"Preço":>10}")

# Itera sobre a tupla e imprime cada produto e seu preço formatado
for produto, preco in produtos:
    print(f"{produto:<15} R$ {preco:>8.2f}")
