miDiccionario = {
    
    "Nombre": "Gabriel",
    "Apellido" : "Garcia Rivas",
    "Edad" : 21
}
print(" ")
print("Mi diccionario es: ", miDiccionario)

def acceso_clave():
    print(" ")
    nombre = miDiccionario["Nombre"]
    print(nombre)
    print(" ")
    
    
def modificar_clave():
    print(" ")
    miDiccionario["edad"] = 22
    print("Su nueva edad es", miDiccionario["edad"])
    print(" ")

def agregar_clave():
    print(" ")
    miDiccionario["profesion"] = "Estudiante"
    print(miDiccionario)
    print(" ")
 
def pop_clave():
    print(" ")
    edad = miDiccionario.pop("Edad")
    print(miDiccionario)
    print(" ")
    
def del_clave():
    print(" ")
    del miDiccionario["Edad"]
    print(miDiccionario)
    print(" ")

def clear_clave():
    print(" ")
    miDiccionario.clear()
    print(miDiccionario)
    print(" ")

def keys_clave():
    print(" ")
    claves = miDiccionario.keys()
    print(claves)
    print(" ")
    
def values_clave():
    print(" ")
    valores = miDiccionario.values()
    print(valores)
    print(" ")
    
def items_clave():
    print(" ")
    items = miDiccionario.items()   # Devuelve una vista de los pares clave-valor como tuplas.
    print(items)
    print(" ")

def get_clave():
    print(" ")
    nombre = miDiccionario.get("Nombre")
    print(nombre)
    print(" ")
    
def update_clave():
    print(" ")
    miDiccionario.update({"Edad": 25, "Profesion": "Estudiante"})
    print(miDiccionario)
    print(" ")
    
def iteracion_clave():
    print(" ")
    for clave in miDiccionario.keys():
        print(clave)
    print(" ")
    
def iteracion_valor():
    print(" ")
    for valor in miDiccionario.values():
        print(valor)
    print(" ")

def iteracion_claveValor():
    print(" ")
    for clave, valor in miDiccionario.items():
        print(f"{clave}: {valor}")
    print(" ")
    
iteracion_claveValor()
