from sistema import Sistema
def menu():
    print('==== Sistema de Clientes ====')
    print('1.Cadastrar cliente \n2.Listar cliente \n3.Buscar cliente \n4.Editar cliente \n5.Excluir cliente \n6.Salvar em arquivo \n7.Carregar arquivo \n0.Sair')
menu()
sistema = Sistema()

while True:
    menu()
    escolha = input('Escolha: ')

    if escolha == '1':
        sistema.cadastrar_cliente()

    elif escolha == '2':
        sistema.listar_clientes()
        
    elif escolha == '3':
        sistema.buscar_cliente()
