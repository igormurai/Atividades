#Crie um método para definir o valor da propriedade primeiroNome. Use o modificador de acesso correto para ele.

class Usuario:
    def __init__(self):
        self._primeiroNome = ""

    @property
    def primeiroNome(self):
        return self._primeiroNome

    def set_primeiroNome(self, novo_nome):
        self._primeiroNome = novo_nome

    def hello(self):
        return f"Olá, {self._primeiroNome}"

# Exemplo de uso
usuario = Usuario()
usuario.set_primeiroNome("João")
print(usuario.hello())  # Saída: Olá, João
