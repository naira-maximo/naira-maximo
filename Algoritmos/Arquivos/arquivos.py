# Cria um arquivo no diretório se não existir e substitui se já existir no c:/Python3x
arquivo = open('numeros.txt', 'w')
for linha in range(1, 101):
    arquivo.write('%d\n' %linha)
arquivo.close()

# readlines gera uma lista onde cada elemento