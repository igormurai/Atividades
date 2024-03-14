#Implemente uma classe chamada Pessoa que tenha dois atributos privados chamados “primeiroNome” e “ultimoNome”, respectivamente. Em seguida, implemente métodos chamados “getPrimeiroNome()” e “getUltimoNome()”, para ler os atributos, e os métodos “setPrimeiroNome()” e “setUltimoNome()” para atribuir valores a eles. Depois crie uma instância da classe Pessoa definindo os seguintes valores:
#primeiroNome = 'João'
#ultimoNome = 'Carvalho'
#Após, imprima os valores desses atributos no console.

class Pessoa:
    def __init__(self):
        self._primeiroNome = None
        self._ultimoNome = None

    def getPrimeiroNome(self):
        return self._primeiroNome

    def setPrimeiroNome(self, novo_nome):
        self._primeiroNome = novo_nome

    def getUltimoNome(self):
        return self._ultimoNome

    def setUltimoNome(self, novo_nome):
        self._ultimoNome = novo_nome

# Criando uma instância da classe Pessoa
pessoa = Pessoa()

# Definindo os valores dos atributos primeiroNome e ultimoNome
pessoa.setPrimeiroNome("João")
pessoa.setUltimoNome("Carvalho")

# Imprimindo os valores desses atributos no console
print("Primeiro Nome:", pessoa.getPrimeiroNome())  # Saída: João
print("Último Nome:", pessoa.getUltimoNome())      # Saída: Carvalho
