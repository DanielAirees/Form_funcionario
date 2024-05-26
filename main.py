from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import re
import datetime
import crud
           

class App:
    def __init__(self, janela):
        self.Objeto = crud.AppBD()

# criando o Frame do Logo

        self.frame_logo = ctk.CTkFrame(
            master=janela, width=900, height=50, fg_color='#DAA520', corner_radius=0)
        self.frame_logo.place(x=0, y=0)

        self.titulo = ctk.CTkLabel(
            self.frame_logo, text='CADASTRO DE FUNCIONÁRIOS', font=('Helvetica', 28, 'bold'))
        self.titulo.place(x=190, y=10)

        # Criando o switch para mudar aparência
        a = ctk.BooleanVar()
        self.modo = ctk.CTkSwitch(
            self.frame_logo, text="Modo", variable=a, command=self.trocar_modo, progress_color='#4169E1')
        self.modo.place(x=750, y=15)

# ---------------------------------------------------------------------------------

# Criando o Frame Formulário

        self.frame_formulario = ctk.CTkFrame(janela, width=240, height=370)
        self.frame_formulario.place(x=10, y=55)

        # elementos do Frame Formulário
        self.dados_pessoais = ctk.CTkLabel(self.frame_formulario, text='DADOS PESSOAIS', font=('Helvetica', 14))
        # self.linha = ttk.Separator(self.frame_formulario, orient='horizontal')
        self.linha = ttk.Label(self.frame_formulario, relief='groove', text='h',font=('ivy 1'), background='silver')

        self.nome = ctk.CTkLabel(self.frame_formulario, text='Nome Completo', font=('Helvetica', 14))
        self.ent_nome = ctk.CTkEntry(self.frame_formulario, width=200, corner_radius=5, height=15, validate="key")
        max_digitos = 100
        self.ent_nome.configure(validatecommand=(self.frame_formulario.register(self.validar_str), '%P', max_digitos))

        self.rg = ctk.CTkLabel(self.frame_formulario, text='RG', font=('Helvetica', 14))
        self.ent_rg = ctk.CTkEntry(self.frame_formulario, width=110, validate="key", 
                                   placeholder_text='Apenas números', corner_radius=5, height=15)
        max_digitos = 8
        self.ent_rg.configure(validatecommand=(self.frame_formulario.register(self.validar_num), '%P', max_digitos))

        self.dt_nasc = ctk.CTkLabel(self.frame_formulario, text='Data de Nascimento', font=('Helvetica', 14))
        self.ent_dt_nasc = ctk.CTkEntry(self.frame_formulario, width=130, placeholder_text='dd/mm/aaaa', corner_radius=5, height=15)
                     
        self.orgaoEmissor = ctk.CTkLabel(self.frame_formulario, text='Orgão Emissor', font=('Helvetica', 14))
        self.ent_orgaoEmissor = ctk.CTkEntry(self.frame_formulario, width=80, corner_radius=5, height=15, validate="key")
        max_digitos = 10
        self.ent_orgaoEmissor.configure(validatecommand=(self.frame_formulario.register(self.validar_str), '%P', max_digitos))

        self.cpf = ctk.CTkLabel(self.frame_formulario, text='CPF', font=('Helvetica', 14))
        self.ent_cpf = ctk.CTkEntry(self.frame_formulario, width=130, placeholder_text='Apenas números', corner_radius=5, height=15, validate="key")
        max_digitos = 11
        self.ent_cpf.configure(validatecommand=(self.frame_formulario.register(self.validar_num), '%P', max_digitos))

        self.genero = ctk.CTkLabel(self.frame_formulario, text='Gênero', font=('Helvetica', 14))
        self.genero_lista = ["masculino", "Feminino", "Outro"]
        self.combo_genero = ctk.CTkComboBox(
            self.frame_formulario, values=self.genero_lista, width=130, corner_radius=5, font=('Helvetica', 12), height=15, state="readonly")
        self.combo_genero.set(self.genero_lista[0])
        
        self.ddd = ctk.CTkLabel(self.frame_formulario, text='DDD', font=('Helvetica', 14))
        self.ent_ddd = ctk.CTkEntry(self.frame_formulario, width=60, corner_radius=5, height=15, validate="key")
        max_digitos = 2
        self.ent_ddd.configure(validatecommand=(self.frame_formulario.register(self.validar_num), '%P', max_digitos))
        
        self.tel = ctk.CTkLabel(self.frame_formulario, text='Telefone', font=('Helvetica', 14))
        self.ent_tel = ctk.CTkEntry(self.frame_formulario, width=130, placeholder_text='Apenas números', corner_radius=5, height=15, validate="key")
        max_digitos = 9
        self.ent_tel.configure(validatecommand=(self.frame_formulario.register(self.validar_num), '%P', max_digitos))

        # Posicionamento dos elementos do Frame Formulário
        self.dados_pessoais.place(x=60, y=10)
        self.linha.place(x=10, y=50, width=280)

        self.nome.place(x=10, y=50)
        self.ent_nome.place(x=10, y=72)

        self.rg.place(x=10, y=150)
        self.ent_rg.place(x=10, y=172)

        self.orgaoEmissor.place(x=130, y=150)
        self.ent_orgaoEmissor.place(x=130, y=172)

        self.cpf.place(x=10, y=100)
        self.ent_cpf.place(x=10, y=122)

        self.genero.place(x=10, y=200)
        self.combo_genero.place(x=10, y=222)

        self.dt_nasc.place(x=10, y=250)
        self.ent_dt_nasc.place(x=10, y=272)   

        self.ddd.place(x=10, y=300)
        self.ent_ddd.place(x=10, y=322)   

        self.tel.place(x=80, y=300)
        self.ent_tel.place(x=80, y=322)    

