#Crie um objeto chamado usuario1. Depois defina seu primeiro nome como "Joe" e faça com que ele retorne este nome.

class Usuario:
    def __init__(self):
        self._primeiroNome = ""

    @property
    def primeiroNome(self):
        return self._primeiroNome

    def set_primeiroNome(self, novo_nome):
        self._primeiroNome = novo_nome

    def get_primeiroNome(self):
        return self._primeiroNome

    def hello(self):
        return f"Olá, {self._primeiroNome}"

# Criando um objeto usuario1
usuario1 = Usuario()

# Definindo o primeiro nome como "Joe"
usuario1.set_primeiroNome("Joe")

# Obtendo e imprimindo o primeiro nome
print(usuario1.get_primeiroNome())  # Saída: Joe
