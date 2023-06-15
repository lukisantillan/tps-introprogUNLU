#def para definir una funcion, etc
def operacion (x,y) :
    suma = x + y
    return suma
print("el resultado de la suma es ", operacion(2,4)  )

#abs para ver valor absoluto
numero = -10
funcionAbsoluto = abs(numero)
print(funcionAbsoluto)

#len para contar cantidad de caracteres

nombre = "lucas"
funcionConteo = len(nombre)
print("lucas tiene " + str(funcionConteo) + " letras")

#pow para hacer potenciación

numeroBase = 2
numeroExponente = 3

funcionElevar = pow(numeroBase, numeroExponente)

print("El numero "+ str(numeroBase) + " elevado en "+ str(numeroExponente) + " da como resultado " + str(funcionElevar))


#calcular perimetro de un cuadrado  int para pedir numero entero

altura = int(input("Ingresa la medida de la altura:"))
base = int(input("Ingresa la medida de la base:"))

perimetro = 2 * (base + altura)
area = base * altura

print("el perimetro mide " +  str(perimetro))
print("el area mide " + str(perimetro))

#intercambio de datos en asignacion multiple

def algoritmoCambio(variable1,variable2):
    print(variable1, variable2)
    variable1, variable2 = variable2, variable1
    return variable1, variable2

print(algoritmoCambio(1,2))

###intercambio de datos en variables
a= 10
b= 2
print(a,b)
auxiliar = b
b = a
a = auxiliar
###############################

def promedio(parcial1,parcial2) : 
    notaCompleta = parcial1 + parcial2
    promedio = (notaCompleta/2)
    return "El promedio del  es... " + str( (promedio))
print(promedio(5,9))


#########

def conversion(): 
    pesos = float(input("ingrese su dinero:"))
    dolar = pesos / 80.5
    euro = pesos / 69.5
    real = pesos / 14.1
    print("Usted tiene " + str(pesos) + " pesos argentinos, los cuales se convierten en: ")
    print("- U$"+ str(((dolar)) + " dolares"))
    print("- R$"+ str(round((euro)) + " reales"))
    print("- U$"+ str(round((real)) + " reales"))
print(conversion())


print(abs(10.42))
