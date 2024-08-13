from random import randrange

class Ordenacao:
    def __init__(self):
        self.lista_bubble = []
        self.lista_direct = []

    def bubble_sort(self, lista_desordenada):
        ordenada = True
        for i in range(1, len(lista_desordenada)):
            for j in range(len(lista_desordenada) - i):
                if lista_desordenada[j] > lista_desordenada[j+1]:
                    var_aux =lista_desordenada[j+1]
                    lista_desordenada[j+1] = lista_desordenada[j]
                    lista_desordenada[j] = var_aux
                    ordenada = False
            if ordenada:
                print('Essa lista já está ordenada.')
                break 
        self.lista_bubble = lista_desordenada

    def direct_selection(self, lista):
        for i in range(len(lista)):
            indice_do_menor = i
            for j in range(i, len(lista)):
                if lista[j] < lista[indice_do_menor]:
                    indice_do_menor = j
            lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]
        self.lista_direct = lista
    
    def gera_lista_aleatoria(self, tamanho):
        self.lista_aleatoria = [randrange(100) for _ in range(tamanho)]
        return self.lista_aleatoria

    def gera_lista_quase_ordenada(self, tamanho):
        lista_quase_ordenada = [i for i in range(tamanho)]
        lista_quase_ordenada[tamanho//10] = -500
        return lista_quase_ordenada 