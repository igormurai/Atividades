#Crie uma propriedade na classe Usuario chamada primeiroNome e evite que qualquer código de fora da classe altere o seu valor, usando o modificador de acesso apropriado.

class Usuario:
    def __init__(self):
        self._primeiroNome = ""

    @property
    def primeiroNome(self):
        return self._primeiroNome

    def hello(self):
        return f"Olá, {self._primeiroNome}"

# Exemplo de uso
usuario = Usuario()
usuario._primeiroNome = "João"  # Tentativa de atribuição fora da classe
print(usuario.hello())  # Saída: Olá, João
