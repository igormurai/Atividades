#2. Acrescente ao método hello() a capacidade de acessar a propriedade primeiroNome, para que o método possa retornar a string "Olá, primeiroNome".

class Usuario():
    # as propriedades
    primeiroNome = ""
    ultimoNome = ""

    # método que diz Olá ao usuário
    def hello(self):
        return f"Olá, {self.primeiroNome}"

# Exemplo de uso
usuario = Usuario()
usuario.primeiroNome = "João"
print(usuario.hello())  # Saída: Olá, João
