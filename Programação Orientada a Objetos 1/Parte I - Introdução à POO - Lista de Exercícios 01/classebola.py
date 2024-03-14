#Classe Bola: Crie uma classe que modele uma bola:

#a. Atributos: Cor, circunferência, material

#b. Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

# Criando uma instância da classe Bola
bola = Bola(cor="vermelha", circunferencia=10, material="couro")

# Mostrando a cor atual da bola
print("Cor atual da bola:", bola.mostraCor())  # Saída: vermelha

# Trocando a cor da bola
bola.trocaCor("azul")

# Mostrando a nova cor da bola
print("Nova cor da bola:", bola.mostraCor())   # Saída: azul
