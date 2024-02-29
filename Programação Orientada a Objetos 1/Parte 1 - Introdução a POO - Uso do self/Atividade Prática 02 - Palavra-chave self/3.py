
class Usuario():
    # as propriedades
    primeiroNome = ""
    ultimoNome = ""

    # método que diz Olá ao usuário
    def hello(self):
        return f"Olá, {self.primeiroNome}"

# Agora a classe Usuario está definida

# Criando um novo objeto Usuario
novo_usuario = Usuario()

# Atribuindo os valores para primeiroNome e ultimoNome
novo_usuario.primeiroNome = "Jonnie"
novo_usuario.ultimoNome = "Bravo"

# Chamando o método hello() para imprimir a saída
print(novo_usuario.hello())  # Saída: Olá, Jonnie