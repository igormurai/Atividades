#Classe Carro: Implemente uma classe chamada Carro com as seguintes propriedades:

#a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.

#b. O consumo é especificado no construtor e o nível de combustível inicial é 0.

#c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.

#d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.

#e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

#meuFusca = Carro(15) # 15 quilômetros por litro de combustível.

#meuFusca.adicionarGasolina(20) # abastece com 20 litros de combustível.

#meuFusca.andar(100) # anda 100 quilômetros.

#meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.

class Carro:
    def __init__(self, consumo_km_por_litro):
        self.consumo_km_por_litro = consumo_km_por_litro
        self.nivel_combustivel = 0

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo_km_por_litro
        if combustivel_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= combustivel_necessario
            print(f"O carro percorreu {distancia} quilômetros.")
        else:
            print("Combustível insuficiente. O carro não pode percorrer a distância desejada.")

    def obter_gasolina(self):
        return self.nivel_combustivel

    def adicionar_gasolina(self, quantidade):
        self.nivel_combustivel += quantidade
        print(f"Tanque abastecido com {quantidade} litros de combustível.")


# Exemplo de uso:
if __name__ == "__main__":
    meu_fusca = Carro(15)  # 15 quilômetros por litro de combustível
    meu_fusca.adicionar_gasolina(20)  # abastece com 20 litros de combustível
    meu_fusca.andar(100)  # anda 100 quilômetros
    print(f"Restam {meu_fusca.obter_gasolina()} litros de combustível no tanque.")
