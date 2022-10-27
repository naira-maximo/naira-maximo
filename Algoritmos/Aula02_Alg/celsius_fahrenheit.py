# Elaborar um algoritmo que efetue a conversão de graus Celsius para Fahrenheit

print("Conversor de Unidades de Temperatura")

print("Celsius (°C) para Fahrenheit (°F)")
c = float(input("Graus Celsius (°C): "))
f = c * 1.8 + 32
print(f"Temperatura em Fahrenheit (°F): {f}")

print("Fahrenheit (°F) para Celsius (°C)")
f = float(input("Graus Fahrenheit (°F): "))
c = (f - 32)/1.8
print(f"Temperatura em Celsius (°C): {c}")

resposta = input("Deseja continuar? (S) SIM (N) NÃO: ")
if resposta == "S":
    print("Próximo exercício")
elif resposta == "s":
    print("Próximo exercício")
else:
    print("Teste finalizado")