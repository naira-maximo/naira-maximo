# Operadores Relacionais
# Operadores Lógicos - *, /, //, %, +, -, ** - float ou int
# Operação de Concatenção - 'str1' + 'str2' =  'str1str2'

nome = "Lucas"
idade = 45
salario = 3450.56
status = True
idade_meses = idade * 12

# <, >, <=, >=, == (=), !=
# Proposição - É uma expressão que nos leva a um valor True ou False

# Qual o seu nome? F
# O nome dele é Ricardo -  T [ nome == 'Ricardo' ]
# A media da turma é maior que 7,5 - T [ media_turma >= 7.5 ]
# Tabela Verdade - ~p, p ^ q, p v q
print( 4 >= 6.7 )
print( 4 <= 6.7 )
print( 4 < 6.7 )
print( 4 > 6.7 )
print( 4 == 6.7 )
print( 4 != 6.7 )

# Operadores Lógicos

# Tabela Verdade - ~p, p ^ q, p v q
# Python Operadores Lógicos
# ~ - not (!)
# ^ - and (&&)
# v - or (||) - or != xor
# or (ou inlusivo)
# xor (ou exclusiv)

# p | q | p or q | p xor q
# V   V     V         F
# V   F     V         V
# F   V     V         V
# F   F     F         F

# a = 2 (0010) a xor b = 0100 = 4
# b = 6 (0110)

print( 4 >= 6.7 )
print( 4 <= 6.7 )
print( 4 < 6.7 )
print( 4 > 6.7 )
print( 4 == 6.7 )
print( 4 != 6.7 )

print( 3 < 25 or 45 < 34 ) # True
print( 25 < 3 or 45 < 34 ) # False
print( 3 < 25 and 34 < 45 ) # True

# while - enquanto
# if, if..else, if...elif...else - se...então...senão

velocidade = int(input("Informe sua velocidade: "))
valor_multa = 0.0

if velocidade > 110:
    valor_multa = (velocidade - 110) * 5.0 # operador ternário

print(f'O valor da multa é {valor_multa:.2f}.')