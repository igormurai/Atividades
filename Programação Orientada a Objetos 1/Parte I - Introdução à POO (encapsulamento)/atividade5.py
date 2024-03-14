#Implemente uma classe chamada Laptop que possua um atributo privado chamado “preco” que armazena o preço do laptop (sem qualquer validação). Em seguida, implemente um método para ler esse atributo chamado “get_preco()” e um método para modificar esse atributo chamado “set_preco()” sem validação também. Em seguida, crie uma instância da classe Laptop siga estas etapas:
#• usando o método “get_preco()” imprima o valor do atributo “preco” na tela
#• usando o método “set_preco()”, defina o valor do atributo “preco” para 3999”

class Laptop:
    def __init__(self):
        self._preco = None

    def get_preco(self):
        return self._preco

    def set_preco(self, novo_preco):
        self._preco = novo_preco

# Criando uma instância da classe Laptop
laptop = Laptop()

# Usando o método get_preco() para imprimir o valor do atributo preco
print("Preço do laptop:", laptop.get_preco())  # Saída: None

# Usando o método set_preco() para definir o valor do atributo preco
laptop.set_preco(3999)

# Usando novamente o método get_preco() para imprimir o valor atualizado do atributo preco
print("Novo preço do laptop:", laptop.get_preco())  # Saída: 3999
