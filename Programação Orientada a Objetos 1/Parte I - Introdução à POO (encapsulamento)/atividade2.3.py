#Agora, crie um método para retornar o valor primeiroNome.

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

# Exemplo de uso
usuario = Usuario()
usuario.set_primeiroNome("João")
print(usuario.get_primeiroNome())  # Saída: João
