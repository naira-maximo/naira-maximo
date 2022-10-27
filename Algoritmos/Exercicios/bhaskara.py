import math
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
    x1 = (-b + math.sqrt(delta)) / (2 * a) # Sem importar math, raiz quadrada seria n**1\2
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Temos como solução duas raízes reais e diferentes")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")