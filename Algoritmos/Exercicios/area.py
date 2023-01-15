def area():
    valor = float(input('Insira o valor: '))
    tipo = str(input('Insira o tipo da forma (C para círculo e Q para quadrado): ')).upper().strip()
    if tipo == 'C':
        print(f'Para um círculo com raio {valor}, a área é {3.14 * (valor**2)}')
    elif tipo == 'Q':
        print(f'Para um quadrado com lado {valor}, a área é {valor * valor}')
    else:
        print(f'{tipo} não é aceito como tipo. Insira C para círculo e Q para quadrado')
        area()
area()
