# Form_funcionario
 Eu utilizei o Python integrado ao postgresql para construir esse formulário. O intuito era aprender crud e fazer a integração de Python com banco de dados. Para um visual mais moderno, utilizei a biblioteca Custom Tkinter.
Para fazer funcionar, você precisa criar uma tabela no PostgreSQL com o seguinte código e alterar a password na pasta crud:

CREATE TABLE pessoa (
    cod integer PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
	cpf varchar(14) not null unique,
	rg varchar(14) not null,
	emissor varchar(10) not null,
	genero varchar(10) not null,
	data_nascimento date not null 
);

CREATE TABLE endereco (
    endereco_id SERIAL PRIMARY KEY,
    cod integer REFERENCES pessoa(cod),
	cep varchar(10) not null,
	estado varchar(10) not null,
    cidade VARCHAR(50) NOT NULL,
	bairro varchar(50) not null,
	rua varchar(100) not null,
	numero varchar(10) not null,
	complemento varchar(100) null    
);

CREATE TABLE telefone (
    telefone_id SERIAL PRIMARY KEY,
    cod integer REFERENCES pessoa(cod),
	ddd varchar(5) not null,
    telefone VARCHAR(15) NOT NULL    
);

CREATE TABLE profissional (
    cargo_id SERIAL PRIMARY KEY,
	cod integer references pessoa(cod),
	data_contratacao date not null,
    cargo VARCHAR(50) NOT NULL,
	area varchar(30) not null,
	nivel varchar(30) not null,
	salario numeric (10,2) not null
);

--Para inserir uma nova pessoa:
INSERT INTO pessoa (cod, nome, cpf, rg, emissor, genero, data_nascimento)
VALUES (1, 'Margot Diaz', '12345678900', '1234567', 'SSP', 'Feminino', '1990-01-01');

-- Inserir dados na tabela endereco
INSERT INTO endereco (cod, cep, estado, cidade, bairro, rua, numero, complemento)
VALUES (1, '12345678', 'SP', 'São Paulo', 'Centro', 'Av. Paulista', '100', 'Apto 101');

-- Inserir dados na tabela telefone
INSERT INTO telefone (cod, ddd, telefone)
VALUES (1, '11', '999999999');

-- Inserir dados na tabela profissional
INSERT INTO profissional (cod, data_contratacao, cargo, area, nivel, salario)
VALUES (1, '2020-01-01', 'Analista de Dados', 'Operacional', 'Pleno', 5000.00);
