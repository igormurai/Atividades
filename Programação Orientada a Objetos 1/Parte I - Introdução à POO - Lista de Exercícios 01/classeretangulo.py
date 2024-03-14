#Classe Retangulo: Crie uma classe que modele um retangulo:

#a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

#b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

#c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidadesde um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)

# Programa principal
if __name__ == "__main__":
    # Pedindo ao usuário para informar as medidas do local
    ladoA = float(input("Informe o comprimento do local: "))
    ladoB = float(input("Informe a largura do local: "))

    # Criando um objeto Retangulo com as medidas informadas
    local = Retangulo(ladoA, ladoB)

    # Calculando a área e o perímetro do local
    area = local.calcularArea()
    perimetro = local.calcularPerimetro()

    # Calculando a quantidade de pisos e rodapés necessários
    quantidade_pisos = area // 1  # Considerando que cada piso cobre 1 metro quadrado
    quantidade_rodapes = perimetro // 1  # Considerando que cada rodapé cobre 1 metro linear

    # Exibindo os resultados
    print("\n--- Resultados ---")
    print("Área do local:", area, "metros quadrados")
    print("Perímetro do local:", perimetro, "metros")
    print("Quantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)
