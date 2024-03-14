#Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        if self.fome == 0 and self.tedio == 0:
            return f"{self.nome} está muito feliz!"
        elif self.fome == 0:
            return f"{self.nome} está alimentado, mas entediado."
        elif self.tedio == 0:
            return f"{self.nome} está com fome, mas se divertindo."
        else:
            return f"{self.nome} está com fome e entediado."

    def mostrar_status(self):
        print(f"Nível de fome de {self.nome}: {self.fome}")
        print(f"Nível de tédio de {self.nome}: {self.tedio}")


# Exemplo de uso:
if __name__ == "__main__":
    bichinho = BichinhoVirtual("Rex")

    comida_fornecida = int(input("Quantidade de comida fornecida: "))
    tempo_brincadeira = int(input("Tempo de brincadeira: "))

    bichinho.alimentar(comida_fornecida)
    bichinho.brincar(tempo_brincadeira)

    print(bichinho.humor())
    bichinho.mostrar_status()

#Crie uma "porta escondida" no programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.
    
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        if self.fome == 0 and self.tedio == 0:
            return f"{self.nome} está muito feliz!"
        elif self.fome == 0:
            return f"{self.nome} está alimentado, mas entediado."
        elif self.tedio == 0:
            return f"{self.nome} está com fome, mas se divertindo."
        else:
            return f"{self.nome} está com fome e entediado."

    def mostrar_status(self):
        print(f"Nível de fome de {self.nome}: {self.fome}")
        print(f"Nível de tédio de {self.nome}: {self.tedio}")

    def __str__(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}"


# Exemplo de uso:
if __name__ == "__main__":
    bichinho = BichinhoVirtual("Rex")

    while True:
        print("1. Alimentar o bichinho")
        print("2. Brincar com o bichinho")
        print("3. Ver humor do bichinho")
        print("4. Ver status do bichinho")
        print("5. Opção secreta")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            comida_fornecida = int(input("Quantidade de comida fornecida: "))
            bichinho.alimentar(comida_fornecida)
        elif escolha == '2':
            tempo_brincadeira = int(input("Tempo de brincadeira: "))
            bichinho.brincar(tempo_brincadeira)
        elif escolha == '3':
            print(bichinho.humor())
        elif escolha == '4':
            bichinho.mostrar_status()
        elif escolha == '5':
            print("Opção secreta selecionada:")
            print(bichinho)
        else:
            print("Opção inválida. Por favor, escolha novamente.")

#Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nível inicial aleatório de fome e tédio.
    
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)  # Nível inicial de fome aleatório
        self.tedio = random.randint(0, 100)  # Nível inicial de tédio aleatório

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        if self.fome == 0 and self.tedio == 0:
            return f"{self.nome} está muito feliz!"
        elif self.fome == 0:
            return f"{self.nome} está alimentado, mas entediado."
        elif self.tedio == 0:
            return f"{self.nome} está com fome, mas se divertindo."
        else:
            return f"{self.nome} está com fome e entediado."

    def mostrar_status(self):
        print(f"Nível de fome de {self.nome}: {self.fome}")
        print(f"Nível de tédio de {self.nome}: {self.tedio}")

    def __str__(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}"


# Função para alimentar todos os bichinhos na fazenda
def alimentar_fazenda(bichinhos, quantidade_comida):
    for bichinho in bichinhos:
        bichinho.alimentar(quantidade_comida)

# Função para brincar com todos os bichinhos na fazenda
def brincar_fazenda(bichinhos, tempo_brincadeira):
    for bichinho in bichinhos:
        bichinho.brincar(tempo_brincadeira)

# Função para mostrar humor de todos os bichinhos na fazenda
def humor_fazenda(bichinhos):
    for bichinho in bichinhos:
        print(bichinho.humor())


# Exemplo de uso:
if __name__ == "__main__":
    num_bichinhos = int(input("Quantidade de bichinhos na fazenda: "))
    fazenda = []

    for i in range(num_bichinhos):
        fazenda.append(BichinhoVirtual(f"Bichinho {i+1}"))

    while True:
        print("\n--- Menu da Fazenda de Bichinhos ---")
        print("1. Alimentar todos os bichinhos")
        print("2. Brincar com todos os bichinhos")
        print("3. Ver humor de todos os bichinhos")
        print("4. Ver status de todos os bichinhos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            quantidade_comida = int(input("Quantidade de comida fornecida para todos os bichinhos: "))
            alimentar_fazenda(fazenda, quantidade_comida)
        elif escolha == '2':
            tempo_brincadeira = int(input("Tempo de brincadeira para todos os bichinhos: "))
            brincar_fazenda(fazenda, tempo_brincadeira)
        elif escolha == '3':
            humor_fazenda(fazenda)
        elif escolha == '4':
            for bichinho in fazenda:
                bichinho.mostrar_status()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
