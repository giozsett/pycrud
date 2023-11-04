# Classe principal do programa.
# Roda o código e acessa as classes.

# Importando a classe do arquivo interface.py.
from interface import Interface
from bancodados import BD

# Faz a interface existir no main.
interface = Interface()
banco = BD("catalogofilmes.db")

opcao = ""
while opcao != 0:
    interface.logotipo()
    interface.mostraMenuPrincipal()
    opcao = interface.selecionaOpcao([0, 1, 2])
    interface.limpatela()

    # Tela de cadastro de filmes.
    if opcao == 1:
        interface.mostraCadastroFilmes()

    #Tela de lista de filmes.
    if opcao == 2:
        pass

    if opcao == 3:
        pass


# Se não for uma dessas opções, retornará a mensagem de opção inválida.
interface.selecionaOpcao([0, 1, 2])