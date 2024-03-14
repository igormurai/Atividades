#Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

#a. Possua uma classe chamada Ponto, com os atributos x e y.

#b. Possua uma classe chamada Retangulo, com os atributos largura e altura.

#c. Possua uma função para imprimir os valores da classe Ponto

#d. Possua uma função para encontrar o centro de um Retângulo.

#e. Você deve criar alguns objetos da classe Retangulo.

#f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.

#g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

#h. O valor do centro do objeto deve ser mostrado na tela

#i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicio, largura, altura):
        self.ponto_inicio = ponto_inicio
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        centro_x = self.ponto_inicio.x + self.largura / 2
        centro_y = self.ponto_inicio.y + self.altura / 2
        return Ponto(centro_x, centro_y)


# Função para criar um retângulo e mostrar seu centro
def criarRetangulo():
    x = float(input("Digite a coordenada x do ponto de início do retângulo: "))
    y = float(input("Digite a coordenada y do ponto de início do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    ponto_inicio = Ponto(x, y)
    retangulo = Retangulo(ponto_inicio, largura, altura)
    return retangulo


# Função para exibir o menu
def exibirMenu():
    print("\n--- Menu ---")
    print("1. Criar Retângulo")
    print("2. Encontrar Centro do Retângulo")
    print("3. Sair")
    return input("Escolha uma opção: ")


# Programa principal
if __name__ == "__main__":
    while True:
        opcao = exibirMenu()

        if opcao == "1":
            retangulo = criarRetangulo()
        elif opcao == "2":
            if 'retangulo' in locals():
                centro = retangulo.encontrarCentro()
                print("O centro do retângulo é:")
                centro.imprimir()
            else:
                print("Crie um retângulo primeiro.")
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
