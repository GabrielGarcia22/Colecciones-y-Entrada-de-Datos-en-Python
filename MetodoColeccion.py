miLista = [12, 55, 22, 66, 48, 57, 112, 44, 544, 12]
miTupla = (22, 51, 118, 77, 15, 215, 97, 5)

miDiccionario = {
    
    "Nombre": "Gabriel",
    "Apellido" : "Garcia Rivas",
    "Edad" : 21
}

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
    
def coleccionTupla_count():
    print(" ")
    print("Cuanta veces aparece el valor: ", miTupla.count(22)) # Retorna la cantidad de veces que un valor aparece en la tupla
    print(" ")
    
def coleccionTupla_index():
    print(" ")
    print("Devuelve el indice: ", miTupla.index(22)) # Devuelve el índice de la primera aparición de un valor específico.
    print(" ")
    
    
def coleccionDiccionario_pop():
    print(" ")
    edad = miDiccionario.pop("Edad")
    print(miDiccionario)
    print(" ")

def coleccionDiccionario_popitem():
    print(" ")
    item = miDiccionario.popitem() # Elimina y devuelve el último par clave-valor añadido al diccionario como una tupla.
    print(item)
    print(miDiccionario)
    
def coleccionDiccionario_update():
    print(" ")
    miDiccionario.update({"Edad": 25, "Profesion": "Estudiante"})
    print(miDiccionario)
    print(" ")
    
def coleccionOperaciones_len():
    print(" ")  
    print(len(miLista))   # Devuelve el número de elementos en una colección
    print(len(miTupla))
    print(len(miDiccionario))
    print(" ")
    
def coleccionOperaciones_in():
    print(" ")  
    print(55 in miLista)   # Verifica si un elemento está en una colección
    print(4 in miTupla)
    print("Nombre" in miDiccionario)
    print(" ")
    
def coleccionOperaciones_not_in():
    print(" ")  
    print(55 not in miLista)   # Verifica si un elemento está en una colección
    print(4 not in miTupla)
    print("Nombre" not in miDiccionario)
    print(" ")
    
def coleccionOperaciones_compresionLista():
    print(" ")  
    numeroPares = [x for x in range(11) if x % 2 == 0]
    print(numeroPares)
    print(" ")  
    
    
def coleccionOperaciones_compresionDiccionario():
    print(" ")  
    numeroPares = {x for x in range(11) if x % 2 == 0}
    print(numeroPares)
    print(" ")  
    
coleccionOperaciones_compresionDiccionario()
    

