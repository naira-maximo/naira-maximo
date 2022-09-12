import tkinter as tk # Importar a biblioteca
from tkinter import ttk
window=tk.Tk()  # Criar uma janela e instanciar a classe
window.title("Sistema de Cadastro - Administrador")  # Título da janela

# Variáveis de configurações gerais
clb30=('Calibre', 30)
clb15=('Calibre', 15)
pink="#fae8e8"

# Configurações da página
window.configure(bg=pink)  # Cor do plano de fundo da tela

# Frame do título
frametitulo=tk.Frame(
    master=window,
    width=500,
    height=100,
    bg=pink)

# Frame do cadastro de grupos
frame1=tk.Frame(
    master=window,
    relief=tk.GROOVE,
    borderwidth=3,
    width=1000,
    height=100,
    bg=pink
)

# Título da página
title=tk.Label(  # Widget de texto
    master=frametitulo,
    text="Cadastrar Grupos",
    fg="black",
    bg=pink,
    font=clb30
)
title.place(x=35, y=35)  # Adicionar o widget à janela

# Dividir o Frame em linhas e colunas
window.rowconfigure(0, weight=1, minsize=50) 
window.columnconfigure([0, 1, 2], weight=1, minsize=100)

lbl_grupos=tk.Label(
    master=frame1,
    text="Para criar um Grupo, cadastre o Líder e o Fake Client",
    fg="black",
    bg=pink,
    font=clb15,
    width=20
)
lbl_grupos.grid(row=0, column=0)

ent_grupo=tk.Entry(master=frame1, font=clb15, width=20)
ent_grupo.grid(row=0, column=1)

buttonlider=tk.Button(
    master=frame1,
    text="Cadastrar",
    fg="black",
    bg="#c5a8b0",
    font = clb15,
    width=10,
    height=1,
    activebackground="#26413c",
    command=inserir_grupos()
)
buttonlider.grid(row=0, column=2, padx=30, pady=20)
# padx: preenchimento horizontal pady: preenchimento vertical

frametitulo.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame1.place(x=30, y=100)

frame2 = tk.Frame(master=frame1, relief=tk.FLAT, width=900, height=500, bg=pink)

grupo1 = tk.Label(master=frame2, text="Grupo 1", fg="black", bg=pink, font=clb15, width=20)
grupo2 = tk.Label(master=frame2, text="Grupo 2", fg="black", bg=pink, font=clb15, width=20)
grupo3 = tk.Label(master=frame2, text="Grupo 3", fg="black", bg=pink, font=clb15, width=20)
grupo4 = tk.Label(master=frame2, text="Grupo 4", fg="black", bg=pink, font=clb15, width=20)
grupo5 = tk.Label(master=frame2, text="Grupo 5", fg="black", bg=pink, font=clb15, width=20)

nomelider1 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)
nomelider2 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)
nomelider3 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)
nomelider4 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)
nomelider5 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)

emaillider1 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)
emaillider2 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)
emaillider3 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)
emaillider4 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)
emaillider5 = tk.Entry(master=frame2, font = ("Calibre", 15), width=20)

window.mainloop()  # Método que executa eventos como cliques de botão
