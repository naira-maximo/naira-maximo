import tkinter as tk # Importar a biblioteca
from tkinter import ttk
from tkinter import END
from tkinter.messagebox import NO
from turtle import heading

lista_grupos = []

window=tk.Tk()  # Criar uma janela e instanciar a classe

# Criação da função que recolhe informações cadastradas
def criar_grupo():
    nome_lider = ent_lider.get()
    email_lider = ent_lemail.get()
    nome_client = ent_client.get()
    email_client = ent_cemail.get()
    codigo = len(lista_grupos)+1
    codigo_str = "GRUPO-{}".format(codigo)
    lista_grupos.append((codigo_str, nome_lider, email_lider, nome_client, email_client))

# Variáveis de configurações gerais
clb30=('Calibre', 30)
clb15=('Calibre', 15)
black="#000000"
grey="#a6a6a6"
pink="#fae8e8"

window.configure(bg=pink)  # Cor do plano de fundo da tela
window.title("Sistema de Cadastro - Administrador")  # Título da janela

# Título da página
lbl_titulo=tk.Label(master=window,
    text="Cadastro de Grupos",
    fg=black, bg=pink, font=clb30)
lbl_titulo.grid(row=0, column=0, padx=30, pady=20)

# Widget de texto - descrição do cadastro
lbl_desc=tk.Label(
    master=window,
    text='Após inserir os dados do Líder do Grupo e Fake Client, clique no botão "Cadastrar" para salvar as informações e criar outro grupo',
    fg=black, bg=pink, font=clb15)
lbl_desc.grid(row=1, column=0, padx=30)

# Frame cadastro de grupos
frm_grupo=tk.Frame(master=window, relief=tk.GROOVE, bd=3,
    width=1000, height=100, bg=pink)
frm_grupo.rowconfigure([0, 1], weight=1, minsize=50) 
frm_grupo.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
frm_grupo.grid(row=2, column=0, padx=30, pady=30)

frm_tabela=tk.Frame(master=window, relief=tk.FLAT, bd=1,
    width=100, height=100, bg=pink)
frm_tabela.rowconfigure(0, weight=1, minsize=100) 
frm_tabela.columnconfigure(0, weight=1, minsize=100)
frm_tabela.grid(row=3, column=0, padx=5, pady=5)

# Widget de texto - nome Líder do Grupo
lbl_lider=tk.Label(master=frm_grupo, text="Nome do Líder do Grupo:",
    fg=black, bg=pink, font=clb15)
lbl_lider.grid(row=0, column=0, sticky="e")

# Widget de entrada - nome Líder do Grupo
ent_lider=tk.Entry(master=frm_grupo, width=30, fg=black, font=('Calibre 13'))
ent_lider.grid(row=0, column=1, padx=10)

# Widget de texto - e-mail Líder do Grupo
lbl_lemail=tk.Label(master=frm_grupo, text="E-mail do Líder do Grupo:",
    fg=black, bg=pink, font=clb15)
lbl_lemail.grid(row=0, column=2, sticky="e")

# Widget de entrada - e-mail Líder do Grupo
ent_lemail=tk.Entry(master=frm_grupo, width=30, fg=black, font=('Calibre 13'))
ent_lemail.grid(row=0, column=3, padx=10)

# Widget de texto - nome Fake Client
lbl_client=tk.Label(master=frm_grupo, text="Nome do Fake Client:",
    fg=black, bg=pink, font=clb15)
lbl_client.grid(row=1, column=0, sticky="e")

# Widget de entrada - nome Fake Client
ent_client=tk.Entry(master=frm_grupo, width=30, fg=black, font=('Calibre 13'))
ent_client.grid(row=1, column=1, padx=10)

# Widget de texto - e-mail Fake Client
lbl_cemail=tk.Label(master=frm_grupo, text="E-mail do Fake Client:",
    fg=black, bg=pink, font=clb15)
lbl_cemail.grid(row=1, column=2, sticky="e")

# Widget de entrada - e-mail Fake Client
ent_cemail=tk.Entry(master=frm_grupo, width=30, fg=black, font=('Calibre 13'))
ent_cemail.grid(row=1, column=3, padx=10)

button_grupo=tk.Button(master=frm_grupo, text="Cadastrar", 
    fg=black, bg=grey, font = clb15,
    width=10, height=1, activebackground="#c5a8b0",
    command=criar_grupo)
button_grupo.grid(row=0, column=4, padx=20)

button_home=tk.Button(master=frm_grupo, text="Home", 
    fg=black, bg=grey, font = clb15,
    width=10, height=1,
    activebackground="#c5a8b0")
button_home.grid(row=1, column=4, padx=20)

tree=ttk.Treeview(master=frm_tabela, selectmode="browse", column=("nomelider", "emaillider", "nomeclient", "emailclient"), show="headings")

tree.column("nomelider", width=200, minwidth=50, stretch=NO)
tree.heading("#1", text="Nome do Líder do Grupo")

tree.column("emaillider", width=200, minwidth=50, stretch=NO)
tree.heading("#2", text="E-mail do Líder do Grupo")

tree.column("nomeclient", width=200, minwidth=50, stretch=NO)
tree.heading("#3", text="Nome do Fake Client")

tree.column("emailclient", width=200, minwidth=50, stretch=NO)
tree.heading("#4", text="E-mail do Fake Client")


tree.insert("", END, values=lista_grupos)
tree.grid(row=0, column=0)

window.mainloop()  # Método que executa eventos como cliques de botão e mantém a janela aberta