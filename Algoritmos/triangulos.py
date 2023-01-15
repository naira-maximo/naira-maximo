# Estruturas de Seleção

# 1) Dados três valores A, B, C, elaborar um algoritmo para verificar se os comprimentos informados são válidos para formar um triângulo,
# e em caso positivo, verificar se o triângulo formado é equilátero, isósceles ou escaleno:
# Dados de entrada: três lados de um triângulo (A, B, C)
# Dados de saída - Possíveis mensagens: 
# •	Não compõem um triângulo válido; 
# •	É um triângulo equilátero; 
# •	É um triângulo escaleno; ou 
# •	É um triângulo isósceles.

# O que é triângulo?
# Resposta: Figura geométrica fechada de três lados, onde seus comprimentos atendem minimamente um dos seguintes critérios:
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

# Observação: Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

# O que é um triângulo equilátero?
# Resposta: Um triângulo com três lados iguais.

# O que é um triângulo isósceles?
# Resposta: Um triângulo com dois lados iguais

# O que é um triângulo escaleno?
# Resposta: Um triângulo com todos os lados diferentes.

# É triângulo?  É equilátero?  É isósceles?  É escaleno?    Ações
#     V               V             F             F      "Equilátero"
#     V               F             V             -      "Isósceles"
#     V               F             F             V       "Escaleno"
#     F               -             -             -   "Não é um triângulo"
print('-='*13)
print('Analisador de Triângulos')
print('-='*13)
def triangulo():
    a = int(input('Insira o valor de A: '))
    b = int(input('Insira o valor de B: '))
    c = int(input('Insira o valor de C: '))

    if abs(a<b+c) and abs(b<a+c) and abs(c<a+b):
        print('É um triângulo e ', end='')
        if (a==b) and (b==c):
            print('é um triângulo equilátero')
        elif (a==b) or (a==c) or (b==c):
            print('é um triângulo isósceles')
        elif (a!=b) and (b!=c) and (a!=c):
            print('é um triângulo escaleno')
         
    else:
        print('Não compõem um triângulo válido')
    return triangulo()
triangulo()
