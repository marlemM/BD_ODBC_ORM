A) Explique um pouco como funciona o ORM escolhido.

# SQLAlchemy - ORM para Python

O SQLAlchemy é um ORM (Object-Relational Mapping) para Python, que permite interagir com bancos de dados relacionais usando objetos Python. Ele mapeia tabelas do banco de dados em classes Python e possibilita realizar operações de banco de dados através desses objetos, sem precisar escrever SQL manualmente.

Conceitos-chave

## Tabelas e Classes:

Você define classes Python que representam as tabelas do banco de dados.
Cada classe é uma subclasse da classe declarative_base() do SQLAlchemy.
As colunas do banco de dados são definidas como atributos da classe.
Relacionamentos entre tabelas podem ser definidos usando atributos especiais, como relationship().

## Sessões:
Uma sessão é uma interface para interagir com o banco de dados.
Você cria uma sessão a partir de uma instância do sessionmaker, especificando uma engine de banco de dados.
A sessão permite que você inicie transações, execute consultas, adicione, atualize e exclua objetos.

## Consultas:
O SQLAlchemy oferece uma linguagem de consulta poderosa e expressiva chamada SQLAlchemy ORM Query.
Você pode executar consultas usando a sintaxe do SQLAlchemy para filtrar, ordenar e agrupar dados.
As consultas são executadas através de métodos da sessão, como query(), filter(), order_by(), group_by(), etc.

## Relacionamentos:
O SQLAlchemy permite definir relacionamentos entre tabelas usando atributos especiais nas classes.
Os relacionamentos podem ser do tipo um-para-um, um-para-muitos e muitos-para-muitos.
Você pode acessar objetos relacionados usando atributos de objeto, que são automaticamente carregados do banco de dados quando necessário.

## Migrações:
O SQLAlchemy suporta migrações de esquema de banco de dados, permitindo que você faça alterações na estrutura do banco de dados de forma controlada.
As migrações ajudam a manter o esquema do banco de dados atualizado à medida que seu aplicativo evolui.

##  Engines:
Uma engine é a interface para se conectar a um banco de dados.
Você cria uma engine fornecendo a URL de conexão do banco de dados.
O SQLAlchemy suporta vários bancos de dados populares, como SQLite, PostgreSQL, MySQL, Oracle, entre outros.
Esses são apenas alguns dos conceitos principais do SQLAlchemy. Ele oferece uma ampla gama de recursos e opções de configuração para atender às necessidades de diferentes projetos. A documentação oficial do SQLAlchemy é uma excelente fonte de referência e exemplos detalhados para explorar mais a fundo seu funcionamento.