class BinarySearch:

    def binary_search(self, num, lista_ordenada):
        
        num_q = lista_ordenada[len(lista_ordenada)//2]
        indice = len(lista_ordenada)//2
        while num != num_q:
            if num > num_q:
                lista_ordenada = lista_ordenada[len(lista_ordenada)//2:]
                indice += len(lista_ordenada)//2 
                num_q = lista_ordenada[len(lista_ordenada)//2]
            else:
                lista_ordenada = lista_ordenada[:len(lista_ordenada)//2]
                indice -= len(lista_ordenada)//2
                num_q = lista_ordenada[len(lista_ordenada)//2]

        return indice

x = BinarySearch()
print(x.binary_search('e', ['a', 'e', 'i']))










