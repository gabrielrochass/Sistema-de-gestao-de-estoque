# Sistema de gestão de estoque

## Sobre o projeto
O sistema de gestão de estoques desenvolvido em Python utiliza programação orientada a objetos para fornecer uma solução eficiente para o controle de produtos e quantidades em um banco de dados SQLite. Este projeto visa oferecer funcionalidades básicas, como inserção e remoção de itens do estoque, enquanto mantém uma estrutura organizada e de fácil compreensão.

## Funcionalidades Principais
O sistema oferece as seguintes funcionalidades principais:
1. **Inserção de Produtos**: Permite adicionar novos produtos ao estoque, especificando o nome do produto e sua quantidade.
2. **Remoção de Produtos**: Permite remover produtos do estoque, garantindo que a quantidade correta seja subtraída.

## Bibliotecas Utilizadas
O projeto utiliza a biblioteca SQLite3 para interagir com o banco de dados, facilitando a criação e manipulação das tabelas.

## Estrutura do Banco de Dados
O banco de dados utiliza uma única tabela denominada "store", que armazena informações sobre os produtos em estoque. A tabela possui os seguintes campos:
- **id**: Identificador único para cada registro na tabela.
- **produto**: Nome do produto armazenado.
- **quantidade**: Quantidade disponível do produto em estoque.

## Funcionamento do Código
O código é estruturado em uma classe principal denominada "Gestao", que gerencia todas as operações relacionadas ao estoque. Ao ser inicializada, a classe estabelece uma conexão com o banco de dados SQLite e verifica se a tabela "store" já existe. Se não existir, a tabela é criada. As operações de inserção e remoção de produtos são realizadas através dos métodos "insert" e "remove", respectivamente.

## Principais comando SQL utilizados:
1. Remove:
 ```
 DELETE FROM table_name WHERE condition;
 ```
2. Insert:
 ```
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
 ```
3. Create table:
 ```
 CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
 ```
 4. Select:
  ```
 SELECT column1, column2 FROM table_name WHERE condition;
 ```
 5. Order by:
  ```
 SELECT * FROM table_name ORDER BY column_name ASC|DESC;
 ```


