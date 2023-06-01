from faker import Faker
import random
import psycopg2

# Conectando ao banco de dados
conn = psycopg2.connect(database="equipebd", user="postgres", password="admin", host="localhost")
cur = conn.cursor()

# Instanciando o objeto Faker
fake = Faker()

# Função para gerar um número aleatório de funcionários
# Função para gerar um número aleatório de funcionários
def gerar_funcionarios(num_funcionarios):
    for _ in range(num_funcionarios):
        nome = fake.name()[:15]  # Limita o tamanho do nome para 15 caracteres
        # Resto do código
        sexo = random.choice(['M', 'F'])
        data_nasc = fake.date_of_birth(minimum_age=18, maximum_age=65)
        salario = random.uniform(1000, 10000)
        supervisor = random.choice(range(1, num_funcionarios+1))
        depto = random.choice(range(1, 3))
        query = "INSERT INTO funcionario (nome, sexo, dataNasc, salario, supervisor, depto) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nome, sexo, data_nasc, salario, supervisor, depto)
        cur.execute(query, values)

# Função para gerar um número aleatório de departamentos
def gerar_departamentos(num_departamentos):
    for _ in range(num_departamentos):
        sigla = fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter()
        descricao = fake.word()
        gerente = random.choice(range(1, num_departamentos+1))
        query = "INSERT INTO departamento (sigla, descricao, gerente) VALUES (%s, %s, %s)"
        values = (sigla, descricao, gerente)
        cur.execute(query, values)

# Função para gerar um número aleatório de equipes
def gerar_equipes(num_equipes):
    for _ in range(num_equipes):
        nome_equipe = fake.company_suffix()
        query = "INSERT INTO equipe (nomeEquipe) VALUES (%s)"
        values = (nome_equipe,)
        cur.execute(query, values)

# Função para gerar um número aleatório de membros
def gerar_membros(num_membros, num_funcionarios, num_equipes):
    for _ in range(num_membros):
        cod_equipe = random.choice(range(1, num_equipes+1))
        cod_funcionario = random.choice(range(1, num_funcionarios+1))
        query = "INSERT INTO membro (codEquipe, codFuncionario) VALUES (%s, %s)"
        values = (cod_equipe, cod_funcionario)
        cur.execute(query, values)

# Definindo o número de linhas para cada tabela
num_funcionarios = 10
num_departamentos = 2
num_equipes = 2
num_membros = 8

# Populando as tabelas
gerar_funcionarios(num_funcionarios)
gerar_departamentos(num_departamentos)
gerar_equipes(num_equipes)
gerar_membros(num_membros, num_funcionarios, num_equipes)

# Commit das alterações e fechamento da conexão
conn.commit()
conn.close()
