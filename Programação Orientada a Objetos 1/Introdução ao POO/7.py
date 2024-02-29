#7. Supondo que você tenha uma classe chamada Usuario
class Usuario:
    def __init__(self, primeiro_nome, ultimo_nome):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome

# Criando uma instância chamada usuario1
usuario1 = Usuario(primeiro_nome="John", ultimo_nome="Doe")

# Agora você pode acessar os atributos dessa instância
print(f"Primeiro Nome: {usuario1.primeiro_nome}")
print(f"Último Nome: {usuario1.ultimo_nome}")
