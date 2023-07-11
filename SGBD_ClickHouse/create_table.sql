-- Criação da tabela de clientes
CREATE TABLE clientes (
  id Int32,
  nome String,
  endereco String,
  telefone String,
  PRIMARY KEY (id)
) ENGINE = MergeTree()
  ORDER BY id;
  
-- Criação da tabela de cardápio
CREATE TABLE cardapio (
  id Int32,
  sabor String,
  PRIMARY KEY (id)
) ENGINE = MergeTree()
  ORDER BY id;

-- Criação da tabela de estoque
CREATE TABLE estoque (
  id Int32,
  ingrediente String,
  quantidade Int32,
  PRIMARY KEY (id)
) ENGINE = MergeTree()
  ORDER BY id;
  
CREATE TABLE pedidos (
  id Int32,
  cliente_id Int32,
  pizza_id Int32,
  data DateTime,
  valor Decimal(10, 2),
  status String,
  endereco_entrega String,
  PRIMARY KEY (id)
) ENGINE = MergeTree()
  ORDER BY id;

-- Criação da tabela de funcionários
CREATE TABLE funcionarios (
  id Int32,
  nome String,
  cargo String,
  data_contratacao Date,
  salario Decimal(10, 2),
  PRIMARY KEY (id)
) ENGINE = MergeTree()
  ORDER BY id;

-- Criação da tabela de transações financeiras
CREATE TABLE transacoes (
  id Int32,
  tipo String,
  valor Decimal(10, 2),
  data DateTime,
  PRIMARY KEY (id)
) ENGINE = MergeTree()
  ORDER BY id;
  
-- Criação da tabela de fornecedores
CREATE TABLE fornecedores (
  id Int32,
  nome String,
  contato String,
  produto_fornecido String,
  preco Decimal(10, 2),
  PRIMARY KEY (id)
) ENGINE = MergeTree()
  ORDER BY id;


