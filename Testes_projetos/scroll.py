from tkinter import *
from tkinter import ttk

# Configurações da janela
window = Tk() 
window.configure(bg='#fae8e8')  # Cor do plano de fundo da tela
window.geometry("1200x600")
window.title('Sistema de Cadastro - Administrador')  # Título da janela

# Criar um frame para comportar o canvas
frm_main=Frame(window, bg='#fae8e8')
frm_main.pack(fill=BOTH, expand=1) 

# O canvas aceita o scrollbar, mas ela só faz o papel da responsividade
canvas=Canvas(frm_main, bg='#fae8e8')
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Configurações do scrollbar
scrollbar_ver = ttk.Scrollbar(frm_main, orient=VERTICAL, command=canvas.yview) # Comando xview para orientação HORIZONTAL
scrollbar_ver.pack(side=RIGHT, fill=Y)
scrollbar_hor = ttk.Scrollbar(frm_main, orient=HORIZONTAL, command=canvas.xview) # Comando xview para orientação HORIZONTAL
scrollbar_hor.pack(side=BOTTOM, fill=X)

# Configurações do canvas
canvas.configure(yscrollcommand=scrollbar_ver.set, xscrollcommand=scrollbar_hor.set) # xscrollcomand para barra horizontal
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all'))) # Seleciona qual parte do canvas o scrollbar deve identificar

module_frame = Frame(window, bg='#fae8e8', relief=GROOVE, bd=1) # Não colocamos o frame com o .pack nesse caso

# Integração do frame geral a uma janela do canvas
canvas.create_window((0,0), window=module_frame, anchor='nw')


window.mainloop()

