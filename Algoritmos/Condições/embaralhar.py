def embaralha(s):
    import random
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)

print(embaralha('palmeiras'))
print(embaralha('churrasco'))