# --------------------------------------------------------------------------------- 
        # Criando o Frame Endereço

        self.frame_endereco = ctk.CTkFrame(janela, width=250, height=370)
        self.frame_endereco.place(x=254, y=55)

        self.endereco = ctk.CTkLabel(self.frame_endereco, text='ENDEREÇO', font=('Helvetica', 14))
             
        self.linha = ttk.Label(self.frame_endereco, relief='groove', text='h',font=('ivy 1'), background='silver')
         
        self.cep = ctk.CTkLabel(self.frame_endereco, text='CEP', font=('Helvetica', 14))
        self.ent_cep = ctk.CTkEntry(self.frame_endereco, width=100, placeholder_text='Apenas números', corner_radius=5, height=15, validate="key")
        max_digitos = 8
        self.ent_cep.configure(validatecommand=(self.frame_endereco.register(self.validar_num), '%P', max_digitos))

        self.cidade = ctk.CTkLabel(self.frame_endereco, text='Cidade', font=('Helvetica', 14))
        self.ent_cidade = ctk.CTkEntry(self.frame_endereco, width=150, corner_radius=5, height=15, validate="key")
        max_digitos = 50
        self.ent_cidade.configure(validatecommand=(self.frame_endereco.register(self.validar_str), '%P', max_digitos))

        self.estado = ctk.CTkLabel(self.frame_endereco, text='Estado', font=('Helvetica', 14))
        self.estado_lista = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
                                'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        self.combo_estado = ctk.CTkComboBox(
            self.frame_endereco, values=self.estado_lista, width=60, corner_radius=5, font=('Helvetica', 12), height=15, state='readonly')
        self.combo_estado.set(self.estado_lista[0])

        self.bairro = ctk.CTkLabel(self.frame_endereco, text='Bairro', font=('Helvetica', 14))
        self.ent_bairro = ctk.CTkEntry(self.frame_endereco, width=220, corner_radius=5, height=15, validate="key")
        max_digitos = 50
        self.ent_bairro.configure(validatecommand=(self.frame_endereco.register(self.validar_str), '%P', max_digitos))

        self.rua = ctk.CTkLabel(self.frame_endereco, text='Rua', font=('Helvetica', 14))
        self.ent_rua = ctk.CTkEntry(self.frame_endereco, width=220, corner_radius=5, height=15, validate="key")
        max_digitos = 100
        self.ent_rua.configure(validatecommand=(self.frame_endereco.register(self.validar_str), '%P', max_digitos))

        self.numero = ctk.CTkLabel(self.frame_endereco, text='Número', font=('Helvetica', 14))
        self.ent_numero = ctk.CTkEntry(self.frame_endereco, width=50, corner_radius=5, height=15, validate="key")
        max_digitos = 5
        self.ent_numero.configure(validatecommand=(self.frame_endereco.register(self.validar_num), '%P', max_digitos))

        self.complemento = ctk.CTkLabel(self.frame_endereco, text='Complemento', font=('Helvetica', 14))
        self.ent_complemento = ctk.CTkEntry(self.frame_endereco, width=160, corner_radius=5, 
                                            height=15,placeholder_text='(opcional)', validate="key")
        max_digitos = 100
        self.ent_complemento.configure(validatecommand=(self.frame_endereco.register(self.validar_str), '%P', max_digitos))


        # Posicionando os elementos no Frame Endereço
        self.endereco.place(x=90, y=10)
        self.linha.place(x=10, y=50, width=290)

        self.cep.place(x=10 ,y=50)
        self.ent_cep.place(x=10, y=72)

        self.cidade.place(x=10 ,y=100)
        self.ent_cidade.place(x=10 ,y=122)

        self.estado.place(x=170 ,y=100)
        self.combo_estado.place(x=170, y=122)

        self.bairro.place(x=10 ,y=150)
        self.ent_bairro.place(x=10, y=172)

        self.rua.place(x=10, y=200)
        self.ent_rua.place(x=10, y=222)

        self.numero.place(x=10 ,y=250)
        self.ent_numero.place(x=10 ,y=272)

        self.complemento.place(x=70 ,y=250)
        self.ent_complemento.place(x=70 ,y=272)
    
