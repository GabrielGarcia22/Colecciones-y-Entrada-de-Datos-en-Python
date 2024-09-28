vehiculos = {
        "ABC125" : {"modelo": "Toyota Corolla", "año": 2015},
        "CBA725" : {"modelo": "Honda Fit", "año": 2017},
        "BAC125" : {"modelo": "Honda Accord", "año": 2012},
        "CAB128" : {"modelo": "Hyundai Sonata", "año": 2020},
    }

def asignacion_1():
    usuario = ("Gabriel", "Garcia", 23,)
    print(" ")
    print(f"Nombre: {usuario[0]}")
    print(f"Apellido: {usuario[1]}")
    print(f"Edad: {usuario[2]}")
    print(" ")
    

def asignacion_2(matricula):
    return vehiculos.get(matricula, "Vehiculo no encontrado")
print(" ")   
matricula = input("Cual es la matricula de su vehiculo? ")
info_vehiculo = asignacion_2(matricula)
print(f"Informacion del vehiculo con matricula {matricula}: {info_vehiculo}")
print(" ")
    
    
asignacion_2(matricula)