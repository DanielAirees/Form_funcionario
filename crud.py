import psycopg2 as conector

class AppBD:
    def __init__(self):
        print('Método construtor')

    def abrir_conexao(self):
        try:
            self.conexao = conector.connect(database='postgres',
                                   user='postgres',
                                   host='127.0.0.1',
                                   password='senhadoBD',
                                   port='5432')
        except (Exception, conector.Error) as erro:
            if self.conexao:
                print('erro ao conectar com banco de dados')

# --------------------------------------------------------------------------------- 
    def inserir(self, cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel):
        try:
            self.abrir_conexao()
            cursor = self.conexao.cursor()
            query = """insert into public."colaborador" ("cod", "nome", "cpf", "rg", "emissor", "genero", "data_nascimento",
                            "ddd", "telefone", "cep", "cidade", "estado", "bairro", "rua", "numero", "complemento", "salario", 
                            "data_contratacao", "cargo", "area", "nivel") 
                            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            inserir = (cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel)
            cursor.execute(query, inserir)
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'dado cadastrado')

        except (Exception, conector.Error) as erro:
            if self.conexao:
                print('Erro ao cadastrar')
        finally:
            if cursor:
                cursor.close()
            if self.conexao:
                self.conexao.close()
            print('Conexão com banco de dados encerrada')

# --------------------------------------------------------------------------------- 
    def Select (self):
        try:
            self.abrir_conexao()
            cursor = self.conexao.cursor()
            query = """select * from public."colaborador" """
            cursor.execute(query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, conector.Error) as erro:
            print('Erro ao selecionar id')

        finally:
            if cursor:
                cursor.close()
            if self.conexao:
                self.conexao.close()
            print('Conexão com banco de dados encerrada')

        return registros
    
# --------------------------------------------------------------------------------- 
    def Delete (self, cod):
        try:
            self.abrir_conexao()
            cursor = self.conexao.cursor()
            query = """delete from public."colaborador" where "cod" = (%s)"""
            cursor.execute(query, (cod,))
            self.conexao.commit()
            count = cursor.rowcount
            print(count, 'registro excluído com sucesso')

        except (Exception, conector.Error) as erro:
            print('Erro ao excluir dados')

        finally:
            if cursor:
                cursor.close()
            if self.conexao:
                self.conexao.close()
            print('Conexão com banco de dados encerrada."')

# --------------------------------------------------------------------------------- 
    def Atualizar(self, cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, 
                  estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel):
        try:
            self.abrir_conexao()
            cursor = self.conexao.cursor()
            
            sql_select_query = """select * from public."colaborador" 
                                        where "cod" = %s"""
            
            cursor.execute(sql_select_query, (cod,))
            registro = cursor.fetchone()
            print(registro)
            
            sql_update_query = """Update public."colaborador" set "nome" = %s, 
            "cpf" = %s, rg= %s, emissor= %s, genero= %s, data_nascimento= %s, ddd = %s, telefone= %s, cep= %s, cidade= %s, 
                  estado= %s, bairro= %s, rua= %s, numero= %s, complemento= %s, salario= %s, data_contratacao= %s, 
            cargo= %s, area= %s, nivel= %s where "cod" = %s"""
            cursor.execute(sql_update_query, (nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, 
                  estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel, cod))
            self.conexao.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado no BD! ")
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from public."colaborador" 
                                    where "cod" = %s"""
            cursor.execute(sql_select_query, (cod,))
            record = cursor.fetchone()
            print(record)
        except (Exception, conector.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if (self.conexao):
                cursor.close()
                self.conexao.close()
                print("Conexão com banco de dados encerrada.")