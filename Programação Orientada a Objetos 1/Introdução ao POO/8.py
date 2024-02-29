8. Defina os valores do primeiro e último nome para usuario1.

class Usuario:
    def __init__(self, primeiro_nome, sobrenome, nome_usuario, email):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.nome_usuario = nome_usuario
        self.email = email

    def exibir_informacoes(self):
        return f"Nome: {self.primeiro_nome} {self.sobrenome}\nNome de Usuário: {self.nome_usuario}\nEmail: {self.email}"

# Criando a primeira instância da classe Usuario e definindo valores para o nome e email
usuario1 = Usuario("Igor", "Murai", "igormurai", "igormurai@gmail.com")

# Exibindo as informações do usuário
informacoes_do_usuario = usuario1.exibir_informacoes()
print(informacoes_do_usuario)
