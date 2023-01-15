# Contrua um algoritmo que seja capaz de concluir qual dentre os seguintes animais foi escolhido, através de perguntas e respostas.
# Animais possíveis: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.
#            ____              
#           |     Quadrúpedes-| --- Carnívoros --- Leão
#           |                 | --- Herbívoros --- Cavalo
# Mamíferos-|     Bípedes-| --- Onívoros --- Homem
#           |             | --- Frutívoros --- Macaco
#           |     Voadores --- Morcego
#           |____ Aquáticos --- Baleia
#       ____              
#      |     Não-voadoras-| --- Tropicais --- Avestruz
# Aves-|                  | --- Polares --- Pinguim
#      |     Nadadoras --- Pato
#      |____ De rapina --- Águia
#          ____ 
#         |     Com casco --- Tartaruga
# Répteis-|     Carnívoros --- Crocodilo
#         |____ Sem patas --- Cobra

print('Pense em um desses animais, mas não me conte qual é:')
print('-' * 55)
print('''Águia
Avestruz
Baleia
Cavalo
Cobra
Crocodilo
Homem
Leão
Macaco
Morcego
Pato
Pinguim
Tartaruga''')
print('-' * 55)
print('Vou tentar descobrir qual é, mas preciso que me responda algumas perguntas:')

def animal():
    tipo = str(input('\nO animal que você pensou é um mamífero, uma ave ou um réptil? ')).lower().strip()
    if tipo == 'mamífero' or tipo == 'mamifero':
        patas = str(input('\nO animal que você pensou é quadrúpede, bípede, voador ou aquático? ')).lower().strip()
        if patas == 'quadrúpede' or tipo == 'quadrupede':
            alimento = str(input('\nO animal que você pensou é carnívoro ou herbívoro? ')).lower().strip()
            if alimento == 'carnívoro' or alimento == 'carnivoro':
                print('\nO animal que você pensou é o leão')
            elif alimento == 'herbívoro' or alimento == 'herbivoro':
                print('\nO animal que você pensou é o cavalo')
            else:
                print('\n\033[1;31mInsira um tipo válido\033[m')
        elif patas == 'bípede' or patas == 'bipede':
            alimento = str(input('\nO animal que você pensou é onívoro ou frutívoro? ')).lower().strip()
            if alimento == 'onívoro' or alimento == 'onivoro':
                print('\nO animal que você pensou é o homem')
            elif alimento == 'frutívoro' or alimento == 'frutivoro':
                print('\nO animal que você pensou é o macaco')
            else:
                print('\n\033[1;31mInsira um tipo válido\033[m')
        elif patas == 'voador':
            print('\nO animal que você pensou é o morcego')
        elif patas == 'aquatico' or patas == 'aquático':
            print('\nO animal que você pensou é a baleia')
        else:
            print('\n\033[1;31mInsira um tipo válido\033[m')
    elif tipo == 'ave':
        habitat = str(input('\nO animal que você pensou é nadador, de rapina ou não-voador? ')).lower().strip()
        if habitat == 'nadador':
            print('\nO animal que você pensou é o pato')
        elif habitat == 'de rapina' or habitat == 'rapina':
            print('\nO animal que você pensou é a águia')
        elif habitat == 'não-voador' or 'não voador':
            clima = str(input('\nO animal que você pensou é tropical ou polar? ')).lower().strip()
            if clima == 'tropical':
                print('\nO animal que você pensou é o avestruz')
            elif clima == 'polar':
                print('\nO animal que você pensou é o pinguim')
            else:
                print('\n\033[1;31mInsira um tipo válido\033[m')
    elif tipo == 'réptil' or tipo == 'reptil':
        casco = str(input('\nO animal que você pensou tem casco? ')).lower().strip()
        if casco == 'sim':
            print('\nO animal que você pensou é a tartaruga')
        elif casco == 'não':
            sem_patas = str(input('\nO animal que você pensou tem patas? ')).lower().strip()
            if sem_patas == 'sim':
                print('\nO animal que você pensou é o crocodilo')
            elif sem_patas == 'não':
                print('\nO animal que você pensou é a cobra')
            else:
                print('\n\033[1;31mInsira um tipo válido\033[m')
    else:
        print('\n\033[1;31mInsira um tipo válido\033[m')
        animal()
    animal()
animal()