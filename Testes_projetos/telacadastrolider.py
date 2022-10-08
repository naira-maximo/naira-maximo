from tkinter import *
from tkinter import ttk

# cores
co0 = "#FAE8E8" #rosa
co1 = "#D9D9D9" #cinza
co2 = "#1A1D1A" #preta

window=Tk()  # Criar uma janela e instanciar a classe
scrollbar = Scrollbar(window) 
scrollbar.pack( side = RIGHT, fill = Y)

# função de criar frame
def criar_frame(quadro, row, column):
    frame = Frame(quadro, background = co0, relief=FLAT, bd=1)
    frame.rowconfigure(row, minsize = 10)  # Quantas linhas o frame terá
    frame.columnconfigure(column, minsize = 100)  # Quantas colunas o frame terá
    frame.grid(row=row, column=column, padx=10, sticky='w') # Local onde o frame será colocado

# criar widgets ###quadro é se seá colocado na janela ou em frame
def criar_label(quadro, text, font, r, c, name=None):
    if name is not None:
        label = Label(quadro, text=text, font=font, background=co0, name=name)
    else:
        label = Label(quadro, text=text, font=font, background=co0)
        label.grid(row=r, column=c, padx=5, pady=3, sticky = "w")

def criar_entry(quadro, font, r, c, name=None):
    if name is not None:
        entry = Entry(quadro, font = font, justify = "left", name=name)
    else:
        entry = Entry(quadro, font = font, justify = "left")
        entry.grid(row=r, column=c, padx=5, pady=3, sticky = "w")

def criar_button(quadro, text, font, r, c, command, name=None):
    if name is not None:
        button = Button(quadro, text = text, font = font, height = 0, command = command, name=name)
    else:
        button = Button(quadro, text = text, font = font, height = 0, command = command)
        button.grid(row=r, column=c, padx=5, pady=3, sticky = "w")