# --------------------------------------------------------------------------------- 
        # Criando o Frame Dados Profissionais

        self.frame_dados_prof = ctk.CTkFrame(janela, width=210, height=370)
        self.frame_dados_prof.place(x=508, y=55)

        self.dados_profissionais = ctk.CTkLabel(self.frame_dados_prof,text='DADOS PROFISSIONAIS', font=('Helvetica', 14))
        # self.linha = ttk.Separator(self.frame_dados_prof, orient='horizontal')
        self.linha = ttk.Label(self.frame_dados_prof, relief='groove', text='h',font=('ivy 1'), background='silver')
        
        self.id = ctk.CTkLabel(self.frame_dados_prof, text="Matrícula", font=('Helvetica', 14))
        self.ent_id = ctk.CTkEntry(self.frame_dados_prof, width=100, corner_radius=5, height=15, validate="key")
        max_digitos = 6
        self.ent_id.configure(validatecommand=(self.frame_dados_prof.register(self.validar_num), '%P', max_digitos))

        self.dt_contratacao = ctk.CTkLabel(self.frame_dados_prof, text='Data de Contratação', font=('Helvetica', 14))
        self.ent_dt_contratacao = ctk.CTkEntry(self.frame_dados_prof, width=130, 
                                               placeholder_text='dd/mm/aaaa', corner_radius=5, height=15)
              

        self.cargo = ctk.CTkLabel(self.frame_dados_prof, text='Cargo', font=('Helvetica', 14))
        self.ent_cargo = ctk.CTkEntry(self.frame_dados_prof, width=130, corner_radius=5, height=15, validate="key")
        max_digitos = 50
        self.ent_cargo.configure(validatecommand=(self.frame_dados_prof.register(self.validar_str), '%P', max_digitos))

        self.area = ctk.CTkLabel(self.frame_dados_prof, text='Área', font=('Helvetica', 14))
        self.area_lista = ["Administrativo", "Comercial", "Financeiro", "Operacional", "RH"]
        self.combo_area = ctk.CTkComboBox(
            self.frame_dados_prof, values=self.area_lista, width=130, corner_radius=5, font=('Helvetica', 12), height=15, state="readonly")
        self.combo_area.set(self.area_lista[0])

        self.nivel = ctk.CTkLabel(self.frame_dados_prof, text='Nível', font=('Helvetica', 14))
        self.nivel_lista = ["Estagiário",
                            "Treinee", "Júnior", "Pleno", "Sênior"]
        self.combo_nivel = ctk.CTkComboBox(
            self.frame_dados_prof, values=self.nivel_lista, width=130, corner_radius=5, font=('Helvetica', 12), height=15, state="readonly")
        self.combo_nivel.set(self.nivel_lista[0])
        
        self.salario = ctk.CTkLabel(self.frame_dados_prof, text='Salário', font=('Helvetica', 14))
        self.ent_salario = ctk.CTkEntry(self.frame_dados_prof, width=130, corner_radius=5, height=15, validate="key", placeholder_text="ex: 1000.00")
        self.ent_salario.configure(validatecommand=(self.frame_dados_prof.register(self.validar_salario), '%P'))
        
        # Posicionando os elementos no frame Dados_Prof

        self.dados_profissionais.place(x=22 ,y=10)
        self.linha.place(x=10, y=50, width=242)

        self.id.place(x=40, y=50)
        self.ent_id.place(x=40, y=72)

        self.dt_contratacao.place(x=40, y=100)
        self.ent_dt_contratacao.place(x=40, y=122)

        self.cargo.place(x=40, y=150)
        self.ent_cargo.place(x=40, y=172)

        self.area.place(x=40, y=200)
        self.combo_area.place(x=40, y=222)

        self.nivel.place(x=40, y=250)
        self.combo_nivel.place(x=40, y=272)

        self.salario.place(x=40, y=300)
        self.ent_salario.place(x=40, y=322)

