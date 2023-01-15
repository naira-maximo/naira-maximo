# Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada; calcule, então, a resposta adequada.
# Utilize os símbolos da tabela a seguir para ler qual a operação aritmética escolhida.
'''Símbolo          Operação aritmética
    +                   Adição
    -                  Subtração
    *                Multiplicação
    /                  Divisão'''

a = int(input('Insira um valor: '))
b = int(input('Insira outro valor: '))
operador = input('Insira um operador (+, -, * ou /) ')
if operador == '+':
    print(f'O resultado da adição de {a} e {b} é {a + b}')
elif operador == '-':
    print(f'O resultado da subtração de {a} e {b} é {a - b}')
elif operador == '*':
    print(f'O resultado da multiplicação de {a} e {b} é {a * b}')
elif operador == '/':
    print(f'O resultado da divisão de {a} e {b} é {a / b}')


