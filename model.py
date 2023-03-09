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
