#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Exercícios básicos com strings

# A. donuts
# Para um inteiro n retorna uma string na forma 'Número de donuts: <n>'
# onde n é o valor passado como argumento.
# Caso n >= 10 devo retornar 'muitos' em lugar do número.
# donuts(5) returns 'Número de donuts: 5'
# donuts(23) returns 'Número de donuts: muitos'
def donuts(n):
  if n < 10:
    n = (f'Número de donuts: {n}')
  else:
    n = ('Número de donuts: muitos')
  return n

# B. pontas
# Dada uma string s, retorna uma string com as duas primeiras e as duas
# últimas letras da string original s
# Assim 'palmeiras' retorna 'paas'
# No entanto, se a string tiver menos que 2 letras, retorna uma string vazia
def pontas(s):
  if len(s) >= 2:
    s = s[:2] + s[-2:]
  else:
    s = ''
  return s

# C. fixa_primeiro
# Dada uma string s, retorna uma string onde todas as ocorrências
# do primeiro caracter são trocados por '*', exceto para o primeiro
# Assim 'abacate' retorna 'ab*c*te'
# Dica: use s.replace(stra, strb) 
def fixa_primeiro(s):
  # letra = s[0]
  # proxima = (s[1:])
  # s = (s[0] + proxima.replace(letra, '*') )
  # return s
  return s[0] + s[1:].replace(s[0], '*')

# D. mistura2
# Sejam duas strings a e b
# Retorno uma string '<a> <b>' separada por um espaço
# com as duas letras trocadas de cada string 
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
def mistura2(a, b):
  return a.replace(a[:2], b[:2]) + ' ' + b.replace(b[:2], a[:2])

# E. palindrome
# Verifique se uma string é palíndrome
#   palindrome('asa') True
#   palindrome('casa') False 
def palindrome(s):
  # return s == s[::-1]
  # ls = list(s)
  # ls.reverse()
  # return s == ''.join(ls)
  s_inverse = ''
  for index in range(len(s) - 1, -1, -1):
    s_inverse += s[index]
  return s == s_inverse
  
  # if len(s) == 3:
  #   if s[0] == s[-1]:
  #     print(True)
  #   else:
  #     print(False)
  # elif len(s) == 5:
  #   if s[0] == s[-1] and s[1] == s[-2]:
  #     print(True)
  #   else:
  #     print(False)
  # elif len(s) == 7:
  #   if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3]:
  #     print(True)
  #   else:
  #     print(False)
  # elif len(s) == 9:
  #   if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3] and s[3] == s[-4]:
  #     print(True)
  #   else:
  #     print(False)
  # elif len(s) == 11:
  #   if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3] and s[3] == s[-4] and s[4] == s[-5]:
  #     print(True)
  #   else:
  #     print(False)
  # else:
  #   print(False)
  # return print

# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4
def busca(frase, palavra):
  cont = 0
  while frase.find(palavra) != -1:
    cont += 1
    frase = frase[((frase.find(palavra))+1):]
  return cont

# Provided simple test() function used in main() toprint
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('donuts')
  test(donuts(4), 'Número de donuts: 4')
  test(donuts(9), 'Número de donuts: 9')
  test(donuts(10), 'Número de donuts: muitos')
  test(donuts(99), 'Número de donuts: muitos')

  print ()
  print ('pontas')
  test(pontas('palmeiras'), 'paas')
  test(pontas('algoritmos'), 'alos')
  test(pontas('a'), '')
  test(pontas('xyz'), 'xyyz')

  print ()
  print ('fixa_primeiro')
  test(fixa_primeiro('babble'), 'ba**le')
  test(fixa_primeiro('aardvark'), 'a*rdv*rk')
  test(fixa_primeiro('google'), 'goo*le')
  test(fixa_primeiro('donut'), 'donut')

  print ()
  print ('mistura2')
  test(mistura2('mix', 'pod'), 'pox mid')
  test(mistura2('dog', 'dinner'), 'dig donner')
  test(mistura2('gnash', 'sport'), 'spash gnort')
  test(mistura2('pezzy', 'firm'), 'fizzy perm')

  print ()
  print ('palindrome')
  test(palindrome('asa'), True)
  test(palindrome('casa'), False)

  print ()
  print ('busca')
  test(busca('ana e mariana gostam de banana', 'ana'), 4)

if __name__ == '__main__':
  main()
