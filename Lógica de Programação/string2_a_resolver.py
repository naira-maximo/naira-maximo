# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras

# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
def verbing(s):
  if len(s) >= 3 and s[-3:] != 'ing':
    s = s + 'ing'
  elif s[-3:] == 'ing':
    s = s + 'ly'
  else:
    s = s
  return s

# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
  no = int(s.find('not'))
  bad = int(s.find('bad'))
  intervalo = (s[no:bad+3])
  if bad > no:
    troca = s.replace(intervalo, 'good')
  else:
    troca = s
  return troca

# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
#  a-inicio + b-inicio + a-final + b-final

def inicio_final(a, b):
  # 'string1' = len('string1') = 7 // 2 = 3 = 7 % 2 = 
  indexa = len(a)//2 + len(a)%2
  indexb = len(b)//2 + len(b)%2
  a1 = a[:indexa]
  a2= a[indexa:]
  b1 = b[:indexb]
  b2 = b[indexb:]

  return a1+b1+a2+b2

  # numero = 0
  # quantidade_a = len(a)
  # quantidade_b = len(b)
  # metade_a = (int(quantidade_a/2))
  # metade_b = (int(quantidade_b/2))
  # if quantidade_a % 2 != 0:                                                    # AVALIA A PRIMEIRA PALAVRA
  #   if quantidade_b % 2 != 0:
  #     print(f'{a[:metade_a+1]}{b[:metade_b+1]}{a[-metade_a:]}{b[-metade_b:]}')
  #   elif quantidade_b % 2 == 0 and quantidade_b != 2:
  #     print(f'{a[:metade_a+1]}{b[:metade_b]}{a[-metade_a:]}{b[-metade_b:]}')
  #   else:
  #     print(f'{a[:metade_a+1]}{b[0]}{a[-metade_a:]}{b[-metade_b:]}')
  # elif quantidade_a % 2 == 0 and quantidade_a != 2:                           # AVALIA A PRIMEIRA PALAVRA
  #   if quantidade_b % 2 != 0:
  #     print(a[:metade_a] + b[:metade_b+1] + a[-metade_a:] + b[-metade_b:])
  #   elif quantidade_b % 2 == 0 and quantidade_b != 2:
  #     print(a[:metade_a] + b[:metade_b] + a[-metade_a:] + b[-metade_b:])
  #   else:
  #     print(a[:metade_a] + b[0] + a[-metade_a:] + b[-metade_b:])
  # else:                                                                       # AVALIA A PRIMEIRA PALAVRA
  #   if quantidade_b % 2 != 0:
  #     print(a[0] + b[:metade_b+1] + a[-metade_a:] + b[-metade_b:])
  #   elif quantidade_b % 2 == 0  and quantidade_b != 2:
  #     print(a[0] + b[:metade_b] + a[-metade_a:] + b[-metade_b:])
  #   else:
  #     print(a[0] + b[0] + a[-metade_a:] + b[-metade_b:])

# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
def zf(n):
  contador = 0
  lista=str(n)
  n = lista[::-1]
  for i in n:
    if i == '0':
      contador += 1
    else:
      break
  return contador

# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
  números = []
  for i in range(0, n-1):
    números.append(str(i))
    palavra = ''.join(números)
  n = palavra.count('2')
  return n

  return

# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
  # numero = 0
  # string = str(n)
  # pot = 0
  # while str(numero)[:len(string)] != str(n):
  #   numero = 2**pot
  #   pot += 1
  # return pot-1
  str_n = str(n)
  index = 0
  while True:
    str_resultado = str(2**index)
    if str_resultado.startswith(str_n):
      break
    index += 1
  return index

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print ()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print ()
  print ('inicio_final')
  test(inicio_final('abcd', 'xy'), 'abxcdy')
  test(inicio_final('abcde', 'xyz'), 'abcxydez')
  test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

  print ()
  print ('zeros finais')
  test(zf(10100100010000), 4)
  test(zf(90000000000000000010), 1)

  print ()
  print ('conta 2')
  test(conta2(20), 2)
  test(conta2(999), 300)
  test(conta2(555), 216)

  print ()
  print ('inicio p2')
  test(inip2(7), 46)
  test(inip2(133), 316)
  test(inip2(1024), 10)
  
if __name__ == '__main__':
  main()
