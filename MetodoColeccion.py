miLista = [12, 55, 22, 66, 48, 57, 112, 44, 544, 12]  

def coleccion_sort():
    print(" ")  
    miLista.sort()    # Ordena los elementos de la lista en orden ascendente.
    print(miLista)
    print(" ")
    
def coleccion_reverse():
    print(" ")
    miLista.reverse()    # Ordena los elementos de la lista en orden descendente.
    print(miLista)
    print(" ")
    
def coleccion_count():
    print(" ")  
    print(miLista.count(12)) # Nos devuelve la veces que se repete el numero 12.
    print(" ")
    
def coleccion_index():
    print(" ")  
    print(miLista.index(22)) # Devuelve el índice de la primera aparición de un elemento en la lista.
    print(" ")

coleccion_index()