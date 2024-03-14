#Vamos voltar para a classe Usuario que desenvolvemos nas atividades anteriores. Agora vamos definir o primeiroNome do usuário como uma propriedade privada (private).

class Usuario:
    def __init__(self):
        self._primeiroNome = ""
        self._ultimoNome = ""

    @property
    def primeiroNome(self):
        return self._primeiroNome

    @primeiroNome.setter
    def primeiroNome(self, value):
        self._primeiroNome = value

    @property
    def ultimoNome(self):
        return self._ultimoNome

    @ultimoNome.setter
    def ultimoNome(self, value):
        self._ultimoNome = value

    def hello(self):
        return f"Olá, {self._primeiroNome} {self._ultimoNome}"

# Exemplo de uso
usuario = Usuario()
usuario.primeiroNome = "João"
usuario.ultimoNome = "Silva"
print(usuario.hello())  # Saída: Olá, João Silva
