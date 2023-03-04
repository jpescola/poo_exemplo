class Pessoa:
    def __init__(self, pnome, snome):
        self.nome = pnome
        self.sobrenome = snome
        self.tipo = 'Pessoa'

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def info(self):
        print(self.nome_completo(), self.tipo)


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, renda):
        super().__init__(nome, sobrenome)
        self.renda = renda
        self.tipo = 'Cliente'


class Vendedor(Pessoa):
    def __init__(self, nome, sobrenome, comissao):
        super().__init__(nome, sobrenome)
        self.comissao = comissao
        self.tipo = 'Vendedor'


p1 = Pessoa('João', 'Escola')
p1.info()
c1 = Cliente('Maria', 'Souza', 1000)
c1.info()
v1 = Vendedor('Osmar', 'Ferreira', '10')
v1.info()
print(v1.nome_completo())
