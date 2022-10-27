# Repetições aninhadas
# • Imprima as tabuadas de 1 a 10

tabuada = 1
while tabuada <=10:
    n = 1
    print('-'*13)
    print(f'Tabuada do {tabuada}:')
    print('-'*13)
    while n <=10:
        print(f'{tabuada} x {n:2} = {tabuada*n}')
        n = n + 1
    tabuada = tabuada + 1