#1. Acrescente à classe Usuario um método construtor para definir um valor para a propriedade primeiroNome assim que o objeto for criado.

class Usuario():
    def __init__(self, primeiro_nome):
        self.primeiroNome = primeiro_nome
        self.ultimoNome = ""

# Exemplo de uso:
# Criando um objeto Usuario e definindo o primeiro nome ao mesmo tempo
usuario1 = Usuario("João")

# Acessando as propriedades
print(usuario1.primeiroNome)  # Saída: João
print(usuario1.ultimoNome)    # Saída: (vazio, pois ainda não foi definido)
