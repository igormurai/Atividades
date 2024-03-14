#Classe Pessoa: Crie uma classe que modele uma pessoa:

#a. Atributos: nome, idade, peso e altura

#b. Métodos: envelhecer, engordar, emagrecer, crescer.

#Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# Criando uma instância da classe Pessoa
pessoa = Pessoa(nome="Maria", idade=20, peso=60, altura=160)

# Exibindo os atributos iniciais da pessoa
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Peso:", pessoa.peso)
print("Altura:", pessoa.altura)

# Fazendo a pessoa envelhecer por 1 ano
pessoa.envelhecer()

# Exibindo os atributos da pessoa após envelhecer 1 ano
print("\n--- Após envelhecer 1 ano ---")
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Peso:", pessoa.peso)
print("Altura:", pessoa.altura)

# Fazendo a pessoa engordar e emagrecer
pessoa.engordar(5)
pessoa.emagrecer(3)

# Exibindo os atributos da pessoa após engordar e emagrecer
print("\n--- Após engordar 5 kg e emagrecer 3 kg ---")
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Peso:", pessoa.peso)
print("Altura:", pessoa.altura)
