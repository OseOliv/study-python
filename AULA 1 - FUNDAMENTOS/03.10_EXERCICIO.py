# FACA UM COVERSOR DE CELSIUS PARA FAHRENHEIT

g = float(input("Digite a temperatura: °C "))
gf = float(input("Digite a temperatura: °F "))

tf = (g * 1.8) + 32  # C > F
tc = (gf - 32) / 1.8  # F > C

print(f"A temperatura {g:.1f}°C em  Fahrenheit e: {tf:.1f}°F")
print(f"A temperatura {gf:.1f}°F em  Celsius e: {tc:.1f}°C")
