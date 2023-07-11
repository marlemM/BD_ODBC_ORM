-- inserir dados da tabela de clientes

INSERT INTO clientes (id, nome, endereco, telefone)
VALUES (1, 'Taciano Silva', 'Rua A, 123', '1111111111');

INSERT INTO clientes (id, nome, endereco, telefone)
VALUES (2, 'Alef Santos', 'Rua B, 456', '2222222222');

INSERT INTO clientes (id, nome, endereco, telefone)
VALUES (3, 'Cíntia Campos', 'Rua C, 789', '3333333333');

INSERT INTO clientes (id, nome, endereco, telefone)
VALUES (4, 'Daniel Leônidas', 'Rua D, 135', '4444444444');

INSERT INTO clientes (id, nome, endereco, telefone)
VALUES (5, 'Marlem Magno', 'Rua E, 246', '5555555555');

-- inserir dados da tabela de cardápio

INSERT INTO cardapio (id, sabor)
VALUES (1, 'Calabresa');

INSERT INTO cardapio (id, sabor)
VALUES (2, 'Margherita');

INSERT INTO cardapio (id, sabor)
VALUES (3, 'Frango');

INSERT INTO cardapio (id, sabor)
VALUES (4, 'Bacon');

INSERT INTO cardapio (id, sabor)
VALUES (5, 'Carne de sol');

-- inserir dados da tabela de estoque

INSERT INTO estoque (id, ingrediente, quantidade)
VALUES (1, 'Molho de tomate, Calabresa', 10);

INSERT INTO estoque (id, ingrediente, quantidade)
VALUES (2, 'Molho branco, Queijo mussarela', 10);

INSERT INTO estoque (id, ingrediente, quantidade)
VALUES (3, 'Molho branco Frango', 10);

INSERT INTO estoque (id, ingrediente, quantidade)
VALUES (4, 'Molho branco, Bacon', 10);

INSERT INTO estoque (id, ingrediente, quantidade)
VALUES (5, 'Molho de tomate, Carne de sol', 10);

-- Inserção de dados na tabela de pedidos
INSERT INTO pedidos (id, cliente_id, pizza_id, data, valor, status, endereco_entrega)
VALUES (1, 1, 1, '2023-07-10 12:00:00', 15.99, 'Entregue', 'Rua X, 123');

INSERT INTO pedidos (id, cliente_id, pizza_id, data, valor, status, endereco_entrega)
VALUES (2, 2, 2, '2023-07-10 18:30:00', 12.99, 'Pendente', 'Rua Y, 456');

INSERT INTO pedidos (id, cliente_id, pizza_id, data, valor, status, endereco_entrega)
VALUES (3, 1, 2, '2023-07-11 14:00:00', 10.99, 'Em andamento', 'Rua Z, 789');

INSERT INTO pedidos (id, cliente_id, pizza_id, data, valor, status, endereco_entrega)
VALUES (4, 3, 1, '2023-07-11 19:30:00', 18.99, 'Pendente', 'Rua W, 987');

INSERT INTO pedidos (id, cliente_id, pizza_id, data, valor, status, endereco_entrega)
VALUES (5, 2, 3, '2023-07-12 11:45:00', 13.99, 'Entregue', 'Rua V, 654');

-- Inserção de dados na tabela de funcionários
INSERT INTO funcionarios (id, nome, cargo, data_contratacao, salario)
VALUES (1, 'João Silva', 'Atendente', '2020-01-15', 2500.00);

INSERT INTO funcionarios (id, nome, cargo, data_contratacao, salario)
VALUES (2, 'Maria Santos', 'Entregador', '2019-05-02', 2000.00);

INSERT INTO funcionarios (id, nome, cargo, data_contratacao, salario)
VALUES (3, 'Pedro Oliveira', 'Pizzaiolo', '2021-03-10', 3000.00);

INSERT INTO funcionarios (id, nome, cargo, data_contratacao, salario)
VALUES (4, 'Ana Souza', 'Caixa', '2022-07-20', 1800.00);

INSERT INTO funcionarios (id, nome, cargo, data_contratacao, salario)
VALUES (5, 'Rafael Mendes', 'Gerente', '2018-11-05', 4000.00);

-- Inserção de dados na tabela de transações financeiras
INSERT INTO transacoes (id, tipo, valor, data)
VALUES (1, 'Venda', 50.00, '2023-07-10 13:30:00');

INSERT INTO transacoes (id, tipo, valor, data)
VALUES (2, 'Venda', 35.00, '2023-07-11 17:15:00');

INSERT INTO transacoes (id, tipo, valor, data)
VALUES (3, 'Despesa', -20.00, '2023-07-12 09:00:00');

INSERT INTO transacoes (id, tipo, valor, data)
VALUES (4, 'Venda', 42.50, '2023-07-13 14:45:00');

INSERT INTO transacoes (id, tipo, valor, data)
VALUES (5, 'Despesa', -10.00, '2023-07-14 12:30:00');

-- Inserção de dados na tabela de fornecedores
INSERT INTO fornecedores (id, nome, contato, produto_fornecido, preco)
VALUES (1, 'Fornecedor A', 'contato@fornecedora.com', 'Queijo mussarela', 50.00);

INSERT INTO fornecedores (id, nome, contato, produto_fornecido, preco)
VALUES (2, 'Fornecedor B', 'contato@fornecedorb.com', 'Carne de sol', 20.00);

INSERT INTO fornecedores (id, nome, contato, produto_fornecido, preco)
VALUES (3, 'Fornecedor C', 'contato@fornecedorc.com', 'Bacon', 30.00);

INSERT INTO fornecedores (id, nome, contato, produto_fornecido, preco)
VALUES (4, 'Fornecedor D', 'contato@fornecedord.com', 'Frango', 10.00);

INSERT INTO fornecedores (id, nome, contato, produto_fornecido, preco)
VALUES (5, 'Fornecedor E', 'contato@fornecedore.com', 'Massa de pizza', 15.00);
