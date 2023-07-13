-- Consulta de todos os clientes:
SELECT * FROM clientes;

-- Consulta de todos os itens do cardápio:
SELECT * FROM cardapio;

-- Consulta de todos os itens do estoque:
SELECT * FROM estoque;

-- Consulta de todos os pedidos:
SELECT * FROM pedidos;

-- Consulta de todos os funcionários:
SELECT * FROM funcionarios;

-- Consulta de todas as transações financeiras:
SELECT * FROM transacoes;

-- Consulta de todos os fornecedores:
SELECT * FROM fornecedores;

-- Selecionar a quantidade de ingredientes disponíveis no estoque:
SELECT SUM(quantidade) FROM estoque;

-- Selecionar o sabor e o número de vendas de cada pizza do cardápio:
SELECT c.sabor, COUNT(p.id) as num_vendas
FROM cardapio c
LEFT JOIN pedidos p ON c.id = p.pizza_id
GROUP BY c.sabor;

-- Selecionar o nome e cargo de todos os funcionários contratados após uma determinada data:
SELECT nome, cargo
FROM funcionarios
WHERE data_contratacao > '2020-01-01';

-- Função que retorna a idade de um cliente a partir da data de nascimento:
CREATE FUNCTION idade_cliente(nascimento Date) RETURNS UInt8
    LANGUAGE SQL
    IMMUTABLE
    AS
    'SELECT toYear(now()) - toYear(nascimento) - (toDate(now()) < toDate(concat(toYear(now()), "-", toMonth(nascimento), "-", toDayOfMonth(nascimento))))';
-- Essa função recebe uma data de nascimento como entrada e retorna a idade do cliente em anos.

-- Procedimento que atualiza a quantidade de um ingrediente no estoque:
CREATE PROCEDURE atualiza_quantidade_ingrediente(ingrediente String, quantidade Int32)
    LANGUAGE SQL
    AS
    'UPDATE estoque SET quantidade = quantidade + :quantidade WHERE ingrediente = :ingrediente';
-- Esse procedimento recebe o nome de um ingrediente e a quantidade a ser adicionada ao estoque como entrada e atualiza a quantidade desse ingrediente no estoque.

-- Função que retorna o valor total de vendas por dia de uma determinada semana:
CREATE FUNCTION vendas_semana(data_inicio Date) RETURNS Array(Decimal(10,2))
    LANGUAGE SQL
    IMMUTABLE
    AS
    'SELECT ARRAY JOIN (SELECT toDate(data) as dia, SUM(valor) as valor_total FROM pedidos WHERE status = ''concluido'' AND toStartOfWeek(data_inicio) = toStartOfWeek(data) GROUP BY dia) ORDER BY dia';