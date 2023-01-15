# JOGO DA FORCA
# Elaborado por Naira Giulia Pereira Maximo dos Santos, utilizando como referência o vídeo do canal I Do Code, disponível em: https://www.youtube.com/watch?v=ma69nu3-ub0
# Jogo criado com o intuito de treinar a linguagem de programação Python, os operadores lógicos (and, or, not) e conjuntos (listas e strings). 
# O campo semântico foi escolhido para trabalhar com uma turma de alfabetização do Pré II. As letras precisam ser maiúsculas e as palavras de uso social (cardápio da escola). 

import random  # Importar biblioteca que seleciona item aleatório da lista
palavras = ['MELANCIA', 'MORANGO', 'BANANA', 'GOIABA', 'ABACAXI', 'UVA', 'LARANJA']

palavra = random.choice(palavras)  # Função para escolher item aleatório

# print(palavra) # Utilizado para testar o jogo

tentativas = 0  # Acumulador para comparação com as chances e acompanhamento do jogador

chances = 4  # Quantas chances para tentar acertar as letras

letras_escolhidas = []

estado_atual = ['_'] * len(palavra)  # Quantidade de caracteres da palavra. length, tamanho

print('\033[1;33;45mJOGO DA FORCA DAS FRUTAS\033[m\n')
print('TENTE ACERTAR A FRUTA SECRETA!')
print(f'VOCÊ PRECISA TENTAR UMA LETRA DE CADA VEZ. SE ERRAR, PERDE UMA CHANCE.')
print(f'VOCÊ TEM {chances} CHANCES PARA ACERTAR.\n')
print('BOA SORTE!')

while tentativas < chances and ''.join(estado_atual) != palavra:  # Condição 'e'. Função .join faz com que a lista da palavra atual se transforme em um texto para ser comparado.
    letra = input('\n\nQUAL LETRA VOCÊ QUER TENTAR? ').upper()
    while letra in letras_escolhidas:
        print(f'\n\033[1;35mVOCÊ JÁ TENTOU A LETRA {letra}, ESCOLHA OUTRA\033[m')
        letra = input('\nQUAL LETRA VOCÊ QUER TENTAR? ')

    letras_escolhidas.append(letra)  # Adicionar as letras digitadas à lista
    
    if letra in palavra:
        print('\n\033[1;33mVOCÊ ACERTOU A LETRA!\033[m')
        for i in range(len(palavra)):  # Passar o laço por todos os caracteres da palavra como índice
            if letra == palavra[i]:  # Se a tentativa for igual a um ou mais índices da palavra escolhida aleatoriamente 
                
                estado_atual[i] = letra  # Colocar a letra na posição da lista
    else:
        print(f'\n\033[1;35mA FRUTA SECRETA NÃO TEM A LETRA {letra}\033[m')
        tentativas += 1  # Igual a tentativas = tentativas + 1

    # Quantas tentativas ele tem
    print (f'\nVOCÊ FEZ {tentativas} TENTATIVAS ERRADAS E AINDA TEM {chances - tentativas} TENTATIVAS\n')

    #Qual o estado atual da palavra
    print('ESSE É SEU ESTADO ATUAL:')
    print(estado_atual)

    #Quais letras ele já tentou
    print('\nAS LETRAS QUE VOCÊ JÁ TENTOU SÃO:')
    for i in letras_escolhidas:
        print(i, end = ' - ')  # O print, por padrão, pula uma linha. Com o end, escolhemos colocar um espaço entre uma letra e outra.

# Finalizar o jogo
if tentativas == chances:
    print(f"\n\n\033[1;31mACABARAM SUAS TENTATIVAS. A FRUTA SECRETA É {palavra}\033[m")
else:
    print(f"\n\n\033[1;33mVOCÊ ACERTOU A FRUTA SECRETA, É {palavra}!\033[m")
