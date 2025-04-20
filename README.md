# Projeto DinheiroSábio - Documentação Oficial

## Introdução

O projeto **DinheiroSábio**, tem como objetivo ajudar os usuários a gerenciar suas despesas de forma simples e eficiente. Com ele, é possível visualizar seus gastos por meio de gráficos interativos, incluindo:

✅ Gráfico de Pizza – Exibe a distribuição dos gastos por categoria.

✅ Gráfico de Barras – Compara despesas fixas e variáveis.

✅ Gráfico de Barras – Compara os gastos totais com a renda mensal, indicando se o usuário está no positivo ou negativo.

Além disso, o usuário pode exportar suas despesas e informações financeiras em formato XLSX, permitindo a visualização dos dados em planilhas como o Excel.


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

**Menu Exportar para XLSX**
* **Exportar Despesas e Informações Financeiras:** Permite ao usuário exportar seus dados financeiros em formato XLSX, com a possibilidade de filtrar as informações por mês. Esse formato pode ser aberto em programas como o Excel, facilitando a visualização e o controle das finanças. 

**Menu Gerar Relatório de Gastos**
* **Gráfico de Pizza – Gastos por Categoria:** Exibe a distribuição percentual dos gastos do usuário por categoria, filtrando os dados conforme o mês selecionado.

* **Gráfico de Barras – Gastos Fixos vs Variáveis:** Compara os gastos fixos com os gastos variáveis, permitindo uma melhor análise financeira mensal.

* **Gráfico de Barras – Gastos Totais vs Renda Mensal:** Compara o total de gastos do usuário com sua renda mensal no período selecionado. Esse gráfico ajuda a identificar se o usuário ficou no positivo ou no negativo no mês, auxiliando no planejamento financeiro e na tomada de decisões para equilibrar os gastos.


## Tecnologias Utilizadas

**Editor de Código:** Visual Studio Code

**Banco de Dados:** MySQL 

**Framework:** SQLAlchemy (para facilitar a interação com o banco de dados.)

**Linguagem de Programação:** Python


## Bibliotecas Principais

**Manipulação de Dados**
* **Pandas:** Para manipulação e análise de dados.

* **NumPy:** Biblioteca base para cálculos numéricos, utilizada internamente pelo Pandas.

**Visualização de Dados**
* **Matplotlib:** Biblioteca para criação de gráficos e visualizações de dados financeiros.


## Diferenciais do Projeto

* **Filtragem de Despesas por Mês:** Permite uma análise financeira mais detalhada.

* **Análise Visual Intuitiva:** Os gráficos ajudam na tomada de decisões financeiras.

* **Exportação de Dados em XLSX:** Facilita o controle financeiro.

* **Organização Modular:** Estrutura bem definida para fácil manutenção.

* **Potencial de Expansão:** A arquitetura do sistema permite futuras melhorias, como:
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


## 🛠️ Observações Necessárias para Rodar o App

Para garantir que o projeto rode corretamente em outro computador, é recomendado utilizar um ambiente virtual Python (`venv`) com as dependências do projeto listadas no arquivo `requirements.txt`.

### 1. Criar um ambiente virtual

No terminal, navegue até a pasta do projeto e execute:

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

- **Windows**:

```bash
.venv\Scripts\activate
```

- **Linux / MacOS**:

```bash
source .venv/bin/activate
```

Você saberá que o ambiente virtual foi ativado quando o nome do ambiente aparecer no início da linha do terminal.

### 3. Instalar as dependências

Com o ambiente ativado, instale todas as dependências necessárias com:

```bash
pip install -r requirements.txt
```

### 4. Rodar o projeto normalmente

Agora, você pode executar seu aplicativo Python com todas as bibliotecas certas, sem interferência de outras instalações do sistema. Para isso, utilize o comando abaixo no terminal (estando dentro do ambiente virtual e no diretório correto):

```bash
python app.py
```

🔁 Substitua app.py pelo nome do arquivo principal do seu projeto, se for diferente.

### 5. Sair do ambiente virtual (opcional)

Quando terminar de usar o projeto, você pode sair do ambiente virtual com:

```bash
deactivate
```

Isso retorna o terminal ao modo normal. Essa etapa é opcional, mas recomendada especialmente se você for trabalhar com outros projetos Python que usam ambientes diferentes.
