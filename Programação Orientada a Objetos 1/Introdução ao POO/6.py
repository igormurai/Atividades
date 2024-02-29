#6. Escreva a classe Usuario e adicione as propriedades e o método (em Python):

class Usuario:
    def __init__(self, nome_usuario, email):
        self.nome_usuario = nome_usuario
        self.email = email

    def exibir_informacoes(self):
        return f"Nome de Usuário: {self.nome_usuario}\nEmail: {self.email}"

# Exemplo de uso:
usuario1 = Usuario("igormurai", "igormurai@gmail.com")
informacoes_do_usuario = usuario1.exibir_informacoes()
print(informacoes_do_usuario)
