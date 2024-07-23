# Crie uma tupla preenchida com os 20 primeiros
# colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Vasco.

times = ("Flamengo", "Palmeiras", "Bahia", "Botafogo", "Athletico-PR",
         "Bragantino", "Internacional", "Cruzeiro", "São Paulo", "Atlético-MG",
         "Fortaleza", "Juventude", "Criciúma", "Cuiabá", "Vasco", "Atlético-GO",
         "Vitória", "Corinthians", "Grêmio", "Fluminense")

primeiros = times[0:5]
print(" === Os 5 primeiros times ===")
print(primeiros)
print("^="*20)
print("")
print("")

ultimos = times[-4:]
print(" === Os últimos 4 colocados ===")
print(ultimos)
print("^="*20)
print("")
print("")

ordem = sorted(times)
print(" === Times em ordem alfabética ===")
print(ordem)
print("^="*20)
print("")
print("")

posicao = times.index("Vasco")
print(" === Em que posição está o time da Vasco. ===")
print(f"O Vasco esta na {posicao+1} posicao")
print("^="*20)
print("")
print("")
