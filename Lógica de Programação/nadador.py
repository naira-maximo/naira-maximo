# Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
'''Idade            Categoria
5 até 7 anos        Infantil A
8 até 10 anos       Infantil B
11 até 13 anos      Juvenil A
14 até 17 anos      Juvenil B
Maiores de 18 anos  Adulto'''

categorias = ['Infantil A', 'Infantil B', 'Juvenil A', 'Juvenil B', 'Adulto']
def nadador():
    idade = int(input('Insira a sua idade: '))
    if idade >= 5 and idade <= 7:
        print(f'Sua categoria é {categorias[0]}')
    elif idade >= 8 and idade <= 10:
        print(f'Sua categoria é {categorias[1]}')
    elif idade >= 11 and idade <= 13:
        print(f'Sua categoria é {categorias[2]}')
    elif idade >= 14 and idade <= 17:
        print(f'Sua categoria é {categorias[3]}')
    elif idade >= 18:
        print(f'Sua categoria é {categorias[4]}')
    else:
        print('Ainda não pertence à uma categoria')
    nadador()
nadador()