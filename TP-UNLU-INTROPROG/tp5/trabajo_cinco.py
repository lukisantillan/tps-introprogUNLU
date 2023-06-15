
#Punto 1 y 2
def sumaAritmetica(num1, num2) :
    suma = num1 + num2
    print('La suma del numero ' + str(num1) + ' y ' + str(num2) + ' es ' + str(suma))
    return suma



#Punto 3 

def conteoDeLetras(nombre):
    cantidadDeLetras = len(nombre)
    print('El nombre : ' + nombre + ' tiene ' + str(cantidadDeLetras) + ' letras.')
    return nombre



#Punto 4 y 9

def elevacion(base, exponente) :
    elevacion = pow(base,exponente)
    return elevacion

def testElevacion():
    print("Testeando Funcion elevacion()... ", end="")
    assert elevacion(10, 3) == 1000
    assert elevacion(3, 2) == 9
    assert elevacion(2,4) == 16
    print("Funciona!")
testElevacion()
#Punto 5 y 6

def mayusAndMinusAlString(string) :
    stringEnMayus = string.upper()
    stringEnMinus= string.lower()
    return stringEnMayus, stringEnMinus


#Punto 7 
def comparacionDeLongitud(nombre1, nombre2) :
    longitudNombreUno = len(nombre1)
    longitudNombreDos = len(nombre2)
    if longitudNombreUno > longitudNombreDos :
        return True
    elif longitudNombreUno < longitudNombreDos:
        return False


def verdadero_falso(nombre1, nombre2) :
    x=len(nombre1) >(nombre2)
    return x
    

