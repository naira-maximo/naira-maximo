# Elaborar um algoritmo que efetue o cálculo de juros simples, tendo como entrada:
# c = capital
# i = taxa de empréstimo
# n = períodos

print("Calculadora de juros simples")

c = float(input("Insira seu capital: "))
i = int(input("Insira a porcentagem da taxa de juros: "))
n = float(input("Insira o período em meses: "))

juros = c * (i/100) * n
print(f'Juros: {juros}')
capital_com_juros = c + juros
print(f'Capital com juros: {capital_com_juros}')