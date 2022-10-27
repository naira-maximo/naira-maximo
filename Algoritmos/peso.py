# Tendo como dados de entrada a altura e o sexo de uma pessoa (M masculino e F feminino)
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# * para homens: (72.7*h)-58
# * para mulheres (62.1*h)-44.7
print('\033[1;35m-\033[m'*20)
print('\033[1;35mCalculo do peso ideal\033[m')
print('\033[1;35m-\033[m'*20)

def peso(): 

    h = float(input('\nInsira sua altura em metros: '))

    pesohomem = (72.7*h)-58
    pesomulher = (62.1*h)-44.7

    resposta = input('Qual o seu sexo? (F) Feminino (M) Masculino: ')
    if resposta == 'M':
        print('Seu peso ideal é \033[1;35m{:.1f}kg\033[m'.format(pesohomem))
    elif resposta == 'F':
        print('Seu peso ideal é \033[1;35m{:.1f}kg\033[m'.format(pesomulher))
    else:
        print('\033[1;35mResponda com F para Feminino ou M para Masculino\033[m')
    return peso()

peso()

