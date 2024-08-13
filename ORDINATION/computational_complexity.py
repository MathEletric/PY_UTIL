# A complexidade computacional é o estudo do uso da memoria em função da velocidade
# de um algoritimo.

# Podemos usar a biblioteca time para medir o desempenho de um código em termos
# de tempo de execução.
from time import time
from class_ordination import Ordenacao

class complexidade_computacional:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0
        self.t3 = 0

    def imprime_resultado(self):
        print(f'Tempo para bubble sort: {self.t2-self.t1}')
        print(f'Tempo para drect selection: {self.t3 - self.t2}')
    def compara_bubble_selection(self, tamanho):
        lista_aleatoria_bubble = Ordenacao().gera_lista_aleatoria(tamanho)
        lista_aleatoria_selection = lista_aleatoria_bubble[:]

        self.t1 = time()
        Ordenacao().bubble_sort(lista_aleatoria_bubble)
        self.t2 = time()
        Ordenacao().direct_selection(lista_aleatoria_selection)
        self.t3 = time()
        self.imprime_resultado()

        lista_quase_ordenada = Ordenacao().gera_lista_quase_ordenada(tamanho)
        self.t1 = time()
        Ordenacao().bubble_sort(lista_quase_ordenada)
        self.t2 = time()
        Ordenacao().direct_selection(lista_quase_ordenada)
        self.t3 = time()
        self.imprime_resultado()

# É notavel que para uma lista quase ordenada o bubble sort melhora o desempenho,
# porém, não supera a seleção direta.
complex_comp = complexidade_computacional().compara_bubble_selection(10000)






