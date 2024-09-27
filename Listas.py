# Creacion de nuestra lista
miLista = [15, 33, 47, 88, 66]
nuevaLista = []

# Acceso por indice en nuestra lista

def acceso_indice():
    print(" ")
    print("Elemento del indice 1: ", miLista[1])  # La salida sera el numero 33


# Modificacion de elementos
def modificacion_elementos():
    print(" ")
    print("Lista sin la modificacion: ", miLista)
    print(" ")
    miLista[2] = 11
    print("Lista después de la modificación: ", miLista)
    print(" ")
    
# Agregar elementos
def agregar_append():
    print(" ")
    print("Lista sin el elemento agregado: ", miLista)
    print(" ")
    miLista.append(256)
    print("Lista después de agregar el elemento: ", miLista)
    print(" ")
    
def agregar_extend():
    print(" ")
    print("Lista sin los elementos agregado: ", miLista)
    print(" ")
    miLista.extend([22, 57, 38])
    print("Lista después de agregar los elementos: ", miLista)
    print(" ")
    
def agregar_insert():
    print(" ")
    print("Lista sin el elemento insertado: ", miLista)
    print(" ")
    miLista.insert(0, 1055)
    print("Lista después de agregar el elemento: ", miLista)
    print(" ")


# Eliminar elementos
def eliminar_remove():
    print(" ")
    print("Lista sin el elemento removido: ", miLista)
    print(" ")
    miLista.remove(33)
    print("Lista después de remover el elemento: ", miLista)
    print(" ")
    
def eliminar_pop():
    print(" ")
    print("Lista sin el elemento removido: ", miLista)
    print(" ")
    elementoEliminado = miLista.pop()
    print("El elemento que fue eliminado es: ", elementoEliminado)  # El pop elimina y devuelve el ultimo elemento
    print("Lista despues del uso de pop", miLista)
    
def eliminar_clear():
    print(" ")
    print("Lista sin aplicar el clear", miLista)
    print(" ")
    miLista.clear()
    print("Lista despues de aplicar el clear", miLista)
    
# Slicing y copiado de listas

def slicing():
    print(" ")
    print("Lista: ", miLista)
    print(" ")
    subLista = miLista[1:4]
    print("Nuestra subLista es: ", subLista)
    print(" ")
    
def copiado():
    print(" ")
    print("Lista: ", miLista)
    print(" ")
    copiaLista = miLista[:]
    print("Nuestra lista copiada es: ", copiaLista)
    
def forIteracion():
    print(" ")
    print("Lista: ", miLista)
    for Lista in miLista:
        print("Imprime cada elemento en la consola: ", Lista)
    print(" ")
    print("Obtener los numeros pares de nuestra lista con for")
    for x in miLista:
        if x % 2 == 0:
            nuevaLista.append(x)
            print(nuevaLista)
            
def compresionLista():
    nuevaLista = [x for x in miLista if x % 2 == 0]
    print(nuevaLista)
# Ejecutar nuestra funcion    

compresionLista()

