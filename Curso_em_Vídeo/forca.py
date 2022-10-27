from codecs import BufferedIncrementalEncoder
import random  # Importar biblioteca que seleciona item aleatório da lista
palavras = ['MELANCIA', 'MAÇÃ', 'BANANA', 'MELÃO', 'ABACAXI', 'MELÃO', 'MEXERICA']

palavra = random.choice(palavras)  # Função para escolher item aleatório

print(palavra)

tentativas = 0  # Como vamos perder o jogo. Fizemos tentativas demais

chances = 4  # Quantas chances para tentar acertar as letras

letras_escolhidas = []

estado_atual = ['_'] * len(palavra)  # Quantidade de caracteres da palavra. length, tamanho

print('\033[1;33;45mJOGO DA FORCA DAS FRUTAS\033[m')
print('TENTE ACERTAR A FRUTA SECRETA')
print(f'VOCÊ PRECISA TENTAR UMA LETRA DE CADA VEZ. SE ERRAR, PERDE UMA CHANCE')
print(f'VOCÊ TEM {chances} CHANCES PARA ACERTAR\n')
print('BOA SORTE!')

while tentativas <= chances and ''.join(estado_atual) != palavra:  # Condição 'e'. Função .join faz com que a lista da palavra atual se transforme em um texto para ser comparado.
    letra = input('\n\nQUAL LETRA VOCÊ QUER TENTAR? ')
    while letra in letras_escolhidas:
        print(f'\nVOCÊ JÁ TENTOU A LETRA {letra}, ESCOLHA OUTRA')
        letra = input('\nQUAL LETRA VOCÊ QUER TENTAR? ')

    letras_escolhidas.append(letra)  # Adicionar as letras digitadas à lista
    
    if letra in palavra:
        print('VOCÊ ACERTOU A LETRA!\n')
        for i in range(len(palavra)):  # Passar o laço por todos os caracteres da palavra como índice
            if letra == palavra[i]:  # Se a tentativa for igual a um ou mais índices da palavra escolhida aleatoriamente 
                
                estado_atual[i] = letra  # Colocar a letra na posição da lista
    else:
        print(f'A FRUTA SECRETA NÃO TEM A LETRA {letra}\n')
        tentativas += 1  # Igual a tentativas = tentativas + 1

    # Quantas tentativas ele tem
    print (f'VOCÊ FEZ {tentativas} TENTATIVAS ERRADAS E AINDA TEM {chances - tentativas} TENTATIVAS')

    #Qual o estado atual da palavra
    print('ESSE É SEU ESTADO ATUAL:')
    print(estado_atual)

    #Quais letras ele já tentou
    print('AS LETRAS QUE VOCÊ JÁ TENTOU SÃO:')
    for i in letras_escolhidas:
        print(i, end = ' - ')  # O print, por padrão, pula uma linha. Com o end, escolhemos colocar um espaço entre uma letra e outra.

    # Finalizar o jogo
    if tentativas == chances:
        print(f"\n\nACABARAM SUAS TENTATIVAS. A FRUTA SECRETA É {palavra}")
    else:
        print("\n\nVOCÊ ACERTOU A FRUTA SECRETA")

# ANSI - ESCAPE SEQUENCE
# CORES DE FONTE \033[  ;    ;    m
# ESTILOS:
# 0 sem estilo - none
# 1 negrito - bold
# 4 sublinhado - underline
# 7 cores invertidas - negative

# TEXTO:
# 30 branco 
# 31 vermelho
# 32 verde 
# 33 amarelo 
# 34 azul 
# 35 roxo 
# 36 azul claro 
# 37 cinza

# BACKGROUND:
# 40 branco 
# 41 vermelho
# 42 verde 
# 43 amarelo 
# 44 azul 
# 45 roxo 
# 46 azul claro 
# 47 cinza