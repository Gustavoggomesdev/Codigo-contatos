class ContactNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None

class PhoneBook:
    def __init__(self):
        self.root = None

    def insert(self, name, phone):
        if not self.root:
            self.root = ContactNode(name, phone)
        else:
            self._insert(self.root, name, phone)

    def _insert(self, current_node, name, phone):
        if name < current_node.name:
            if current_node.left is None:
                current_node.left = ContactNode(name, phone)
            else:
                self._insert(current_node.left, name, phone)
        elif name > current_node.name:
            if current_node.right is None:
                current_node.right = ContactNode(name, phone)
            else:
                self._insert(current_node.right, name, phone)
        else:
            print(f"Contato com o nome {name} já existe.")

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, current_node, name):
        if current_node is None:
            return None
        if name < current_node.name:
            return self._search(current_node.left, name)
        elif name > current_node.name:
            return self._search(current_node.right, name)
        else:
            return current_node

    def list_contacts(self):
        contacts = []
        self._inorder_traversal(self.root, contacts)
        return contacts

    def _inorder_traversal(self, current_node, contacts):
        if current_node:
            self._inorder_traversal(current_node.left, contacts)
            contacts.append((current_node.name, current_node.phone))
            self._inorder_traversal(current_node.right, contacts)

    def remove(self, name):
        self.root = self._remove(self.root, name)

    def _remove(self, current_node, name):
        if current_node is None:
            return current_node

        if name < current_node.name:
            current_node.left = self._remove(current_node.left, name)
        elif name > current_node.name:
            current_node.right = self._remove(current_node.right, name)
        else:
            
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left


            temp = self._min_value_node(current_node.right)
            current_node.name = temp.name
            current_node.phone = temp.phone
            current_node.right = self._remove(current_node.right, temp.name)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


if __name__ == "__main__":
    phone_book = PhoneBook()

    while True:
        print("\n1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Listar todos os contatos")
        print("4. Remover contato")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Digite o nome do contato: ")
            phone = input("Digite o número de telefone do contato: ")
            phone_book.insert(name, phone)
            print(f"Contato {name} adicionado com sucesso.")
        elif choice == "2":
            name = input("Digite o nome do contato que deseja buscar: ")
            contact = phone_book.search(name)
            if contact:
                print(f"Nome: {contact.name}, Telefone: {contact.phone}")
            else:
                print("Contato não encontrado.")
        elif choice == "3":
            contacts = phone_book.list_contacts()
            if contacts:
                print("Lista de contatos:")
                for name, phone in contacts:
                    print(f"Nome: {name}, Telefone: {phone}")
            else:
                print("Nenhum contato encontrado.")
        elif choice == "4":
            name = input("Digite o nome do contato que deseja remover: ")
            phone_book.remove(name)
            print(f"Contato {name} removido com sucesso.")
        elif choice == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")
