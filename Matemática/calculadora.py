from tkinter import *
# CALCULADORA SIMPLES
# Elaborado por Naira Giulia Pereira Maximo dos Santos, utilizando como referência o vídeo do canal Rota da Programação, disponível em: https://www.youtube.com/watch?v=i24MxljM-Bw
# Calculadora de operações básicas criada com o intuito de treinar a linguagem de programação Python e listas.
# Pretendo implementar essa calculadora com operações mais complexas, como uma calculadora científica. 

# Relação de cores da janela
cor1 = '#3B3B3B'
cor2 = '#FEFFFF'
cor3 = '#38576B'
cor4 = '#ECEFF1'
cor5 = '#FFAB40'

# Estrutura da janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310+500+200')
janela.config(bg=cor1)
janela.resizable(width=False, height=False)

# Criando tela de resultados
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

# Criando corpo da calculadora para receber os botões
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Funções da calculadora
todos_valores = ''
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

valor_texto = StringVar()

# Tela da calculadora
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

x = [118, 177, 0, 59, 118, 177, 0, 59, 118, 177, 0, 59, 118, 177, 118]
y = [0, 0, 52, 52, 52, 52, 104, 104, 104, 104, 156, 156, 156, 156, 208]
texto = ['%', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '.',]

# Botões por linha
def criar_botao(command, text, x, y, width=5):
    b = Button(frame_corpo, command = lambda: entrar_valores(command), text=text, width=width, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b.place(x=x, y=y)

for i, botao in enumerate(x):
    criar_botao(texto[i], texto[i], x[i], y[i])

criar_botao('0', '0', 0, 208, 11)

b_resultado = Button(frame_corpo, command = lambda: calcular(), text='=', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_resultado.place(x=177, y=208)

janela.mainloop()

