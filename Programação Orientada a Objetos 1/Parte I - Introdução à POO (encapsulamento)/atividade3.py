#Crie uma classe chamada Empregado(), com três propriedades: nome, salario (deve ser privada) e projeto. Ela também possui um método chamado “trabalho()”, que deverá imprimir o nome do funcionário e o projeto em que ele está trabalhando e um outro método chamado “mostrar()” para exibir os detalhes desse empregado (i.e. nome e salário). Atente para o modificador de acesso da propriedade “salario”. Use o método adequado para ter acesso a ela. Crie um objeto desta classe (i.e. instância) e use os métodos para visualizar os dados.

class Empregado:
    def __init__(self, nome, salario, projeto):
        self.nome = nome
        self._salario = salario
        self.projeto = projeto

    @property
    def salario(self):
        return self._salario

    def trabalho(self):
        print(f"{self.nome} está trabalhando no projeto {self.projeto}")

    def mostrar(self):
        print(f"Nome: {self.nome}, Salário: {self.salario}")

# Criando um objeto empregado1
empregado1 = Empregado("João", 5000, "Projeto A")

# Usando os métodos para visualizar os dados
empregado1.trabalho()  # Saída: João está trabalhando no projeto Projeto A
empregado1.mostrar()   # Saída: Nome: João, Salário: 5000
