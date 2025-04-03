## Projeto DinheiroSábio - Documentação Oficial

**Introdução**

O projeto DinheiroSábio, tem como objetivo ajudar os usuários a gerenciar suas despesas de forma simples e eficiente. Com ele, é possível visualizar seus gastos por meio de gráficos interativos, incluindo:

✅ Gráfico de Pizza – Exibe a distribuição dos gastos por categoria.

✅ Gráfico de Barras – Compara despesas fixas e variáveis.

✅ Gráfico de Barras – Analisa os gastos totais em relação à renda mensal.

Além disso, o usuário pode exportar suas despesas e informações financeiras em formato CSV, permitindo a visualização dos dados em planilhas como o Excel.


## Funcionalidades

**Menu Usuários**
* **Cadastrar Usuários:** Permite ao administrador do sistema adicionar novos usuários ao 
banco de dados, proporcionando o gerenciamento de contas e informações pessoais de cada usuário.

* **Atualizar Usuários:** Oferece a possibilidade de editar dados de usuários existentes, como
nome, e-mail e outras informações relevantes.

* **Deletar Usuários:** Permite remover usuários do sistema, garantindo que o banco de dados
esteja atualizado com as informações mais recentes.

**Menu Categorias**
* **Cadastrar Categorias:** O usuário pode adicionar novas categorias de despesas, como alimentação,
transporte, lazer, entre outras. Isso ajuda a organizar melhor os gastos.

* **Listar Categorias:** Exibe todas as categorias cadastradas no sistema, permitindo que o usuário
visualize e organize suas despesas de forma mais eficiente.

* **Atualizar Categorias:** Permite editar o nome ou a descrição de categorias existentes, garantindo
flexibilidade caso o usuário queira reorganizar suas finanças.

* **Deletar Categorias:** Facilita a remoção de categorias que não são mais necessárias, mantendo o
sistema organizado e livre de dados desnecessários.

**Menu Despesas**
* **Cadastrar Despesas:** O usuário pode registrar novas despesas, associando-as às categorias previamente
criadas, especificando valores, datas e outras informações relevantes.

* **Listar Despesas:** Exibe todas as despesas registradas pelo usuário, permitindo que ele veja rapidamente
seus gastos em diferentes períodos e categorias.

* **Atualizar Despesas:** Permite ao usuário editar despesas já registradas, caso haja necessidade de corrigir
algum valor ou categoria.

* **Deletar Despesas:** Oferece a possibilidade de excluir despesas registradas, mantendo o controle financeiro atualizado e sem erros.

**Menu Exportar para CSV**
* **Exportar Despesas e Informações Financeiras:** Permite ao usuário exportar seus dados financeiros (despesas e categorias) em formato CSV, com a possibilidade de filtrar as informações por mês. Esse formato pode ser aberto em programas como o Excel, facilitando a visualização e o controle das finanças. A exportação por mês permite ao usuário analisar suas finanças de forma mais detalhada, por período.

**Menu Gerar Relatório de Gastos**
* **Gráfico de Pizza – Gastos por Categoria:** Este gráfico exibe a distribuição percentual dos gastos do usuário por categoria, filtrando os dados conforme o mês selecionado. Ele permite uma visualização rápida de como o dinheiro foi gasto em diferentes áreas durante o mês escolhido.

* **Gráfico de Barras – Gastos Fixos vs Variáveis:** Compara os gastos fixos (como aluguel, contas de serviços públicos) com os gastos variáveis (como alimentação, entretenimento), filtrados por mês. Esse gráfico ajuda o usuário a identificar onde pode economizar durante o mês analisado.

* **Gráfico de Barras – Gastos Totais vs Renda Mensal:** Este gráfico compara o total de gastos do usuário com sua renda mensal, filtrado pelo mês escolhido. Ele permite uma análise clara de se o usuário está gastando mais do que ganha naquele mês, facilitando a tomada de decisões financeiras mais conscientes.


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


## Dependências Adicionais

* **greenlet:** Suporte para microthreads, utilizado pelo SQLAlchemy.

* **kiwisolver:** Resolves equações matemáticas, utilizado pelo Matplotlib.

* **cffi:** Interface para chamar funções C a partir do Python, usada em bibliotecas criptográficas.

* **contourpy:** Para criar contornos em gráficos científicos, utilizado pelo Matplotlib.

* **cycler:** Gerencia ciclos de cores e estilos em gráficos, utilizado pelo Matplotlib.

