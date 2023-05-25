import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=('172.17.0.4'),
            database=('equipebd'),
            user=('postgres'),
            password=('admin')
        )

        # create a cursor
        cur = conn.cursor()

        # execute a statement to select the activities of a specific project (in this case, the project with code 1)
        cur.execute('SELECT a.descricao FROM atividade AS a JOIN atividade_projeto AS ap ON a.codigo = ap.codAtividade WHERE ap.codProjeto = 1')

        # retrieve query results
        records = cur.fetchall()
        print("Total number of rows:", cur.rowcount)
        for row in records:
            print(row[0])

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')