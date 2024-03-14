#Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

#a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

#i. tipoCombustivel.

#ii. valorLitro

#iii. quantidadeCombustivel

class BombaDeCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Abastecimento concluído. Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}."
        else:
            return "Não há combustível suficiente na bomba."

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_combustivel:
            valor_a_pagar = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            return f"Abastecimento concluído. Valor a pagar: R$ {valor_a_pagar:.2f}."
        else:
            return "Não há combustível suficiente na bomba."

    def encher_tanque(self):
        self.quantidade_combustivel = float('inf')
        return f"Tanque da bomba de {self.tipo_combustivel} foi completamente abastecido."

    def alterar_valor_litro(self, novo_valor):
        self.valor_litro = novo_valor
        return f"Valor do litro de {self.tipo_combustivel} alterado para R$ {novo_valor:.2f}."

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        return f"Quantidade de {self.tipo_combustivel} na bomba alterada para {nova_quantidade:.2f} litros."


# Exemplo de uso:
if __name__ == "__main__":
    bomba_gasolina = BombaDeCombustivel("gasolina", 5.80, 1000)  # Inicializando uma bomba de gasolina
    print(bomba_gasolina.abastecer_por_valor(50))  # Abastecer R$ 50
    print(bomba_gasolina.abastecer_por_litro(20))  # Abastecer 20 litros
    print(bomba_gasolina.encher_tanque())  # Encher completamente o tanque
    print(bomba_gasolina.alterar_valor_litro(6.00))  # Alterar valor do litro
    print(bomba_gasolina.alterar_quantidade_combustivel(1500))  # Alterar quantidade de combustível

#b. Possua no mínimo esses métodos:

#i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo

#ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.

#iii. alterarValor( ) – altera o valor do litro do combustível.

#iv. alterarCombustivel( ) – altera o tipo do combustível.

#v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    
class BombaDeCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Abastecimento concluído. Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}."
        else:
            return "Não há combustível suficiente na bomba."

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_combustivel:
            valor_a_pagar = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            return f"Abastecimento concluído. Valor a pagar: R$ {valor_a_pagar:.2f}."
        else:
            return "Não há combustível suficiente na bomba."

    def alterar_valor_litro(self, novo_valor):
        self.valor_litro = novo_valor
        return f"Valor do litro de {self.tipo_combustivel} alterado para R$ {novo_valor:.2f}."

    def alterar_tipo_combustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo
        return f"Tipo de combustível alterado para {novo_tipo}."

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        return f"Quantidade de {self.tipo_combustivel} na bomba alterada para {nova_quantidade:.2f} litros."


# Exemplo de uso:
if __name__ == "__main__":
    bomba_gasolina = BombaDeCombustivel("gasolina", 5.80, 1000)  # Inicializando uma bomba de gasolina
    print(bomba_gasolina.abastecer_por_valor(50))  # Abastecer R$ 50
    print(bomba_gasolina.abastecer_por_litro(20))  # Abastecer 20 litros
    print(bomba_gasolina.alterar_valor_litro(6.00))  # Alterar valor do litro
    print(bomba_gasolina.alterar_tipo_combustivel("álcool"))  # Alterar tipo de combustível
    print(bomba_gasolina.alterar_quantidade_combustivel(1500))  # Alterar quantidade de combustível

