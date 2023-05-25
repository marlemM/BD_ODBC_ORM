import psycopg2
"""
Foi necessário dar permissões ao usuário para acessar os dados.
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO empresa_user;
"""
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host='localhost',
            database='equipebd',
            user='postgres',
            password='admin'
        )

        # create a cursor
        cur = conn.cursor()

	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # Execute a query
        cur.execute("SELECT * FROM funcionario")

        # Retrieve query results
        records = cur.fetchall()
        print("Total number of rows:", cur.rowcount)
        for row in records:
            print(row)

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()