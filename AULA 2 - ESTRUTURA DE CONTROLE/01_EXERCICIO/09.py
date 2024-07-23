# Elabore um programa que calcule o valor a
# ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

produtoPreco = float(input("Digite o valor do produto: R$ "))
condPagamento = input("""
- FORMAS DE PAGAMENTO - 
[1] A VISTA DINHEIRO/CHEQUE
[2] A VISTA CARTAO
[3] 2x CARTAO
[4] 3x OU MAIS NO CARTAO
ESCOLHA UMA OPCAO: 
""").strip().lower()

dincheDesc = produtoPreco * 0.10

visCartao = produtoPreco * 0.05

mais3x = produtoPreco * 0.20


if condPagamento == "1":
    pagVista = produtoPreco - dincheDesc
    print(
        f"O valor a ser pago com pagamento à vista dinheiro/cheque com 10% de desconto e: R${pagVista:.2f}")

elif condPagamento == "2":
    pagCartaoVista = produtoPreco - visCartao
    print(f"O valor a pagar a vista com 5% de desconto e de: R${
        pagCartaoVista:.2f}")
elif condPagamento == "3":
    print(f"O valor a pagar em 2x sem juros e de: R${produtoPreco:.2f}")
elif condPagamento == "4":
    pagCartao3x = produtoPreco + mais3x
    print(f"O valor a ser pago com 20% de juros e de: R${pagCartao3x:.2f}")
else:
    print("Operacao Invalida")
