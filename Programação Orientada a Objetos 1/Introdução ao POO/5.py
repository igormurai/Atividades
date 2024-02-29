#5. Escreva o que você acha que deveria ser o nome da classe, os nomes das propriedades para o primeiro e último nome (sobrenome) e o nome do método que retorna “Olá”.

class Pessoa:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
    def cumprimentar(self):
        return f"Olá, {self.primeiro_nome} {self.sobrenome}!"

# Exemplo de uso:
pessoa1 = Pessoa("Igor", "Murai")
mensagem_de_cumprimento = pessoa1.cumprimentar()
print(mensagem_de_cumprimento)