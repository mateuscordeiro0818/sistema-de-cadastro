from sistema import Sistema
import time
def menu():
    time.sleep(1)
    print('==== Sistema de Clientes ====')
    print('1.Cadastrar cliente \n2.Listar cliente \n3.Buscar cliente \n4.Editar cliente \n5.Excluir cliente \n6.Salvar em arquivo \n7.Carregar arquivo \n0.Sair')

sistema = Sistema()

while True:
    menu()
    escolha = input('Escolha: ')

    match escolha:
        case '1':
            sistema.cadastrar_cliente()

        case '2':
            sistema.listar_clientes()

        case '3':
            sistema.buscar_cliente()

        case '4':
            sistema.editar_cliente()

        case '5':
            sistema.excluir_cliente()

        case '6':
            sistema.salvar()

        case '7':
            sistema.carregar()
        
        case '0':
            print('Encerrado')
            break
        
        case _:
            print('Opção invalida.')