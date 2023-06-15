# PUNTO 1
def saludo_por_numero2(numero):
    if (numero > 10):
        print("Tu número " + str(numero) + " es mayor que 10")
    print("Saludos!")


# PUNTO 2


def saludo_por_numero(numero):
    if (numero > 10):
        print("Tu número " + str(numero) + " es mayor que 10")
    elif (numero < 10):
        print("Tu número " + str(numero) + " es menor que 10")
    else:
        print("Tu número " + str(numero) + " es igual que 10")
    print("Saludos!")


# PUNTO 3


def comparacion_de_resultados(numero1, numero2):
    if (numero1 > numero2):
        print(f"El numero {numero1} es mayor que {numero2}")
    elif (numero1 < numero2):
        print(f"El numero {numero1} es menor que {numero2}")
    else:
        print("Los numeros son iguales")


# PUNTO 4

def numero_positivo(numero):
    if (numero < 0):
        print("Su numero es Negativo")
    elif (numero > 0):
        print("Su numero es Positivo")
    else:
        print("Su numero es 0")


# PUNTO 5

def dia_de_la_semana(numeroDeSemana):
    if (numeroDeSemana == 1):
        nombre_dia = "Lunes"
    elif (numeroDeSemana == 2):
        nombre_dia = "Martes"
    elif (numeroDeSemana == 3):
        nombre_dia = "Miercoles"
    elif (numeroDeSemana == 4):
        nombre_dia = "Jueves"
    elif (numeroDeSemana == 5):
        nombre_dia = "Viernes"
    elif (numeroDeSemana == 6):
        nombre_dia = "Sabado"
    elif (numeroDeSemana == 7):
        nombre_dia = "Domingo"
    else:
        nombre_dia = "No es un dia de la Semana"
    
    print(f"Hoy es {nombre_dia}")

# PUNTO 6


def condicion_de_alumno(nota1, nota2):
    promedio = (nota1 + nota2) / 2
    if (nota1 and nota2 > 4 and promedio >= 8):
        estado = "..PROMOVIDO!.."
    elif (nota1 and nota2 >= 4):
        estado = "..REGULAR!.."
    else:
        estado = "..LIBRE:(!!.."
    print(estado)


# PUNTO 7

def que_triangulo_es(medida1, medida2, medida3):
    if (medida1 == medida2 and medida2 == medida3):
        print("El triangulo es equilátero")
    elif(medida1 == medida2 or medida1 == medida3 or medida2 == medida3) :
        print("El triangulo es isósceles")
    else : 
        print("El triangulo es escaleno")

# PUNTO 8

def division(numerador, denominador):
    if(denominador != 0):
        resultadoDeDivision = numerador/denominador
        print(f"El resultado de dividir {str(numerador)} y {str(denominador)} es {str(resultadoDeDivision)}")
    else :
        print("NO SE PUEDE DIVIDR POR 0!")

# PUNTO 9

def que_tipo_es(texto):
    if(texto.isdigit()):
        return("Enviaste numero/s")
    elif(texto.isalpha()) :
        return("Enviaste letras")
    elif(texto.isalnum()):
        return("Enviaste letras y numeros")


def test_que_tipo_es() :
      print("Testeando Funcion que_tipo_es()... ", end="")
      assert que_tipo_es("texto") == "Enviaste letras"
      assert que_tipo_es("numero1") ==  "Enviaste letras y numeros"
      assert que_tipo_es("222") == "Enviaste numero/s"
      print("Funciona!")
test_que_tipo_es()

import math

def resolvente(a,b,c) :
    DentroDeRaiz = pow(b,2) - 4*a*c
    if DentroDeRaiz > 0 :
        resultado1 = (-b + math.sqrt(DentroDeRaiz)) / (2*a)
        resultado2 = (-b - math.sqrt(DentroDeRaiz)) / (2*a)
        return resultado1, resultado2
    elif DentroDeRaiz == 0: 
        resultado1 = -b / (2*a)
        return resultado1

