#Classe Quadrado: Crie uma classe que modele um quadrado:

#a. Atributos: Tamanho do lado

#b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarLado(self, novo_tamanho_lado):
        self.tamanho_lado = novo_tamanho_lado

    def retornarLado(self):
        return self.tamanho_lado

    def calcularArea(self):
        return self.tamanho_lado ** 2

# Criando uma instância da classe Quadrado
quadrado = Quadrado(tamanho_lado=5)

# Mostrando o valor do lado atual do quadrado
print("Tamanho do lado atual:", quadrado.retornarLado())  # Saída: 5

# Mudando o valor do lado do quadrado
quadrado.mudarLado(7)

# Mostrando o novo valor do lado do quadrado
print("Novo tamanho do lado:", quadrado.retornarLado())  # Saída: 7

# Calculando a área do quadrado
print("Área do quadrado:", quadrado.calcularArea())      # Saída: 49
