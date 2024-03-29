# sistema de gestao de estoques - POO

# importando bibliotecas
import sqlite3 as sql # banco de dados

class Gestao:
    def __init__(self):
        self.conexao = sql.connect('estoque.db')
        self.createTable()
    
    def createTable(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS store (
                       id INTEGER PRIMARY KEY, 
                       produto TEXT, 
                       quantidade INTEGER, 
                    )''') # criando tabela no banco de dados
        self.conexao.commit() # salva as alteracoes

    def insert(self, produto, quantidade): #respeitar a ordem
        cursor = self.conexao.cursor() 
        cursor.execute(
            'INSERT INTO store (produto, quantidade) VALUES (?, ?)', (produto, quantidade)) # inserindo dados na tabela
        # dentro das aspas -> nome da tabela, nome das colunas. Fora das aspas -> variaveis
        self.conexao.commit() # salva as alteracoes

    def remove(self, produto, quantidade): # remove um produto do estoque 
        cursor = self.conexao.cursor()
        cursor.execute(
            'SELECT quantidade FROM store WHERE produto=?', (produto,))
        result = cursor.fetchall() # retorna uma lista com os valores encontrados na tabela store
        