## Projeto DinheiroSábio - Documentação Oficial

**Introdução**

O projeto DinheiroSábio, tem como objetivo ajudar os usuários a gerenciar suas despesas de forma simples e eficiente. Com ele, é possível visualizar seus gastos por meio de gráficos interativos, incluindo:

✅ Gráfico de Pizza – Exibe a distribuição dos gastos por categoria.
✅ Gráfico de Barras – Compara despesas fixas e variáveis.
✅ Gráfico de Barras – Analisa os gastos totais em relação à renda mensal.

Além disso, o usuário pode exportar suas despesas e informações financeiras em formato CSV, permitindo a visualização dos dados em planilhas como o Excel.


## Funcionalidades



## Tecnologias Utilizadas

**Editor de Código**
* **Visual Studio Code:** Como editor de código.

**Banco de Dados**
* **MySQL:** Banco de dados relacional utilizado para armazenar os dados do projeto.

**Framework**
* **SQLAlchemy:** ORM (Object Relational Mapper) para facilitar a interação com o banco de dados.

**Linguagem de Programação**
* **Pyhton:** Linguagem de programação utilizada para o desenvolvimento do projeto.


## Bibliotecas

**Manipulação de Dados**
* **Pandas:** Para manipulação e análise de dados.
* **NumPy:** Biblioteca para cálculos numéricos e operações com arrays e matrizes.

**Visualização de Dados**
* **Matplotlib:** Biblioteca para criação de gráficos e visualizações de dados financeiros.

**Segurança e Criptografia**
* **bcrypt:** Biblioteca para hashing de senhas e segurança.
* **cryptography:** Biblioteca para criptografia de dados sensíveis.


## Dependências Adicionais

greenlet: Suporte para microthreads, utilizado pelo SQLAlchemy.

kiwisolver: Resolves equações matemáticas, utilizado pelo Matplotlib.

cffi: Interface para chamar funções C a partir do Python, usada em bibliotecas criptográficas.

contourpy: Para criar contornos em gráficos científicos, utilizado pelo Matplotlib.

cycler: Gerencia ciclos de cores e estilos em gráficos, utilizado pelo Matplotlib.

fonttools: Manipula fontes, utilizado para renderização de textos em gráficos.

pycparser: Parser para código C, utilizado por bibliotecas como cffi.

pyparsing: Biblioteca para análise e processamento de strings baseadas em gramáticas.

six: Fornece compatibilidade entre Python 2 e 3.

tzdata: Banco de dados de fusos horários.

python-dateutil: Facilita o trabalho com datas e fusos horários.

pytz: Manipula fusos horários compatíveis com o datetime do Python.

packaging: Lida com metadados de pacotes Python.

mysql-connector-python: Alternativa ao SQLAlchemy para conectar Python ao MySQL.

PyMySQL: Outra alternativa para conectar Python ao MySQL.

pillow: Biblioteca para processamento de imagens.

typing_extensions: Fornece tipos avançados para anotações no código.


## Diferenciais do Projeto



### Criação do Banco de Dados e Tabelas

-- Criação do Banco de Dados
CREATE DATABASE gestao_despesas;
USE gestao_despesas;

-- Criação do Usuário Vinicius
CREATE USER Vinicius@localhost IDENTIFIED BY '@program225X';
SELECT * FROM mysql.user;

-- Concessão de Permissões ao Usuário Vinicius
GRANT ALL
ON gestao_despesas.*
TO Vinicius@localhost;
SHOW GRANTS FOR Vinicius@localhost;

-- Criação da tabela dos Usuários
CREATE TABLE usuarios (
	usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    renda_mensal DECIMAL(10,2) NOT NULL DEFAULT 0.00
);

-- Criação da tabela das Categorias
CREATE TABLE categorias (
	categoria_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    UNIQUE (usuario_id, nome), -- Restrição de unicidade por usuário
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id) ON DELETE CASCADE
);

-- Criação da Tabela das Despesas
CREATE TABLE despesas (
	despesa_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    categoria_id INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data DATE NOT NULL,
    descricao TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id) ON DELETE CASCADE
);

-- Adiciona a coluna *fixa* na tabela despesas
ALTER TABLE despesas ADD COLUMN fixa TINYINT NOT NULL DEFAULT 0;

-- Criação da tabela de Históricos de Renda
CREATE TABLE historico_renda (
    historico_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    renda_mensal DECIMAL(10,2) NOT NULL,
    data_registro DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id) ON DELETE CASCADE
);

-- Inserir dados dos Usuários
INSERT INTO usuarios (nome, email, cpf, renda_mensal)
VALUES
	('Vinícius', 'vinip8372@gmail.com', '12378596456085', 5000.00),
    ('Henrique', 'henrique21@gmail.com', '00987696798652', 3500.00),
    ('Eduardo', 'eduardo@gmail.com', '00098769865432', 4300.00),
    ('Paulo Junior', 'paulojunior@gmail.com', '00097654857431', 4000.00),
	('Vitor Emanuel', 'vitoremanuel@gmail.com', '99877876500532', 3700.00);

-- Inserir dados das Categorias
INSERT INTO categorias (usuario_id, nome)
VALUES
	(1, 'Academia'),
    (2, 'Combustível'),
    (3, 'Plano de Celular'),
    (4, 'Alimentação'),
    (5, 'Internet');

-- Inserir dados das Despesas    
INSERT INTO despesas (usuario_id, categoria_id, valor, data, descricao, fixa)
VALUES
	(1, 1, 120.00, '2025-02-07', 'Mensalidade da Academia', 1),
    (2, 2, 150.00, '2025-02-07', 'Combustível do Mês', 0),
	(3, 3, 60.00, '2025-02-07', 'Plano de Celular', 1),
	(4, 4, 350.00, '2025-02-07', 'Alimentos para Dieta', 0),
	(5, 5, 100.00, '2025-02-07', 'Internet', 1);

-- Inserir dados dos Históricos de Renda
INSERT INTO historico_renda (usuario_id, renda_mensal, data_registro)
VALUES
	(1, 5000.00, '2025-02-1'),
    (2, 5000.00, '2025-02-1'),
    (3, 3500.00, '2025-02-1'),
    (4, 4300.00, '2025-02-1'),
    (6, 3700.00, '2025-02-1');