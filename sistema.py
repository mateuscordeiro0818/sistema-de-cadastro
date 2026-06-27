from cliente import Cliente
import json

class Sistema:

    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self):
        nom = input('Nome do cliente: ')
        idade = input('Idade do cliente: ')
        email = input('Email do cliente: ')
        telefone = input('Telefone do cliente: ')

        cliente = Cliente(nom, idade, email, telefone)

        self.clientes.append(cliente)
        

    def listar_clientes(self):
      
        print(f"Total de clientes: {len(self.clientes)}")

        for cliente in self.clientes:
            print(f"""
    Nome: {cliente.nome}
    Idade: {cliente.idade}
    Email: {cliente.email}
    Telefone: {cliente.telefone}
    """)

        

    def buscar_cliente(self):
        found = input('Nome do cliente: ')
        for cliente in self.clientes:
            if found == cliente.nome:
                print('Ele é nosso cliente')
                break
            else:
                print('ele nao é nosso cliente')
                break
       

    def editar_cliente():
        pass

    def excluir_cliente():
        pass

    def salvar(self):
        with open('clientes.json', 'w') as arquivo:
            lista_dict = []
            for Cliente in self.clientes:
                lista_dict.append({
                    "nome": Cliente.nome,
                    "idade": Cliente.idade,
                    "email": Cliente.email,
                    "telefone": Cliente.telefone
                })
            json.dump(lista_dict, arquivo)
        

    def carregar(self):
        with open('clientes.json', 'r') as arquivo:
            
            dados = json.load(arquivo)
            for cliente in dados:
                novo_cliente = Cliente(
                    cliente["nome"], cliente["idade"], cliente["email"], cliente["telefone"]
                )
                self.clientes.append(novo_cliente)