#5. Obtenha o nome completo e imprima-o na tela.

class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome):
        self.primeiroNome = primeiro_nome
        self.ultimoNome = ultimo_nome

    def getNomeCompleto(self):
        return f"{self.primeiroNome} {self.ultimoNome}"

# Criando um novo objeto Usuario com os valores do primeiro e último nome
usuario1 = Usuario("Johnny", "Bravo")

# Obtendo o nome completo
nome_completo_usuario1 = usuario1.getNomeCompleto()

# Imprimindo o nome completo na tela
print(nome_completo_usuario1)  # Saída: Johnny Bravo

