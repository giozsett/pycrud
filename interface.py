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

        titulo = self.solicitaValor('Título*: ', ['texto'], False)
        genero = self.solicitaValor('Gênero*: ', ['texto'], False)
        duracao = self.solicitaValor('Duração: ', ['texto'], True)


    def solicitaValor(self, legenda, tipo = ['texto', 'numero'], permiteNulo = False):
        pass

        

        