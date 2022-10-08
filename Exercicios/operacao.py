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

# Estruturas aninhadas
# Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra R$0,20 por minuto.
# Entre 200 e 400 minutos, o preço é R$0,18.
# Acima de 400 minutos, o preço por minuto é R$0,15
# Calcule sua conta de telefone.

minutos=int(input("Insira a quantidade de minutos: "))
if minutos < 200:
    menos200 = minutos*0.20
    print(f"Sua fatura é de: R${menos200}")
if minutos >= 200 and minutos < 400:
    entre = minutos*0.18
    print(f"Sua fatura é de: R${entre}")
if minutos >= 400:
    mais400 = minutos*0.15
    print(f"Sua fatura é de: R${mais400}")

# Elaborar um algoritmo que calcule as raízes da equação do 2º grau conforme a fórmula de Bhaskara.

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("Não tem raízes reais")
elif delta == 0:
    x = -b / (2 * a)
    print("Temos como solução duas raízes reais iguais no valor de:", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Temos como solução duas raízes reais e diferentes")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

#Tendo como dados de entrada a altura e o sexo de uma pessoa (M masculino e F feminino)
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# * para homens: (72.7*h)-58
# * para mulheres (62.1*h)-44.7

print("Calculo do peso ideal")

h = float(input("Insira sua altura em metros: "))

pesohomem = (72.7*h)-58
pesomulher = (62.1*h)-44.7

resposta = input("Qual o seu sexo? (F) Feminino (M) Masculino")
if resposta == "F":
    print(f"Seu peso ideal:{pesohomem} ")
elif resposta == "M":
    print(f"Seu peso ideal:{pesomulher}")
else:
    print("Responda com F para Feminino e M para Masculino")
