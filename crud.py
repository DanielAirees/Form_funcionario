import psycopg2 as conector

class AppBD:
    def __init__(self):
        print('Método construtor')

    def abrir_conexao(self):
        try:
            self.conexao = conector.connect(database='postgres',
                                   user='postgres',
                                   host='127.0.0.1',
                                   password='sua_senha',
                                   port='5432')
        except (Exception, conector.Error) as erro:
            if self.conexao:
                print('erro ao conectar com banco de dados')

# --------------------------------------------------------------------------------- 
    def inserir(self, cod, nome, cpf, rg, emissor, genero, data_nascimento, ddd, telefone, cep, cidade, estado, bairro, rua, numero, complemento, salario, data_contratacao, cargo, area, nivel):
        try:
            self.abrir_conexao()
            cursor = self.conexao.cursor()
            # Inserir dados na tabela pessoa
            cursor.execute("""
                INSERT INTO pessoa (cod, nome, cpf, rg, emissor, genero, data_nascimento)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (cod, nome, cpf, rg, emissor, genero, data_nascimento))

            # Inserir dados na tabela endereco
            cursor.execute("""
                INSERT INTO endereco (cod, cep, estado, cidade, bairro, rua, numero, complemento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (cod, cep, estado, cidade, bairro, rua, numero, complemento))

            # Inserir dados na tabela telefone
            cursor.execute("""
                INSERT INTO telefone (cod, ddd, telefone)
                VALUES (%s, %s, %s)
            """, (cod, ddd, telefone))

            # Inserir dados na tabela profissional
            cursor.execute("""
                INSERT INTO profissional (cod, data_contratacao, cargo, area, nivel, salario)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (cod, data_contratacao, cargo, area, nivel, salario))

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
            query = """SELECT 
            p.cod, p.nome, p.cpf, p.rg, p.emissor, p.genero, p.data_nascimento,
            t.ddd, t.telefone, e.cep, e.cidade, e.estado, e.bairro, e.rua, e.numero, e.complemento,          
            pr.salario, pr.data_contratacao, pr.cargo, pr.area, pr.nivel
            FROM pessoa p
            LEFT JOIN endereco e ON p.cod = e.cod
            LEFT JOIN telefone t ON p.cod = t.cod
            LEFT JOIN profissional pr ON p.cod = pr.cod; """
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
            # Deleta os dados nas tabelas relacionadas
            cursor.execute("DELETE FROM endereco WHERE cod = %s", (cod,))
            cursor.execute("DELETE FROM telefone WHERE cod = %s", (cod,))
            cursor.execute("DELETE FROM profissional WHERE cod = %s", (cod,))
            cursor.execute("DELETE FROM pessoa WHERE cod = %s", (cod,))
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
            
            query = """SELECT 
            p.cod, p.nome, p.cpf, p.rg, p.emissor, p.genero, p.data_nascimento,
            t.ddd, t.telefone, e.cep, e.cidade, e.estado, e.bairro, e.rua, e.numero, e.complemento,          
            pr.salario, pr.data_contratacao, pr.cargo, pr.area, pr.nivel
            FROM pessoa p
            LEFT JOIN endereco e ON p.cod = e.cod
            LEFT JOIN telefone t ON p.cod = t.cod
            LEFT JOIN profissional pr ON p.cod = pr.cod; """
            cursor.execute(query)
            registro = cursor.fetchone()
            print(registro)
            
            cursor.execute("""
            UPDATE pessoa 
            SET nome = %s, cpf = %s, rg = %s, emissor = %s, genero = %s, data_nascimento = %s
            WHERE cod = %s;
            """, (nome, cpf, rg, emissor, genero, data_nascimento, cod))

            # Atualiza os dados na tabela endereco
            cursor.execute("""
                UPDATE endereco 
                SET cep = %s, estado = %s, cidade = %s, bairro = %s, rua = %s, numero = %s, complemento = %s
                WHERE cod = %s;
            """, (cep, estado, cidade, bairro, rua, numero, complemento, cod))

            # Atualiza os dados na tabela telefone
            cursor.execute("""
                UPDATE telefone 
                SET ddd = %s, telefone = %s
                WHERE cod = %s;
            """, (ddd, telefone, cod))

            # Atualiza os dados na tabela profissional
            cursor.execute("""
                UPDATE profissional 
                SET data_contratacao = %s, cargo = %s, area = %s, nivel = %s, salario = %s
                WHERE cod = %s;
            """, (data_contratacao, cargo, area, nivel, salario, cod))

            self.conexao.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado no BD! ")
            print("Registro Depois da Atualização ")
            query = """SELECT 
            p.cod, p.nome, p.cpf, p.rg, p.emissor, p.genero, p.data_nascimento,
            t.ddd, t.telefone, e.cep, e.cidade, e.estado, e.bairro, e.rua, e.numero, e.complemento,          
            pr.salario, pr.data_contratacao, pr.cargo, pr.area, pr.nivel
            FROM pessoa p
            LEFT JOIN endereco e ON p.cod = e.cod
            LEFT JOIN telefone t ON p.cod = t.cod
            LEFT JOIN profissional pr ON p.cod = pr.cod; """
            cursor.execute(query)
            record = cursor.fetchone()
            print(record)
        except (Exception, conector.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if (self.conexao):
                cursor.close()
                self.conexao.close()
                print("Conexão com banco de dados encerrada.")
