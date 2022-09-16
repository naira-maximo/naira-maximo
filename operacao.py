import math
# Elaborar um algoritmo que efetue o cálculo de juros simples, tendo como entrada:
# C = capital
# i = taxa de empréstimo
# n = períodos

print("Calculadora de juros simples")

C = float(input("Insira seu capital: "))
i = int(input("Insira a porcentagem da taxa de juros: "))
n = float(input("Insira o período em meses: "))

juros = C * (i/100) * n
print(f'Juros: {juros}')
capital_com_juros = C + juros
print(f'Capital com juros: {capital_com_juros}')

resposta = input("Deseja continuar? (S) SIM (N) NÃO: ")
if resposta == "S":
    print("Próximo exercício")
elif resposta == "s":
    print("Próximo exercício")
else:
    print("Teste finalizado")

# Elaborar um algoritmo que efetue a conversão de graus Celsius para Fahrenheit

print("Conversor de Unidades de Temperatura")

print("Celsius (°C) para Fahrenheit (°F)")
C = float(input("Graus Celsius (°C): "))
F = C * 1.8 + 32
print(f"Temperatura em Fahrenheit (°F): {F}")

print("Fahrenheit para Celsius (°C)")
F = float(input("Graus Fahrenheit (°F): "))
C = (F - 32)/1.8
print(f"Temperatura em Celsius (°C): {C}")

resposta = input("Deseja continuar? (S) SIM (N) NÃO: ")
if resposta == "S":
    print("Próximo exercício")
elif resposta == "s":
    print("Próximo exercício")
else:
    print("Teste finalizado")


# Criar um algoritmo que permita fazer a conexão cambial entre Reais e Dólares.
# Considerar como taxa de câmbio US$1,0 = R$2,40.
# Ler um valor em Reais pelo teclado e mostrar o correspondente em Dólares.

# Exercícios de Fixação em sala 5/9/2022



# Calcular e imprimir o valor a ser pago pelo cliente.
# Álcool: até 20 litros, desconto de 3% por litro; acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro; acima de 20 litros, desconto de 6% por litro


a=int(input("Primeiro valor: "))
b=int(input("Segundo valor: "))
if a > b:
    print("O primeiro valor é maior que o segundo!")
if b > a:
    print("O segundo valor é maior que o primeiro!")

v=int(input("Velocidade: "))
if v > 110:
    print("Você foi multado!")
    multa=(v-100)*5
    print(f"Valor da multa a ser paga é: {multa}") 
