#Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

#a. Atributos: Nome, Fome, Saúde e Idade

#b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade

class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def calcularHumor(self):
        humor = (self.fome + self.saude) / 2
        return humor

# Criando uma instância da classe BichinhoVirtual
bichinho = BichinhoVirtual(nome="Rex", fome=5, saude=8, idade=2)

# Exibindo os atributos do bichinho
print("Nome:", bichinho.retornarNome())
print("Fome:", bichinho.retornarFome())
print("Saúde:", bichinho.retornarSaude())
print("Idade:", bichinho.retornarIdade())

# Calculando o humor do bichinho
humor = bichinho.calcularHumor()
print("Humor:", humor)
