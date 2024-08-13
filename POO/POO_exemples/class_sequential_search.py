from random import randrange

class GeradorBuscador:
    def __init__(self):
        self.lista_aleatoria = []
        self.indice = None

    def imprime_listas(self, NUM):
        if self.lista_aleatoria:
            print(self.lista_aleatoria)
        else:
            print(f'O objeto não tem lista aleatória ainda.')
        

    def gera_lista_aleatoria(self, n):
        for i in range(n):
            self.lista_aleatoria.append(randrange(10))
        self.imprime_listas()

    def buscador_v1(self, valor):
        for i in range(len(self.lista_aleatoria)):
            if self.lista_aleatoria[i] == valor:
                indice = i
                self.imprime_listas
                return indice
            else:
                return -1
    
    def buscador_v2(self, valor):
         if valor in self.lista_aleatoria:
            return self.lista_aleatoria.index(valor)
         else:
             return -1

lista_obj = GeradorBuscador()
lista_obj.gera_lista_aleatoria(10)
lista_obj.buscador_v1(9)

