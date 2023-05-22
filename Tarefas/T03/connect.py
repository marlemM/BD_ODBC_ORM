import psycopg2

# Define a conexão com o banco de dados
conn_string = "dbname=equipeBD user=postgres password=postgres host=localhost port=5432"
conn = psycopg2.connect(conn_string)

# Define o código do projeto para listar as atividades
projeto_codigo = 1

# Executa a consulta SQL para obter as atividades do projeto
query = f"""
SELECT a.codigo, a.descricao, a.dataInicio, a.dataFim, a.situacao, a.dataConclusao
FROM atividade a
JOIN atividade_projeto ap ON a.codigo = ap.codAtividade
WHERE ap.codProjeto = {projeto_codigo}
"""
cursor = conn.cursor()
cursor.execute(query)

# Exibe os resultados da consulta
for row in cursor.fetchall():
    codigo, descricao, dataInicio, dataFim, situacao, dataConclusao = row
    print(f"Código: {codigo}, Descrição: {descricao}, Data de Início: {dataInicio}, Data de Fim: {dataFim}, Situação: {situacao}, Data de Conclusão: {dataConclusao}")

# Fecha a conexão com o banco de dados
conn.close()
