# Classe para lidar com o banco de dados.

import sqlite3

class BD:
    # Método construtor.
    def __init__(self, banco_dados):
        self.conectarBanco(banco_dados)


    # Conecta no arquivo do banco de dados e cria um cursor.    
    def conectarBanco(self, banco_dados):
        self.banco = sqlite3.connect('')
        self.cursor = self.banco.cursor()

        self.criarTabelaFilmes()

    # Aspas triplas """ permitem pular linhas.
    # TEXT NULL significa que o campo pode ficar em branco.
    def criarTabelaFilmes(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes(
                            id INTERGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            genero TEXT NOT NULL,
                            duracao TEXT NULL,
                            diretor TEXT NULL,
                            estudio TEXT NULL,
                            classificacao TEXT NOT NULL
                            ano TEXT NULL
            )
        """)