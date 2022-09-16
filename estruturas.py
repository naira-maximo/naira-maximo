import math

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