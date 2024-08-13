# Um algorítimo que ordena uma lista de valores.

def main():
    lista_desordenada = [7, 5, 2, 7, 2, 3]
    print(direct_selection(lista_desordenada))
    pass

def direct_selection(lista):

    for i in range(len(lista)):
        indice_do_menor = i
        for j in range(i, len(lista)):
            if lista[j] < lista[indice_do_menor]:
                indice_do_menor = j

        lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]
    return lista

if __name__ == "__main__":
    main()