# ---------------------------------------------------------------------------------

# Criando o Frame dos Botões
        self.frame_botoes = ctk.CTkFrame(janela, width=160, height=315)
        self.frame_botoes.place(x=729, y=85)

        # Botoes
        self.btn_cadastrar = ctk.CTkButton(
            self.frame_botoes, text='Cadastrar', command=self.cadastrar, width=100, font=('Helvetica', 14), corner_radius=5)
        self.btn_apagar = ctk.CTkButton(
            self.frame_botoes, text='Apagar', command=self.limpar, width=100, font=('Helvetica', 14), corner_radius=5)
        self.btn_atualizar = ctk.CTkButton(
            self.frame_botoes, text='Atualizar', command=self.atualizar_dados, width=100, font=('Helvetica', 14), corner_radius=5)
        self.btn_excluir = ctk.CTkButton(
            self.frame_botoes, text='Excluir', command=self.excluir_dados, width=100, font=('Helvetica', 14), corner_radius=5)

        # Posicionando os botões

        self.btn_cadastrar.place(x=32, y=36)
        self.btn_apagar.place(x=32, y=106)
        self.btn_atualizar.place(x=32, y=176)
        self.btn_excluir.place(x=32, y=246)

# ---------------------------------------------------------------------------------

# Criando um frame para organizar a TreeView
        self.frame_treeview = ctk.CTkFrame(janela, width=880, height=260)
        self.frame_treeview.place(x=10, y=435)

        # Criando a TreeView
        self.treeview = ttk.Treeview(self.frame_treeview, columns=(
            "cod", "nome", "cpf", "rg", "emissor", "genero", "data_nascimento", "ddd", "telefone", "cep", "cidade", "estado", "bairro", "rua", "numero", "complemento", "salario", "data_contratacao", "cargo", "area", "nivel"), show="headings")

        # Configurando as colunas
        self.treeview.column("cod", width=75)
        self.treeview.column("nome",width=200)
        self.treeview.column("cpf", width=110)
        self.treeview.column("rg", width=110)
        self.treeview.column("emissor", width=100)
        self.treeview.column("genero", width=150)
        self.treeview.column("data_nascimento", width=160)
        self.treeview.column("ddd", width=50)
        self.treeview.column("telefone", width=130)
        self.treeview.column("cep", width=130)
        self.treeview.column("cidade", width=130)
        self.treeview.column("estado",width=70)
        self.treeview.column("bairro", width=130)
        self.treeview.column("rua", width=150)
        self.treeview.column("numero", width=70)
        self.treeview.column("complemento", width=150)
        self.treeview.column("salario", width=130)
        self.treeview.column("data_contratacao", width=160)
        self.treeview.column("cargo", width=200)
        self.treeview.column("area", width=150)
        self.treeview.column("nivel", width=150)

        self.treeview.heading("cod", text='Matrícula')
        self.treeview.heading("nome", text='Nome')
        self.treeview.heading("cpf", text='CPF')
        self.treeview.heading("rg", text='RG')
        self.treeview.heading("emissor", text='Emissor')
        self.treeview.heading("genero", text='Gênero')
        self.treeview.heading("data_nascimento", text='Data de Nascimento')
        self.treeview.heading("ddd", text='DDD')
        self.treeview.heading("telefone", text='Telefone')
        self.treeview.heading("cep", text='Cep')
        self.treeview.heading("cidade", text='Cidade')
        self.treeview.heading("estado", text='Estado')
        self.treeview.heading("bairro", text='Bairro')
        self.treeview.heading("rua", text='Rua')
        self.treeview.heading("numero", text='Número')
        self.treeview.heading("complemento", text='Complemento')
        self.treeview.heading("salario", text='Salário')
        self.treeview.heading("data_contratacao", text='Data de Contratação')
        self.treeview.heading("cargo", text='Cargo')
        self.treeview.heading("area", text='Área')
        self.treeview.heading("nivel", text='Nível')

        # Preenchendo o TreeView com registros do Banco de Dados
        self.treeview.bind("<<TreeviewSelect>>",
                           self.apresentarRegistrosSelecionados)

        # Carregar dados iniciais
        self.carregarDadosIniciais()

        # Editando o visual da treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                             background="#4F4F4F",
                             foreground="white",
                             rowheight=25,
                             fieldbackground="#4F4F4F",
                             font="helvetica 12")
        self.style.configure("Treeview.Heading", font="helvetica 12")
        self.style.map("Treeview",
                       background=[('selected', '#4169E1')])

        # Adicionando barra de rolagem
        self.scrollbar = ttk.Scrollbar(
            self.frame_treeview, orient="vertical", command=self.treeview.yview)
        self.treeview.config(yscrollcommand=self.scrollbar.set)

        self.scrollbarx = ttk.Scrollbar(
            self.frame_treeview, orient="horizontal", command=self.treeview.xview)
        self.treeview.config(xscrollcommand=self.scrollbarx.set)

        # Posicionando os elementos do Frame Treeview
        self.treeview.place(x=50, y=10, width=990)
        self.scrollbar.place(x=1043, y=10, height=280)
        self.scrollbarx.place(x=50, y=295, width=980)

