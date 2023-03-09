from model import *

p1 = Pessoa('João', 'Escola')
p1.info()
c1 = Cliente('Maria', 'Souza', 1000)
c1.info()
v1 = Vendedor('Osmar', 'Ferreira', '10')
v1.info()
print(v1.nome_completo())
