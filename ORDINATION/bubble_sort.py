# Bubble sort ou ordenação de bolha é o algorítimo mais clássico para ordenação
# de uma lista.
def main():
    lista = [1, 2, 3, 4, 5]
    lista_ordenada = bubble_sort(lista)
    print(lista_ordenada)

def bubble_sort(lista_desordenada):
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
    return lista_desordenada

if __name__ == "__main__":
    main()