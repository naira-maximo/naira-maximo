# Importar bibliotecas
from tkinter import *
from tkinter import ttk
from tkinter import END
from tkinter.messagebox import NO, YES
from turtle import heading, st
import win32com.client as win32  # Biblioteca que possibilita a interagração com o e-mail

grupo = 0

w=Tk()  # Criar uma janela e instanciar a classe

# Criação da função que recolhe informações cadastradas e gera código do grupo
def criar_grupo():
    nome_lider = ent_lider.get()
    email_lider = ent_lemail.get()
    nome_client = ent_client.get()
    email_client = ent_cemail.get()
    global grupo
    grupo += 1
    codigo_str = 'GRUPO-{}'.format(grupo)
    tree.insert('', END, values=[codigo_str, nome_lider, email_lider, nome_client, email_client])
    tree.grid(row=0, column=0, sticky='nsew')
    # Chamar função com os parâmetros "nome" e "email1"
    enviaremail(ent_lider.get(), ent_lemail.get())
    enviaremail(ent_client.get(), ent_cemail.get())

w.configure(bg='#fae8e8')  # Cor do plano de fundo da tela
w.geometry("1200x600")
w.rowconfigure(0, weight=1) 
w.columnconfigure(0, weight=1)
w.title('Sistema de Cadastro - Administrador')  # Título da janela

# Criar um frame para comportar o canvas
window=Frame(w, bg='#fae8e8', relief=GROOVE, bd=3)
window.grid(row=0, column=0, sticky="nsew")

# O canvas aceita o scrollbar, mas ela só faz o papel da responsividade
canvas=Canvas(window, bg='#fae8e8')
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Configurações do scrollbar
scrollbar_ver = ttk.Scrollbar(window, orient=VERTICAL, command=canvas.yview) # Comando xview para orientação HORIZONTAL
scrollbar_ver.pack(side=RIGHT, fill=Y)
scrollbar_hor = ttk.Scrollbar(window, orient=HORIZONTAL, command=canvas.xview) # Comando xview para orientação HORIZONTAL
scrollbar_hor.pack(side=BOTTOM, fill=X)

# Configurações do canvas
canvas.configure(yscrollcommand=scrollbar_ver.set, xscrollcommand=scrollbar_hor.set) # xscrollcomand para barra horizontal
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

frm_geral=Frame(canvas, bg='#fae8e8', relief=FLAT, bd=3) # Não colocamos o frame com o .pack nesse caso
# Integração do frame geral a uma janela do canvas
canvas.create_window((0,0), window=frm_geral, anchor='nw')

# Função para criação de texto
def criar_label(master, text, tamanho, column, row, padx, pady, sticky):
    label=Label(master=master, text=text, bg='#fae8e8', font=('Calibre', tamanho))
    label.grid(column=column, row=row, padx=padx, pady=pady, sticky=sticky)
# Textos gerais da tela
criar_label(frm_geral, 'Cadastro de Grupos', 30, 0, 0, 30, 30, 'nsew')
criar_label(frm_geral, 'Após inserir os dados do Líder do Grupo e Fake Client, clique no botão "Cadastrar" para salvar as informações e criar outro grupo.', 15, 0, 1, 30, 0, 'nsew')  
criar_label(frm_geral, 'Uma senha gerada automaticamente será enviada para o e-mail de cada um dos integrantes ao final do cadastro.', 15, 0, 2, 30, 20, 'nsew')

# Frame do cadastro de grupos
frm_grupo=Frame(frm_geral, bg='#fae8e8', relief=GROOVE, bd=3)
frm_grupo.rowconfigure([0, 1], weight=1, minsize=30) 
frm_grupo.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
frm_grupo.grid(row=3, column=0, columnspan=3, sticky='w', padx=30) # O label do prazo está muito afastado, aumentei o columnspan para aproximar

# Frame da tabela de valores cadastrados
frm_tabela=Frame(frm_geral, relief=GROOVE, bd=1, bg='#fae8e8')
frm_tabela.rowconfigure(0, weight=1, minsize=100) 
frm_tabela.columnconfigure(0, weight=1, minsize=100)
frm_tabela.place(relx=0.02, rely=0.45, relwidth=0.96, relheight=0.5)

