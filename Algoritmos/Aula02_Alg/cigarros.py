# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))

def menos_vida(anos, cigarros):
    dias_por_ano = anos*365
    minutos = dias_por_ano*1440
    cigarros_por_dia = cigarros*dias_por_ano
    menos_minutos = (minutos/10) - cigarros_por_dia
    menos_dias = menos_minutos/1440
    return menos_dias

passado = menos_vida(anos, cigarros)
futuro = menos_vida(5, cigarros)
print(f'Você perdeu {passado:.0f} dias de vida fumando {cigarros} cigarros por dia durante {anos} anos. Se continuar fumando a mesma quantidade de \
cigarros, perderá {futuro:.0f} dias nos próximos 5 anos.')