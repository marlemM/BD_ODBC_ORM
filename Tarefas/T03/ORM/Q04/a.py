from faker import Faker
import random
import psycopg2

# Função para gerar dados falsos
def generate_fake_data(fake, num_rows):
    # Gere dados falsos para a tabela "funcionarios"
    funcionarios = []
    for _ in range(num_rows):
        descricao = fake.sentence(nb_words=6)
        if len(descricao) > 45:
            descricao = descricao[:45]  # Ajustar para 45 caracteres, se exceder
        funcionarios.append(descricao)

    # Gere dados falsos para a tabela "projeto"
    projetos = []
    for _ in range(num_rows):
        nome = fake.company()
        projetos.append(nome)

    # Retorne os dados gerados
    return funcionarios, projetos



# Função para popular as tabelas do banco de dados com dados falsos
def populate_database(num_rows):
    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        host='localhost',
        database='equipebd',
        user='postgres',
        password='admin'
    )

    # Criar um cursor
    cur = conn.cursor()

    try:
        fake = Faker()
        funcionarios, projetos = generate_fake_data(fake, num_rows)

        # Insira os dados na tabela "funcionarios"
        for descricao in funcionarios:
            cur.execute('INSERT INTO funcionarios (descricao) VALUES (%s)', (descricao,))
        print(f'{len(funcionarios)} linhas inseridas na tabela "funcionarios"')

        # Insira os dados na tabela "projeto"
        for nome in projetos:
            cur.execute('INSERT INTO projeto (nome) VALUES (%s)', (nome,))
        print(f'{len(projetos)} linhas inseridas na tabela "projeto"')

        # Efetive as alterações no banco de dados
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        # Fechar a comunicação com o PostgreSQL
        cur.close()
        conn.close()
        print('Conexão com o banco de dados fechada.')

# Número de linhas a serem geradas
num_rows = 10

# Popule as tabelas do banco de dados com dados falsos
populate_database(num_rows)
