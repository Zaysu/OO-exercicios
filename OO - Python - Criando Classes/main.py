import carro

mustant = carro.Carro("Vermelho", 4, "Flex", 2.0, 0, False, 50)
mustant.ligar()
mustant.abastecer()
print(f"A quantidade de combusivel desse carro: {mustant.qtd_combustivel}")




porshe = carro.Carro("verde", 2, "Flex", 2.0, 0, False, 50)
porshe.desligar()
print(f"A quantidade de combusivel desse carro: {porshe.qtd_combustivel}")
porshe.ligar()
porshe.acelerar()
