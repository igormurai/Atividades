#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta,nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque. No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque de R$", valor, "realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

# Criando uma instância da classe ContaCorrente
conta = ContaCorrente(numero_conta="123456", nome_correntista="João da Silva", saldo=1000)

# Imprimindo os atributos da conta corrente
print("Número da Conta:", conta.numero_conta)
print("Nome do Correntista:", conta.nome_correntista)
print("Saldo:", conta.saldo)

# Alterando o nome do correntista
conta.alterarNome("Maria Silva")

# Imprimindo o nome atualizado do correntista
print("Nome do Correntista (após alteração):", conta.nome_correntista)

# Realizando um depósito
conta.deposito(500)

# Imprimindo o saldo após o depósito
print("Saldo após depósito:", conta.saldo)

# Realizando um saque
conta.saque(700)

# Imprimindo o saldo após o saque
print("Saldo após saque:", conta.saldo)
