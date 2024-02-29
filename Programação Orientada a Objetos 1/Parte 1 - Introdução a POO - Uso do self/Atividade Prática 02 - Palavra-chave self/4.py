#4. Use o comando print no método hello() para o objeto usuario1 e observe o resultado.

class Usuario():
    # as propriedades
    primeiroNome = ""
    ultimoNome = ""

    # método que diz Olá ao usuário
    def hello(self):
        return f"Olá, {self.primeiroNome}"

# Criando um objeto Usuario
usuario1 = Usuario()

# Atribuindo um valor para primeiroNome
usuario1.primeiroNome = "Carlos"

# Usando o comando print no método hello() para o objeto usuario1
print(usuario1.hello())  # Saída: Olá, Carlos