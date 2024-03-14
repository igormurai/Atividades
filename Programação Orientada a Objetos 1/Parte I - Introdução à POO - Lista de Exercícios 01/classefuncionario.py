#Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario


# Exemplo de uso:
if __name__ == "__main__":
    funcionario1 = Funcionario("João", 2500.0)
    funcionario2 = Funcionario("Maria", 3000.0)

    print(f"Nome do funcionário 1: {funcionario1.obter_nome()}")
    print(f"Salário do funcionário 1: R$ {funcionario1.obter_salario():.2f}")

    print(f"Nome do funcionário 2: {funcionario2.obter_nome()}")
    print(f"Salário do funcionário 2: R$ {funcionario2.obter_salario():.2f}")

#Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
    
#Exemplo de uso:
    
#harry = funcionário("Harry",25000)

#harry.aumentarSalario(10)
    
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentar_salario(self, porcentagem_de_aumento):
        aumento = self.salario * (porcentagem_de_aumento / 100)
        self.salario += aumento
        print(f"O salário de {self.nome} foi aumentado em {porcentagem_de_aumento}%. Novo salário: R$ {self.salario:.2f}")


# Exemplo de uso:
if __name__ == "__main__":
    harry = Funcionario("Harry", 25000)
    print(f"Salário atual de {harry.obter_nome()}: R$ {harry.obter_salario():.2f}")
    harry.aumentar_salario(10)  # Aumentar o salário em 10%
