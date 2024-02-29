#2. Acrescente ao construtor a capacidade de definir o valor da propriedade ultimoNome, bem como a propriedade primeiroNome.

class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome):
        self.primeiroNome = primeiro_nome
        self.ultimoNome = ultimo_nome

# Exemplo de uso:
# Criando um objeto Usuario e definindo ambos os nomes ao mesmo tempo
usuario1 = Usuario("João", "Silva")

# Acessando as propriedades
print(usuario1.primeiroNome)  # Saída: João
print(usuario1.ultimoNome)    # Saída: Silva
