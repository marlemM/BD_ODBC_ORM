import psycopg2

def connect():
    conn = None
    try:
        # Conectar ao banco de dados PostgreSQL
        conn = psycopg2.connect(
            host='localhost',
            database='equipebd',
            user='postgres',
            password='admin'
        )

        # Criar um cursor
        cur = conn.cursor()

        # Exibir a versão do servidor PostgreSQL
        print('Versão do PostgreSQL:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)

        # Consulta para listar as atividades de um projeto
        projeto_id = 1  # ID do projeto desejado
        cur.execute('SELECT a.descricao FROM atividade AS a JOIN atividade_projeto AS ap ON a.codigo = ap.codAtividade WHERE ap.codProjeto = %s', (projeto_id,))

        # Obter os resultados da consulta
        records = cur.fetchall()
        print("Número total de linhas:", cur.rowcount)
        for row in records:
            print(row[0])

        # Fechar a comunicação com o PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Conexão com o banco de dados fechada.')


if __name__ == '__main__':
    connect()
