# Classe Conta de Investimento: Faça uma classe chamada contaInvestimento que seja semelhante à classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100  # Convertendo a taxa de juros para decimal

    def adicione_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros

    def obter_saldo(self):
        return self.saldo


# Exemplo de uso:
if __name__ == "__main__":
    poupanca = ContaInvestimento(1000, 10)  # Saldo inicial de R$1000,00 e taxa de juros de 10%
    for _ in range(5):
        poupanca.adicione_juros()  # Aplicar método adicioneJuros() cinco vezes
    print(f"Saldo resultante após aplicar juros: R$ {poupanca.obter_saldo():.2f}")
