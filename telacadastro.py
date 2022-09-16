import tkinter as tk # Importar a biblioteca
from tkinter import ttk
window=tk.Tk()  # Criar uma janela e instanciar a classe
window.title("Sistema de Cadastro - Administrador")  # Título da janela

# Configurações da página
window.configure(bg="#fae8e8")  # Cor do plano de fundo da tela

# Frame do cadastro de grupos
frame1=tk.Frame(
    master=window,
    relief=tk.GROOVE,
    borderwidth=3,
    width=1000,
    height=100,
    bg="#fae8e8"
)

# Título da página
title=tk.Label(  # Widget de texto
    master=window,
    text="Cadastrar Grupos",
    fg="#000000",
    bg="#fae8e8",
    font=('Calibre', 30)
)
title.grid(row=0, column=0, padx=20, pady=20, sticky="w")  # Adicionar o widget à janela

lbl_grupos=tk.Label(
    master=frame1,
    text="Quantidade de grupos: ",
    fg="#000000",
    bg="#fae8e8",
    font=('Calibre', 15),
    width=20
)
lbl_grupos.grid(row=0, column=0)

ent_grupo=tk.Entry(master=frame1, font=('Calibre', 15), width=20)
ent_grupo.grid(row=0, column=1)

buttonlider=tk.Button(
    master=frame1,
    text="Cadastrar",
    fg="#000000",
    bg="#c5a8b0",
    font =('Calibre', 15),
    width=10,
    height=1,
    activebackground="#26413c"
)
buttonlider.grid(row=0, column=2, padx=30, pady=20)
# padx: preenchimento horizontal pady: preenchimento vertical

frame1.grid(row=1, column=0, padx= 20)

frame2 = tk.Frame(master=frame1, relief=tk.FLAT, width=900, height=500, bg="#fae8e8")

grupo1 = tk.Label(master=frame2, text="Grupo 1", fg="#000000", bg="#fae8e8", font=('Calibre', 15), width=20)
grupo2 = tk.Label(master=frame2, text="Grupo 2", fg="#000000", bg="#fae8e8", font=('Calibre', 15), width=20)
grupo3 = tk.Label(master=frame2, text="Grupo 3", fg="#000000", bg="#fae8e8", font=('Calibre', 15), width=20)
grupo4 = tk.Label(master=frame2, text="Grupo 4", fg="#000000", bg="#fae8e8", font=('Calibre', 15), width=20)
grupo5 = tk.Label(master=frame2, text="Grupo 5", fg="#000000", bg="#fae8e8", font=('Calibre', 15), width=20)

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
