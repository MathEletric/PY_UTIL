class Carro:
    def __init__(self, a=2000, m='Chevrolet', vm=180):
        self.ano = a
        self.modelo = m
        self.vel_max = vm
        self.velocidade = 0

    def imprimir(self):
        if self.velocidade == 0:
            print(f'Velocidade igual a zero.')
        elif self.velocidade == self.vel_max:
            print(f'Carro está a velocidade máxima: {self.vel_max}')
        elif self.velocidade == self.vel_max/2:
            print(f'Carro está na metade da velocidade: {self.velocidade}')
        elif self.velocidade > self.vel_max/2:
            print(f'Velocidade muito alta. Reduza mais {self.velocidade - self.vel_max/2}')
        elif self.velocidade < self.vel_max/2:
            print('Velocidade abaixo da metade.')
            print(f'Ano: {self.ano}\nModelo: {self.modelo}')

    def acelerar(self, vel_var):
        self.velocidade += vel_var
        if self.velocidade > self.vel_max:
            self.velocidade = self.vel_max
        self.imprimir()

    def pare(self):
        self.velocidade = 0
        self.imprimir()



carro_um = Carro()
carro_dois = Carro(2024, 'Ferrari', 220)
carro_um.acelerar(170)
print(carro_um.velocidade)
carro_um.pare()
