# 1. Indique o tipo dos seguintes valores: 5, 5.0, 4.3, -2, 100, 1.333, “10”
# 2. Experimente digitar type(x) onde x é cada um dos valores acima no Python interativo
# 3. É possível calcular 2 elevado a um milhão?

a = 5
b = 5.0
c = 4.3
d = -2
e = 100
f = 1.333
g = '10'

print(f'O tipo da variável {a} é {type(a)}')
print(f'O tipo da variável {b} é {type(b)}')
print(f'O tipo da variável {c} é {type(c)}')
print(f'O tipo da variável {d} é {type(d)}')
print(f'O tipo da variável {e} é {type(e)}')
print(f'O tipo da variável {f} é {type(f)}')
print(f'O tipo da variável {g} é {type(g)}')

a = 2
b = 1000000
resultado = a**b
print(float(resultado))

# OverflowError: int too large to convert to float
# OverflowError: (34, 'Result too large')

# Números em ponto flutuante podem não ter representação exata no sistema binário
# • Ex.: Digitando no interpretador 3*0.1 teremos como resposta 0.30000000000000004
# • Mas digitando print(“%.1f” %(3*0.1)) teremos 0.3
