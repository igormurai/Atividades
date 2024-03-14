#• Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma ooutro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if self.bucho:
            print(f"{self.nome} está com o seguinte conteúdo no estômago:")
            for alimento in self.bucho:
                print("- " + alimento)
        else:
            print(f"{self.nome} está com o estômago vazio.")

    def digerir(self):
        self.bucho = []

# Criando dois macacos
macaco1 = Macaco("Chico")
macaco2 = Macaco("Bola")

# Alimentando os macacos com três alimentos diferentes
macaco1.comer("banana")
macaco1.comer("maçã")
macaco1.comer("laranja")

macaco2.comer("peixe")
macaco2.comer("carne")
macaco2.comer("vegetais")

# Verificando o conteúdo do estômago de cada macaco
macaco1.verBucho()
macaco2.verBucho()

# Fazendo o macaco1 comer o macaco2
macaco1.comer("Bola")

# Verificando o conteúdo do estômago do macaco1 após a "refeição"
macaco1.verBucho()