# ---------------------------------------------------------------------------------

# Programa Backend

    # Validação de campos numéricos
    def validar_num(self, valor, max_digitos):
        #permite apenas números e até um máximo de dígitos
        if valor.isdigit() and len(valor) <= int(max_digitos):
            return True
        #permite esvaziar o campo
        elif valor == "":
            return True
        else:
            return False

# ---------------------------------------------------------------------------------    
    # Validação de campos strings
    def validar_str(self, valor, max_digitos):
        #verifica a quantidade máxima de caracteres 
        if len(valor) <= int(max_digitos):
            return True
        #permite esvaziar o campo
        elif valor == "":
            return True
        else:
            return False
            
# ---------------------------------------------------------------------------------        
    def validar_salario(self, valor):
        # Permite campo vazio
        if valor == "":
            return True

        # Expressão regular para validar o formato numérico
        pattern = r'^\d{0,8}(\.\d{0,2})?$'
        
        # Verifica se o valor corresponde ao padrão
        if re.match(pattern, valor):
            return True
        else:
            return False
    
# ---------------------------------------------------------------------------------    
    # Função para transformar uma data de dd/mm/yyyy (no widget do programa) para yyyy-mm-dd (no BD)  
    def validar_data(self, texto):
        if len(texto) == 10 and texto[2] == '/' and texto[5] == '/':      
            dia, mes, ano = texto.split('/')
            if dia.isdigit() and mes.isdigit() and ano.isdigit():    
                data_formatada = f"{ano}-{mes}-{dia}"
                return data_formatada
            else: messagebox.showerror(title="Data inválida.", message="Digite dd/mm/aaaa")
        else:messagebox.showerror(title="Data inválida.", message="Digite dd/mm/aaaa")

