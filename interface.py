# Interface do usuário.

import os

class Interface:

    # Método construtor da classe.
    def __init__(self):
        pass


    def logotipo(self):
        print("I_____________________________________I")
        print("|          CATÁLOGO DE FILMES         |")
        print("I_____________________________________I")
        print("")


    def limpatela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        

    # opcoes = []
    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        # Verificar se opcaoSelecionada é um número inteiro válido.
        # Se não for, peça para tentar novamente.
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas)

        try: 
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)


        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        return opcaoSelecionada
    

    def mostraMenuPrincipal(self):
        print("1 - Cadastrar filme.")
        print("2 - Lista de filmes.")
        print("3 - Sair.")
        print("")

    
    def mostraCadastroFilmes(self):
        self.logotipo()

        print("Insira os dados do filme:")
        print("(campos com * são obrigatórios)")
        print("")

        titulo = self.solicitaValor('Título*: ', 'texto', False)
        genero = self.solicitaValor('Gênero*: ', 'texto', False)
        duracao = self.solicitaValor('Duração: ', 'texto', True)
        diretor = self.solicitaValor('Diretor: ', 'texto', True)
        estudio = self.solicitaValor('Estúdio: ', 'texto', True)
        classificacao = self.solicitaValor('Classificação*: ', 'texto', False)
        ano = self.solicitaValor('Ano: ', 'numero', True)


    # Solicita que o usuário insira um valor e valida esse valor.
    # return valorDigitado
    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        # Verifica se está vazio.
        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitaValor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
            return valor
        
        # Verifica se está no formato correto.
        if tipo == 'numero':
            try:
                opcaoSelecionada = float(opcaoSelecionada)
            except ValueError:
                print("Valor inválido!")
                return self.solicitaValor(legenda, tipo, permiteNulo)
            
            return valor
        

        