# MANIPULANDO TEXTO

# ANALISE

frase = "Curso em Video Python"
print(len(frase))  # Comprimento
print(frase.count("o"))  # Quantidade
print(frase.count("o", 0, 13))
print(frase.find("deo"))
print(frase.find("Android"))  # False
print("Curso" in frase)  # True
print("=================")
print(frase.replace("Python", "Android"))
print(frase.upper())
print(frase.lower())
print("=================")
print(frase.capitalize())
print(frase.title())
("")
print("=================")
frase1 = "   Aprenda Python  "
print(frase1.strip())
