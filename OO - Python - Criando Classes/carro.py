class Carro():
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velocidade):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0
        
    def __del__(self):
        print("obj removido da memoria")
        
    def abastecer(self, qtd_combustivel):
        self.qtd_combustivel += qtd_combustivel
        
    def ligar(self):
        if self.is_ligado:
            print("O Carro já está ligado")
        else:
            self.is_ligado = True
            print("O Carro Está sendo ligado")
            
    def desligar(self):
        if self.is_ligado == False:
            print("O Carro já está desligado")
        else:
            self.is_ligado = False
            
    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print("O carro está Desligado")