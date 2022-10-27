# Gere uma lista de 100 inteiros aleatórios entre 1 e 100 que sejam distintos entre si
import random
lista = []
k = 1
while k <= 100:
    x = random.randint(1, 100)
    if x not in lista:
        lista.append(x)
        k = k + 1
print(lista)