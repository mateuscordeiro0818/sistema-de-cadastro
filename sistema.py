from cliente import Cliente
import json

class Sistema:

    def __init__(self):
        self.clientes = []
        self.carregar()


    def cadastrar_cliente(self):
        maior_id = 0
        for cliente in self.clientes:
            if cliente.id > maior_id:
                maior_id = cliente.id

        novo_id = maior_id + 1

        id = novo_id
        nom = input('Nome do cliente: ')
        idade = input('Idade do cliente: ')
        email = input('Email do cliente: ')
        telefone = input('Telefone do cliente: ')

        cliente = Cliente(id, nom, idade, email, telefone)

        self.clientes.append(cliente)

        
    def listar_clientes(self):
      
        print(f"Total de clientes: {len(self.clientes)}")

        for cliente in self.clientes:
            print(f"""
    Id: {cliente.id}              
    Nome: {cliente.nome}
    Idade: {cliente.idade}
    Email: {cliente.email}
    Telefone: {cliente.telefone}
    """)

        

    def buscar_cliente(self):
        found = int(input('id do cliente: '))
        for cliente in self.clientes:
            if found == cliente.id:
                print('Ele é nosso cliente')
                break
        else:
            print('Nome digitado errado ou ele não é nosso cliente.')




    def editar_cliente():
        pass

    def excluir_cliente(self):
        fnex = int(input('Id do cliente: '))
        for cliente in self.clientes:
            if fnex == cliente.id:
                ex = input('Voçe esta prester a excluir um cliente tem certeza? (S/N): ').upper()
                match ex:
                    case 'S':
                        self.clientes.remove(cliente)
                        break

                    case 'N':
                        print('Voltando ao menu')

                    case _:
                        print('opção invalida')
                        return
        else:
            print('Id de cliente não encontrado.')


    def salvar(self):
        with open('clientes.json', 'w') as arquivo:
            lista_dict = []
            for Cliente in self.clientes:
                lista_dict.append({
                    "id": Cliente.id,
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
                    cliente["id"], cliente["nome"], cliente["idade"], cliente["email"], cliente["telefone"]
                )
                self.clientes.append(novo_cliente)