# ---------------------------------------------------------------------------------
    # Função para transformar uma data de yyyy-mm-dd (no BD) para dd/mm/yyyy (no widget do programa)
    def transformar_data(self, data_bd):
     
        partes = data_bd.split('-')
        if len(partes) == 3:
            return f"{partes[2]}/{partes[1]}/{partes[0]}"
        else:
            return 

# ---------------------------------------------------------------------------------        
    def comparar_datas(self, data_nascimento, data_contratacao):
        try:
            # Converte as strings de data para objetos datetime
            dt_nasc = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
            dt_cont = datetime.datetime.strptime(data_contratacao, "%d/%m/%Y")
            hoje = datetime.datetime.today()

            # Verifica se alguma das datas é futura
            if dt_nasc > hoje:
                messagebox.showerror("Erro de Validação", "A data de nascimento não pode ser futura.")
                return False

            if dt_cont > hoje:
                messagebox.showerror("Erro de Validação", "A data de contratação não pode ser futura.")
                return False
            
            # Compara as datas
            if dt_cont <= dt_nasc:
                    messagebox.showerror("Erro de Validação", "A data de contratação deve ser posterior à data de nascimento.")
                    return False
            return True
        
        except ValueError:
            messagebox.showerror("Erro de Formato", "Formato de data inválido. Use o formato dd/mm/aaaa.")
            return False
        
# ---------------------------------------------------------------------------------
    def trocar_modo(self):
        print('trocando modo')
        if self.modo.get() == 1:  # Verifica se o botão de alternância está ligado
            ctk.set_appearance_mode('light')

        else:
            ctk.set_appearance_mode('dark')

# ---------------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):
        self.limpar()
        for selection in self.treeview.selection():
            # Obtém as informações do item selecionado da treeview
            item = self.treeview.item(selection)
            # Extrai os campos do item
            cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel = item["values"][0:21]
            # Insere no campo de entrada correspondente
            self.ent_id.insert(0, cod)
            self.ent_nome.insert(0, nome)
            self.ent_cpf.insert(0, cpf)
            self.ent_rg.insert(0, rg)
            self.ent_orgaoEmissor.insert(0, emissor)
            self.combo_genero.set(genero)
            self.ent_dt_nasc.insert(0, self.transformar_data(data_nascimento))
            self.ent_ddd.insert(0, ddd)
            self.ent_tel.insert(0, telefone)
            self.ent_cep.insert(0 , cep)
            self.ent_cidade.insert(0, cidade)
            self.combo_estado.set(estado)
            self.ent_bairro.insert(0, bairro)
            self.ent_rua.insert(0, rua)
            self.ent_numero.insert(0, numero)
            self.ent_complemento.insert(0, complemento)
            self.ent_salario.insert(0, salario)
            self.ent_dt_contratacao.insert(0, self.transformar_data(data_contratacao))
            self.ent_cargo.insert(0, cargo)
            self.combo_area.set(area)
            self.combo_nivel.set(nivel)

