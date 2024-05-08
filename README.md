# Form_funcionario
 Eu utilizei o Python integrado ao postgresql para construir esse formulário. O intuito era aprender crud e fazer a integração de Python com banco de dados. Para um visual mais moderno, utilizei a biblioteca Custom Tkinter.
Para fazer funcionar, você precisa criar uma tabela no PostgreSQL com o seguinte código e alterar a password na pasta crud:

create table colaborador(
cod integer not null primary key unique,
nome varchar(90) not null,
cpf varchar(11) not null unique,
rg varchar(9) not null unique,
emissor varchar(30) not null,
genero varchar(9),
data_nascimento date not null,
ddd varchar(2) not null,
telefone varchar(20) not null,
cep varchar(10) not null,
cidade varchar(60) not null,
estado varchar(2) not null,
bairro varchar(30) not null,
rua varchar(90) not null,
numero varchar(9) not null,
complemento varchar(100),
salario integer not null,
data_contratacao date not null,
cargo varchar(30) not null,
area varchar(30) not null,
nivel varchar(30) not null);
