# Creacion de nuestra Tupla
miTupla = (5, 2, 22, 33, 57, 245, 307, 46, 22)

def acceso_indice():
    print(" ")
    print("Elemento del indice 1: ", miTupla[1])  # La salida sera el numero 2
    print(" ")
    
def metodo_count():
    print(" ")
    print("Cuanta veces aparece el valor: ", miTupla.count(22)) # Retorna la cantidad de veces que un valor aparece en la tupla
    print(" ")
    
def metodo_index():
    print(" ")
    print("Devuelve el indice: ", miTupla.index(22)) # Devuelve el índice de la primera aparición de un valor específico.
    print(" ")
    
    
def conversion_tupla():
    print(" ")
    miLista = [12, 24, 55, 60, 80]
    miTupla = tuple(miLista)
    print("Mi lista convertida a Tupla", miLista)
    print(" ")
    
    
def conversion_lista():
    print(" ")
    miLista = list(miTupla)
    print("Mi Tupla convertida a Lista", miLista)
    print(" ")
    
    
    
    
conversion_lista()