# ---------------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
            # utilizado para acompanhar o número total de registros carregados.
            self.id = 0
            # iid é utilizado para identificar os itens inseridos na treeview.
            self.iid = 0
            registros = self.Objeto.Select()
            print("************ dados dsponíveis no BD ***********")
            for item in registros:
                cod = item[0]
                nome = item[1]
                cpf = item[2]
                rg = item[3]
                emissor = item[4]
                genero = item[5]
                data_nascimento = item[6]
                ddd = item[7] 
                telefone = item[8]
                cep = item[9]
                cidade = item[10]
                estado = item[11]
                bairro = item[12]
                rua = item[13]
                numero = item[14]
                complemento = item[15]
                salario = item[16]
                data_contratacao = item[17]
                cargo = item[18]
                area = item[19]
                nivel = item[20]

                print('Cod = ', cod)
                print("Nome = ", nome)
                print("CPF = ", cpf)
                print("RG = ", rg)
                print("Emissor = ", emissor)
                print("Gênero = ", genero)
                print("Data de Nascimento = ", data_nascimento)
                print('ddd = ', ddd)
                print("telefone = ", telefone)
                print("cep = ", cep)
                print("cidade = ", cidade)
                print("Estado = ", estado)
                print("Bairro = ", bairro)
                print("Rua = ", rua)
                print("Número = ", numero)
                print("Complemento = ", complemento)
                print("Salário = ", salario)
                print("Data de Contratação = ", data_contratacao)
                print("Cargo = ", cargo)
                print("Área = ", area)
                print("nivel  = ", nivel, "\n")

                self.treeview.insert('', 'end',
                                         iid=self.iid,
                                         values=(cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel))
                self.iid = self.iid + 1
                self.id = self.id + 1
            print('Dados da Base')
        except:
            print('Ainda não existem dados para carregar')

# ---------------------------------------------------------------------------------
    def pegar_dados(self):
        cod = int(self.ent_id.get())
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        rg = self.ent_rg.get()
        emissor = self.ent_orgaoEmissor.get()
        genero = self.combo_genero.get()
        data_nascimento = self.validar_data(self.ent_dt_nasc.get())
        ddd = self.ent_ddd.get()
        telefone = self.ent_tel.get()
        cep = self.ent_cep.get()
        cidade = self.ent_cidade.get()
        estado = self.combo_estado.get()
        bairro = self.ent_bairro.get()
        rua = self.ent_rua.get()
        numero = self.ent_numero.get()
        complemento = self.ent_complemento.get()
        salario = float(self.ent_salario.get())
        data_contratacao = self.validar_data(self.ent_dt_contratacao.get())
        cargo = self.ent_cargo.get()
        area = self.combo_area.get()
        nivel = self.combo_nivel.get()
        return (cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, 
                cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel)

# ---------------------------------------------------------------------------------
    def cadastrar(self):
        data_nascimento = self.ent_dt_nasc.get()
        data_contratacao = self.ent_dt_contratacao.get()
        if not self.comparar_datas(data_nascimento, data_contratacao):
            return  # Se as datas são inválidas, interrompe o cadastro
        try:
            #Pega os dados dos campos de entrada
            dados = self.pegar_dados()  # Chamada do método corrigida

            # Mapear os campos para suas posições na tupla 'dados'
            campos = [
                "cod", "nome", "cpf", "rg", "emissor", "genero", "data_nascimento", "ddd", "telefone",
                "cep", "cidade", "estado", "bairro", "rua", "numero", "complemento", "salario",
                "data_contratacao", "cargo", "area", "nivel"
            ]

            # Definir campos obrigatórios
            campos_obrigatorios = {"cod", "nome", "cpf", "rg", "emissor", "genero", "data_nascimento", "ddd", "telefone",
                "cep", "cidade", "estado", "bairro", "rua", "numero", "salario",
                "data_contratacao", "cargo", "area", "nivel"}

            # Verificar se os campos obrigatórios estão preenchidos
            for campo, valor in zip(campos, dados):
                if campo in campos_obrigatorios and valor == "":
                    messagebox.showerror("Erro", f"O campo '{campo}' deve ser preenchido.")
                    return

            # Descompacte os dados
            cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel = dados

            self.Objeto.inserir(cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, 
                                telefone, cep, cidade, estado, bairro, rua, numero, complemento, 
                                salario, data_contratacao, cargo, area, nivel)

            # cadastrando no treeview
            self.treeview.insert('', 'end',
                                iid=self.iid,
                                values=(cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel))
            self.iid = self.iid + 1
            self.id = self.id + 1

            messagebox.showinfo("","Dado cadastrado com sucesso")
            self.limpar()
            
        except Exception:
            messagebox.showerror("Campo(s) inválido(s)", "Não foi possível cadastrar")
