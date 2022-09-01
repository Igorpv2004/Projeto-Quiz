import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao() # abrindo a conexao com o banco de dados
        self.db_connection = self.db_connection.conectar()
        self.con = self.db_connection.cursor()#navegacao no banco de dados

    def inserir(self, nome, pontuacao):
        try:
            sql = "insert into Cadastro(codigo, nome, pontuacao) " \
                  "values ('' , '{}' , '{}')".format(nome, pontuacao)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha(s) afestada(s).".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def excluir(self, cod):
        try:
            sql = "delete from Cadastro where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount)
        except Exception as erro:
            return erro
