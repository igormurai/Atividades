#10. Use o método que retorna “Olá” com as variáveis primeiro nome e último nome para dizer Olá ao usuário.

class Usuario:
    def __init__(self, primeiro_nome, sobrenome, nome_usuario, email):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.nome_usuario = nome_usuario
        self.email = email

    def exibir_informacoes(self):
        return f"Nome: {self.primeiro_nome} {self.sobrenome}\nNome de Usuário: {self.nome_usuario}\nEmail: {self.email}"

    def cumprimentar(self):
        return f"Olá, {self.primeiro_nome} {self.sobrenome}!"

# Criando a primeira instância da classe Usuario e definindo valores para o nome e email
usuario1 = Usuario("Igor", "Murai", "igormurai", "igormurai@gmail.com")

# Obtendo o nome e sobrenome do usuário
nome_do_usuario = usuario1.primeiro_nome
sobrenome_do_usuario = usuario1.sobrenome

# Imprimindo na tela
print("Nome do usuário:", nome_do_usuario)
print("Sobrenome do usuário:", sobrenome_do_usuario)

# Usando o método cumprimentar para dizer "Olá" ao usuário
mensagem_ola = usuario1.cumprimentar()

# Imprimindo a mensagem na tela
print(mensagem_ola)