# ---------------------------------------------------------------------------------
    def limpar(self):
        self.ent_id.delete(0, END)
        self.ent_nome.delete(0, END)
        self.ent_cpf.delete(0, END)
        self.ent_rg.delete(0, END)
        self.ent_orgaoEmissor.delete(0, END)
        self.combo_genero.set(self.genero_lista[0])
        self.ent_dt_nasc.delete(0, END)
        self.ent_ddd.delete(0, END)
        self.ent_tel.delete(0, END)
        self.ent_cep.delete(0, END)
        self.ent_cidade.delete(0, END)
        self.combo_estado.set(self.estado_lista[0])
        self.ent_bairro.delete(0, END)
        self.ent_rua.delete(0, END)
        self.ent_numero.delete(0, END)
        self.ent_complemento.delete(0, END)
        self.ent_salario.delete(0, END)
        self.ent_dt_contratacao.delete(0, END)
        self.ent_cargo.delete(0, END)
        self.combo_area.set(self.area_lista[0])
        self.combo_nivel.set(self.nivel_lista[0])

# ---------------------------------------------------------------------------------
    def excluir_dados(self):
        confirmar = messagebox.askyesno("Confirmação de exclusão", "Tem certeza que quer excluir este item?")
        try:
            if confirmar:
                cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel = self.pegar_dados()
                self.Objeto.Delete(cod)
                # excluindo do treeview
                # O '*' desempacota os itens do .get_children
                self.treeview.delete(*self.treeview.get_children())
                self.carregarDadosIniciais()
                self.limpar()
                messagebox.showinfo("","Dado excluído com sucesso")
                print('Produto Excluído com Sucesso!')
            else:
                # Ação cancelada pelo usuário
                print('Exclusão cancelada pelo usuário.')
        except Exception:
            print('Não foi possível excluir o registro')
            messagebox.showerror("Erro", "Não foi possível excluir o registro")

# ---------------------------------------------------------------------------------
    def atualizar_dados(self):
        data_nascimento = self.ent_dt_nasc.get()
        data_contratacao = self.ent_dt_contratacao.get()
        if not self.comparar_datas(data_nascimento, data_contratacao):
            return  # Se as datas são inválidas, interrompe o cadastro
        try:
            #Pega os dados dos campos de entrada
            dados = self.pegar_dados()  # Chamada do método corrigida

            # Mapear os campos para suas posições na tupla 'dados'
            campos = [
                "cod", "nome", "cpf", "rg", "emissor", "genero", "data_nascimento", "ddd", "telefone",
                "cep", "cidade", "estado", "bairro", "rua", "numero", "complemento", "salario",
                "data_contratacao", "cargo", "area", "nivel"
            ]

            # Definir campos obrigatórios
            campos_obrigatorios = {"cod", "nome", "cpf", "rg", "emissor", "genero", "data_nascimento", "ddd", "telefone",
                "cep", "cidade", "estado", "bairro", "rua", "numero", "salario",
                "data_contratacao", "cargo", "area", "nivel"
                }

            # Verificar se os campos obrigatórios estão preenchidos
            for campo, valor in zip(campos, dados):
                if campo in campos_obrigatorios and valor == "":
                    messagebox.showerror("Erro", f"O campo '{campo}' deve ser preenchido.")
                    return

            # Descompacte os dados
            cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel = dados

            self.Objeto.Atualizar(cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel)

            messagebox.showinfo("","Dado atualizado com sucesso")
            # atualizar treeview
            self.treeview.delete(*self.treeview.get_children())
            self.carregarDadosIniciais()
            self.limpar
            print('registro atualizado com sucesso!')

        except Exception:
            print('Não foi possível atualizar')
            messagebox.showerror("Campo(s) inválido(s)", "Não foi possível atualizar")
            

# ---------------------------------------------------------------------------------
# Janela Principal do Custom TKinter

root = ctk.CTk()
ctk.set_appearance_mode('dark')
principal = App(root)
root.title('Airees')
root.geometry('900x700+400+50')
root.resizable(False, False)
root.mainloop()