def get_entries(parent):
    lista = []
    for child in parent.winfo_children():
        if type(child) is Entry:
            lista.append(child)

    # função que pegar o valor da caixa de entrada do "n° de sprints, ao apertar o button.
    # essa função também "abre um frame" para que as linhas referentes ao cadastro da sprint sejam encaixadas
    def entry_sprint():
        try:
            valor = int(en_numsprints.get())
        except:
            return
        # frame_sprint = criar_frame(janela, valor, 4, 3, 2)
        frame_sprint = criar_frame(frame_parent_sprints, valor, 0)
        for i in range(valor):
            criar_label(frame_sprint, f"Sprint {i+1}", "Calibri, 10", i, 0)
            criar_label(frame_sprint, "Início:", "Calibri, 10", i, 1)
            criar_entry(frame_sprint, "Calibri, 10", i, 2)
            criar_label(frame_sprint, "Fim:", "Calibri, 10", i, 3)
            criar_entry(frame_sprint, "Calibri, 10", i, 4)
            criar_label(frame_sprint, "Dias para avaliação:", "Calibri, 10", i, 5)
            criar_entry(frame_sprint, "Calibri, 10", i, 6)

    def entry_times():
        valor = get_entry_int(en_numtimes)
        for i in range(valor):
            row = i
            frame_time = criar_frame(frame_parent_times, row, 0)
            # lista_frame_time.append(frame_time)

            frame_time_data = criar_frame(frame_time, 0, 0)
            criar_label(frame_time_data, f"Time {i+1}",          "Calibri, 10", row, 0)
            # criar_label(frame_time_data, "Nome", "Calibri, 10", row, 1)
            criar_entry(frame_time_data,                          "Calibri, 10", row, 2)
            criar_label(frame_time_data, "Quantidade de alunos:", "Calibri, 10", row, 3)
            criar_entry(frame_time_data,                          "Calibri, 10", row, 4, name="q_alunos")
            # lista.append(criar_button(frame_time_data, "Cadastrar", "Calibri, 10", i, 3, command = entry_alunos(en_numalunos)))
            criar_button(frame_time_data, "Cadastrar",           "Calibri, 10", row, 5, command = update_member_forms)

    # Atualiza a tela para criar os formularios para cada membro de acordo com o numero de membros especificado em cada time
    def update_member_forms():

        # acessa a lista global de frames de time
        # global lista_frame_time

        # pra cada frame_time da lista
        for ft_index, frame_time in enumerate(frame_parent_times.winfo_children()):

            e = frame_time.winfo_children()[0].children["q_alunos"]
            print('e is "', e, '"')

            num_alunos = get_entry_int(e)
            print('num_alunos ', num_alunos)


            members_parent = reset_or_create_frame(frame_time, 1, ft_index + 1)

            # se nenhum aluno for cadastrado nesse time,
            # significa que não há mais nenhum passo a ser executado para o frame_time atual, continue o loop 
            if num_alunos < 1:
                continue 

            num_alunos = (lambda x : 0 if x == 0 else (3 if x < 3 else (9 if x > 9 else x)))(num_alunos)
            print(num_alunos)

            # para cada aluno, cria um formulário de cadastro
            for i in range(num_alunos):
                criar_formulario_aluno(members_parent, i)

    def reset_or_create_frame(parent:Frame, index:int, row:int):

        # tenta executar o proximo código
        try:

            # acessa o child de index 1 (frame) no parent
            frame = parent.winfo_children()[index]
            # print(f"frame já existe: {frame}")

            # deleta o frame
            frame.destroy()

        # caso não encontre o frame dentro do parent:
        # frame não existe
        except:
            """"""
            # print("frame doesn't exist")
        
        # pelo menos 1 aluno será cadastrado, crie o frame para armazenar o formulario
        frame = criar_frame(parent, row, 0)

        # Retorna o frame
        return frame

    # Retorna o valor na entry especificada
    def get_entry_int (entry):

        # tenta acessar o valor na entry especificada e retorná-lo como int
        try:
            return int(entry.get())

        # em caso de erro, retorne 0
        except:
            print("erro")
            return 0

    # Cria os campos para o cadastro de UM aluno
    def criar_formulario_aluno (parent, row):
        aluno = criar_frame(parent, row, 0)
        criar_label(aluno, "Nome:",  "Calibri, 10", row, 0)
        criar_entry(aluno,           "Calibri, 10", row, 1)
        criar_label(aluno, "E-mail:","Calibri, 10", row, 2)
        criar_entry(aluno,           "Calibri, 10", row, 3)
        criar_label(aluno, "Função:","Calibri, 10", row, 4)
        criar_entry(aluno,           "Calibri, 10", row, 5)
        # TODO:
        # from Roles.Role import *
        # roles = ...
        # criar_dropdown(parent, roles,"Calibri, 10", row, 5)

    # HIERARQUIA:
    #
    #            janela
    #            |
    #            |   janela_header                       # contém o titulo "Cadastro"
    #            |
    #            |   frame_section0                      # separa a primeira seção da janela
    #            |   |
    #            |   |   sprints_header                  # contem o cabeçalho do cadastro de sprints
    #            |   |   frame_parent_sprints            # contem cada sprint
    #            |   |   |   sprint_form                 # um sprint_form para cada sprint
    #            |   |   |   ...
    #            |   |
    #            |
    #            |   frame_section1                      # separa a segunda seção da janela
    #            |   |
    #            |   |   teams_header                    # contem o cabeçalho do cacdastro de times
    #            |   |   frame_parent_times              # contem cada frame_time
    #            |   |   |
    #            |   |   |   frame_time                  # um frame_time para cada time
    #            |   |   |   |   members_parent          # intermédio entre frame_time e cada membro
    #            |   |   |   |   |   member_form         # contem o formulário de um membro
    #            |   |   |   |   |   
    #            |   |   |   |      
    #            |   |   |   frame_time[...]
    #            |   |   |   frame_time[...]
    #            |   |   |
    #            |   |
    #            |

    # criando a janela
    # janela = Tk()
    # janela.configure(bg=co0)
    # janela.title('Sistema de Cadastro - Administrador')
    # janela.geometry("1200x600")

    janela = criar_frame(frame_parent, 0, 0)

    # aqui coloco o tamanho da tela, largura x altura
    # tentativa de dar numero de linhas e colunas para a tabela. Se deixo ativado, os labels ficam espalhados pela tela.
    # janela.rowconfigure([0,1,2,3], weight = 1, minsize=30)
    # janela.columnconfigure([0,1,2], weight = 1, minsize=30)
    # janela.configure(background=co0)
    # janela.grid_rowconfigure(0, weight=1)
    # janela.grid_columnconfigure(0, weight=1)

    # lista_frame_time = []

    # janela_header
    titulo=Label(janela, text='Cadastro de Times', bg='#fae8e8', font=('Calibre', 30))
    titulo.grid(row=0, column=0, padx=30, pady=10, sticky='w')

    # frame_body = Frame(janela)
    # frame_body.pack(fill=BOTH, expand=1)


    # frame_body = criar_frame(janela, 1, 0)
    frame_body = Frame(janela, bg=co0)
    frame_body.grid(row=1, column=0)

    # frame_body.grid_rowconfigure(0, weight=1)
    # frame_body.grid_columnconfigure(0, weight=1)

    # canvas = Canvas(frame_body)
    # canvas.place(relwidth=1, relheight=1)
    # ttk.Scrollbar(frame_body, orient=VERTICAL, command=canvas.yview).place(relx=1, y=0, relheight=1)

    # frame_body.grid_rowconfigure(0, weight=1)
    # frame_body.grid_columnconfigure(0, weight=1)
    # frame_body.grid_propagate(False)

    # canvas = Canvas(frame_body, bg="yellow")
    # canvas = Canvas(frame_body)
    # canvas.grid(row=0, column=0, sticky="nsew")
    # photoScroll = Scrollbar(frame_body, orient=VERTICAL)
    # photoScroll.config(command=canvas.yview)
    # canvas.config(yscrollcommand=photoScroll.set)
    # photoScroll.grid(row=0, column=1, sticky="ns")
    # def update_scrollregion(event):
    #     canvas.configure(scrollregion=canvas.bbox("all"))

    # canvas.bind("<Configure>", update_scrollregion)

    # cria a seção de sprints
    frame_section0 = criar_frame(frame_body, 1, 0)
    # frame_section0.grid_rowconfigure(0, weight=1)
    # frame_section0.grid_columnconfigure(0, weight=1)

    frame_sprints = criar_frame(frame_section0, 0, 0)
    # frame_sprints.grid_rowconfigure(0, weight=1)
    # frame_sprints.grid_columnconfigure(0, weight=1)


    # título
    criar_label(frame_sprints, "Sprints", "Calibri, 12", 0, 0)

    # input: label, entry, button
    criar_label(frame_sprints, "Número de Sprints:    ", "Calibri, 10", 1, 0)
    en_numsprints = criar_entry(frame_sprints, "Calibri, 10", 1, 1)
    criar_button(frame_sprints, "Cadastrar", "Calibri, 10", 1, 2, command = entry_sprint)

    # data: list-wrapper
    frame_parent_sprints = criar_frame(frame_section0, 2, 0)
    # frame_parent_sprints.grid_rowconfigure(0, weight=1)
    # frame_parent_sprints.grid_columnconfigure(0, weight=1)


    # TODO:
    # Cria uma 'section' de acordo com a seguinte hierarquia:
    #           section
    #           |   header
    #           |   |   title
    #           |   |   header_data     (ex.: [label, entry, button])
    #           |   section_data        (ex.: [list-wrapper])
    #
    # Onde 'section' contém 'header' e 'section_data' e
    #      'header' contém 'title' e 'header_data'
    #
    # '...._data' corresponde a uma lista de parametros a serem convertidos em widgets
    # def create_section (window, row, title, header_data, ):
    #     frame_section = criar_frame(window, row, 0)


    # cria a seção de times
    frame_section1 = criar_frame(frame_body, 2, 0)
    # frame_section1.grid_rowconfigure(0, weight=1)
    # frame_section1.grid_columnconfigure(0, weight=1)

    times_header = criar_frame(frame_section1, 0, 0)
    # times_header.grid_rowconfigure(0, weight=1)
    # times_header.grid_columnconfigure(0, weight=1)


    # título
    criar_label(times_header, "Times", "Calibri, 12", 0, 0)

    # input: label, entry, button
    criar_label(times_header, "Quantidade de Times:", "Calibri, 10", 1, 0)
    en_numtimes = criar_entry(times_header, "Calibri, 10", 1, 1)
    criar_button(times_header, "Cadastrar", "Calibri, 10", 1, 2, command = entry_times)

    # data: list-wrapper
    frame_parent_times = criar_frame(frame_section1, 2, 0)
    # frame_parent_times.grid_rowconfigure(0, weight=1)
    # frame_parent_times.grid_columnconfigure(0, weight=1)


    def confirmar_cadastros():
        from Sprints.Sprints import create_sprint
        from Users.Authentication import CURRENT_USER
        def to_date(value:str):
            from datetime import date
            l = value.split('/')
            return date(int(l[0]), int(l[1]), int(l[2]))
        # get sprints
        sprints = frame_parent_sprints.winfo_children()
        # for each sprint:
        for sprint in sprints:
        # try:
            s_entries = get_entries(sprint)
            inicio = to_date(s_entries[0].get())
            fim =    to_date(s_entries[1].get())
            periodo = get_entry_int(s_entries[2])
            create_sprint(CURRENT_USER.group_id, inicio, fim, periodo)
        # except:
            print(f'Erro ao criar sprint! {sprint}')

        from Users.Authentication import create_team, register
        # get teams
        times = frame_parent_times.winfo_children()
        for time in times:
            time_data = time.winfo_children()[0]
        #   name
            name = str(get_entries(time_data)[0].get())
        #   save team
            team_id = create_team(name, CURRENT_USER.group_id)
        #   for each member:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(time.winfo_children()[1])
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(time.winfo_children()[1].winfo_children())
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            for member in time.winfo_children()[1].winfo_children():
                print(f'member {member}')
                # m_entries = get_entries(member)
                # print(f'm_entries {member.winfo_children()}')
                m_name = member.winfo_children()[1].get()
                m_email = member.winfo_children()[3].get()
                m_role = get_entry_int(member.winfo_children()[5])
        #       register(member)
                register(m_name, m_email, CURRENT_USER.group_id, team_id, m_role)


    Button(janela, text="Confirmar Cadastros", font="Calibri, 14", command=confirmar_cadastros).grid(row=0, column=1, sticky='e')

    return janela


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

frm_geral=Frame(canvas, bg='#fae8e8', relief=FLAT, bd=3) # Não colocamos o frame com o .pack nesse caso

# Integração do frame geral a uma janela do canvas
canvas.create_window((0,0), window=frm_geral, anchor='nw')

frame_body = Frame(module_frame, bg=co0)
frame_body.grid(row=1, column=0)