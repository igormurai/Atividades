#3. Adicione à classe Usuario um método chamado getNomeCompleto() que retorna o nome completo do usuário.

class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome):
        self.primeiroNome = primeiro_nome
        self.ultimoNome = ultimo_nome

    def getNomeCompleto(self):
        return f"{self.primeiroNome} {self.ultimoNome}"

# Exemplo de uso:
# Criando um objeto Usuario e definindo ambos os nomes ao mesmo tempo
usuario1 = Usuario("João", "Silva")

# Obtendo o nome completo
nome_completo = usuario1.getNomeCompleto()
print(nome_completo)  # Saída: João Silva
