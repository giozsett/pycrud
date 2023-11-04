# Classe principal do programa.
# Roda o código e acessa as classes.

# Importando a classe do arquivo interface.py.
from interface import Interface
from bancodados import BD

# Faz a interface existir no main.
interface = Interface()

opcao = ""
while opcao != 0:
    interface.Logotipo()
    interface.mostraMenuPrincipal()
    opcao = interface.selecionaOpcao([0, 1, 2])
    interface.limpatela()

    banco = BD("catalogofilmes.db")

# Se não for uma dessas opções, retornará a mensagem de opção inválida.
interface.selecionaOpcao([0, 1, 2])