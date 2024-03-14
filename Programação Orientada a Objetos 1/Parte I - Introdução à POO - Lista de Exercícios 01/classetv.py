#Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Televisor:
    def __init__(self):
        self.canal = 1
        self.volume = 10

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido. O número do canal deve estar entre 1 e 100.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo atingido.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo atingido.")

# Função para exibir o menu
def exibirMenu():
    print("\n--- Menu ---")
    print("1. Mudar Canal")
    print("2. Aumentar Volume")
    print("3. Diminuir Volume")
    print("4. Desligar Televisor")
    return input("Escolha uma opção: ")

# Programa principal
if __name__ == "__main__":
    televisao = Televisor()

    while True:
        print("\nCanal:", televisao.canal)
        print("Volume:", televisao.volume)
        
        opcao = exibirMenu()

        if opcao == "1":
            novo_canal = int(input("Digite o número do canal desejado: "))
            televisao.mudarCanal(novo_canal)
        elif opcao == "2":
            televisao.aumentarVolume()
        elif opcao == "3":
            televisao.diminuirVolume()
        elif opcao == "4":
            print("Desligando o televisor.")
            break
        else:
            print("Opção inválida.")
