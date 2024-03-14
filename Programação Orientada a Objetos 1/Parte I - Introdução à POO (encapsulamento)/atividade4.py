#Crie uma classe chamada Robo(). Ela deverá ter duas propriedades privadas: nome e ano_construcao. Também deverá ter um método de nome “diga_alo()”, para mostrar na tela o nome do robô e seu ano de construção. Crie os métodos “setters” e “getters” necessários. Instancie a classe e use os métodos criados para visualizar / atualizar os dados.

class Robo:
    def __init__(self, nome, ano_construcao):
        self._nome = nome
        self._ano_construcao = ano_construcao

    # Getter para o nome
    def get_nome(self):
        return self._nome

    # Setter para o nome
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    # Getter para o ano de construção
    def get_ano_construcao(self):
        return self._ano_construcao

    # Setter para o ano de construção
    def set_ano_construcao(self, novo_ano):
        self._ano_construcao = novo_ano

    # Método para mostrar o nome e ano de construção do robô
    def diga_alo(self):
        print(f"Olá, eu sou o robô {self._nome}, construído no ano de {self._ano_construcao}")

# Instanciando a classe e utilizando os métodos
robo1 = Robo("R2-D2", 1977)
robo1.diga_alo()  # Saída: Olá, eu sou o robô R2-D2, construído no ano de 1977

# Alterando o nome do robô
robo1.set_nome("C-3PO")
robo1.diga_alo()  # Saída: Olá, eu sou o robô C-3PO, construído no ano de 1977
