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