# Widgets de entrada
ent_lider=Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # Nome Líder
ent_lider.grid(row=0, column=1, padx=5)

ent_lemail=Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # E-mail Líder
ent_lemail.grid(row=0, column=3, padx=5)

ent_client=Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # Nome Client
ent_client.grid(row=1, column=1, padx=5)

ent_cemail=Entry(master=frm_grupo, width=30, fg='#1a1d1a', font=('Calibre 13'))  # E-mail Client
ent_cemail.grid(row=1, column=3, padx=5)

criar_label(frm_grupo, 'Nome do Líder do Grupo:', 15, 0, 0, 0, 0, 'e')  # Widget de texto nome Líder do Grupo
criar_label(frm_grupo, 'E-mail do Líder do Grupo:', 15, 2, 0, 0, 0, 'e')  # Widget de texto e-mail Líder do Grupo
criar_label(frm_grupo, 'Nome do Fake Client:', 15, 0, 1, 0, 0, 'e') # Widget de texto nome Fake Client
criar_label(frm_grupo, 'E-mail do Fake Client:', 15, 2, 1, 0, 0, 'e')  # Widget de texto e-mail Fake Client

def criarbotao(nome, texto, comando, linha):
    nome=Button(master=frm_grupo, text=texto, 
    fg='#1a1d1a', bg='#d9d9d9', font=('Calibre', 15),
    width=10, height=1, activebackground='#c5a8b0',
    command=comando)
    nome.grid(row=linha, column=4, padx=5, pady=5)
criarbotao('button_grupo', 'Cadastrar', criar_grupo, 0)
criarbotao('button_home', 'Home', 0, 1)

# Tabela gerada com dados cadastrados pelo Administrador
tree=ttk.Treeview(master=frm_tabela, selectmode='browse',
    column=('codigogrupo', 'nomelider', 'emaillider', 'nomeclient', 'emailclient'),
    show="headings")

scrollver_tree = ttk.Scrollbar(frm_tabela, orient=VERTICAL, command=tree.yview) # Comando xview para orientação HORIZONTAL
scrollver_tree.grid(row=0, column=0, sticky='e')
tree.configure(yscrollcommand=scrollver_tree.set) # xscrollcomand para barra horizontal
tree.bind('<Configure>', lambda e: tree.configure(scrollregion=tree.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

def criartabela(coluna, tamanho, número, texto): 
    tree.column(coluna, width=tamanho, minwidth=50, stretch=YES)
    tree.heading(número, text=texto)

criartabela('codigogrupo', 150, '#1', 'Código do grupo')
criartabela('nomelider', 250, '#2', 'Nome do Líder do Grupo')
criartabela('emaillider', 250, '#3', 'E-mail do Líder do Grupo')
criartabela('nomeclient', 250, '#4', 'Nome do Fake Client')
criartabela('emailclient', 250, '#5', 'E-mail do Fake Client')

# Função envio de  e-mail Líder do Grupo e Fake Client
def enviaremail(nome, email1):
    outlook = win32.Dispatch('outlook.application')  # Criar interação com outlook
    email = outlook.CreateItem(0)  # Criar um e-mail

    # Configurar as informações do e-mail
    email.To = email1
    email.Subject = 'E-mail automático - Senha cadastrada para Avaliação 360°'
    email.HTMLBody = f"""
    <p>Olá, {nome}!</p>

    <p>Aqui está sua senha gerada automaticamente, para acesso à plataforma de Avaliação 360°:</p>
    <p>SENHA:</p>
    <p>E-MAIL CADASTRADO: {email1}</p>

    <p><b>Sua senha é intrasferível, não compartilhe com ninguém.</b></p>

    <p>Não responda a este e-mail.</p>
    """

    if str(object='@') in email1:
        email.Send()
        print(f'E-mail enviado para {nome}')
    else:
        print(f'Não existe e-mail cadastrado para {nome}')

window.mainloop()  # Método que executa eventos como cliques de botão e mantém a janela aberta