* **fonttools:** Manipula fontes, utilizado para renderização de textos em gráficos.

* **pycparser:** Parser para código C, utilizado por bibliotecas como cffi.

* **pyparsing:** Biblioteca para análise e processamento de strings baseadas em gramáticas.

* **python-dateutil:** Facilita o trabalho com datas e fusos horários.

* **pytz:** Manipula fusos horários compatíveis com o datetime do Python.

* **mysql-connector-python:** Alternativa ao SQLAlchemy para conectar Python ao MySQL.

* **PyMySQL:** Outra alternativa para conectar Python ao MySQL.

* **pillow:** Biblioteca para processamento de imagens.


## Diferenciais do Projeto

* **Filtragem de Despesas por Mês:** Tanto na exportação para CSV quanto nos relatórios
gráficos, os usuários podem filtrar suas despesas por mês, permitindo uma análise financeira
mais detalhada e organizada.

* **Análise Visual Intuitiva:** Os gráficos gerados com Matplotlib permitem que os usuários
visualizem seus gastos de maneira clara e eficiente, ajudando na tomada de decisões financeiras.

* **Exportação de Dados em CSV:** Permite que os usuários exportem seus registros financeiros
e analisem as informações em softwares como Excel, possibilitando um controle financeiro mais
aprofundado.

* **Organização Modular:** O projeto está bem estruturado, separando funcionalidades em menus
específicos (Usuários, Categorias, Despesas, Exportação, Relatórios), o que melhora a manutenção
e escalabilidade do código.

* **Pontencial de Expansão:** A arquitetura do sistema permite futuras melhorias, como:
Novas funcionalidades nos menus, como dashboards e notificações financeiras. E Aprimoramento
da interface, tornando-a mais moderna e responsiva para acesso em diferentes dispositivos.


## Criação do Banco de Dados e Tabelas

```sql
CREATE DATABASE gestao_despesas;
USE gestao_despesas;

CREATE USER Vinicius@localhost IDENTIFIED BY '@program225X';
SELECT * FROM mysql.user;

GRANT ALL 
ON gestao_despesas.*
TO Vinicius@localhost;
SHOW GRANTS FOR Vinicius@localhost;

CREATE TABLE usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    renda_mensal DECIMAL(10,2) NOT NULL DEFAULT 0.00
);

CREATE TABLE categorias (
    categoria_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    UNIQUE (usuario_id, nome), -- Restrição de unicidade por usuário
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id) ON DELETE CASCADE
);

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

ALTER TABLE despesas ADD COLUMN fixa TINYINT NOT NULL DEFAULT 0;

CREATE TABLE historico_renda (
    historico_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    renda_mensal DECIMAL(10,2) NOT NULL,
    data_registro DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id) ON DELETE CASCADE
);

INSERT INTO usuarios (nome, email, cpf, renda_mensal) VALUES
('Vinícius', 'vinip8372@gmail.com', '12378596456085', 5000.00),
('Henrique', 'henrique21@gmail.com', '00987696798652', 3500.00),
('Eduardo', 'eduardo@gmail.com', '00098769865432', 4300.00),
('Paulo Junior', 'paulojunior@gmail.com', '00097654857431', 4000.00),
('Vitor Emanuel', 'vitoremanuel@gmail.com', '99877876500532', 3700.00);

INSERT INTO categorias (usuario_id, nome) VALUES
(1, 'Academia'),
(2, 'Combustível'),
(3, 'Plano de Celular'),
(4, 'Alimentação'),
(5, 'Internet');

INSERT INTO despesas (usuario_id, categoria_id, valor, data, descricao, fixa) VALUES
(1, 1, 120.00, '2025-02-07', 'Mensalidade da Academia', 1),
(2, 2, 150.00, '2025-02-07', 'Combustível do Mês', 0),
(3, 3, 60.00, '2025-02-07', 'Plano de Celular', 1),
(4, 4, 350.00, '2025-02-07', 'Alimentos para Dieta', 0),
(5, 5, 100.00, '2025-02-07', 'Internet', 1);

INSERT INTO historico_renda (usuario_id, renda_mensal, data_registro) VALUES
(1, 5000.00, '2025-02-01'),
(2, 5000.00, '2025-02-01'),
(3, 3500.00, '2025-02-01'),
(4, 4300.00, '2025-02-01'),
(6, 3700.00, '2025-02-01');
```
