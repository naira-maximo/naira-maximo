# Tendo como dados de entrada a altura e o sexo de uma pessoa (M masculino e F feminino)
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# * para homens: (72.7*h)-58
# * para mulheres (62.1*h)-44.7
print('\033[1;35m-\033[m'*20)
print('\033[1;35mCalculo do peso ideal\033[m')
print('\033[1;35m-\033[m'*20)

def peso_ideal(): 

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
        peso_ideal()
peso_ideal()

# O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta.
# A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição.
'''IMC em adultos          Condição
   abaixo de 18,5       abaixo do peso
   entre 18,5 e 25      peso normal
   entre 25 e 30        acima do peso
   acima de 30          obeso'''

condição = ['abaixo do peso', 'peso normal', 'acima do peso', 'obeso']
peso = float(input('Insira o seu peso: '))
altura = float(input('Insira sua altura: '))

calculo = peso / (altura**2)

if calculo < 18.5:
    print(f'O resultado do seu IMC é {calculo:.1f}, portanto você está {condição[0]}')
elif calculo >= 18.5 and calculo <= 25:
    print(f'O resultado do seu IMC é {calculo:.1f}, portanto você está {condição[1]}')
elif calculo > 25 and calculo <= 30:
    print(f'O resultado do seu IMC é {calculo:.1f}, portanto você está {condição[2]}')
else:
    print(f'O resultado do seu IMC é {calculo:.1f}, portanto você está {condição[3]}')

