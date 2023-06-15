# 1

var1 = 'Hola mundo'
var2 = "Hola mundo"
var3 = 100
var4 = '100'

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

'''
El tipo de dato de las cadenas de texto son "String", se pueden escribir con comillas simples o dobles, segun lo que investigue
su diferencia es simplemente estetica, no es lo mismo que una variable tenga el valor 100 a "100", ya que varia el tipo de dato, con 
las comillas es un string y sin las comillas es un Number entero
'''

# 2
mi_valor = 'Hola'

'''
El operador + en string nos concatena los mismos, los une, el operador * nos repite el string la cantidad de veces que queramos,
uno al lado del otro, El problema en el codigo que tenemos arriba es que estamos tratando de utilizar un operador en dos tipos diferentes de datos,
y teniendo en cuenta que este operador funciona de manera diferente con Strings y con numbers, no logra compatibilizar entre ambos, ni realizar
una funcion. Y en el error nos aclara que solo puede concatenar string con string.
'''

# 3
# Len(), nos sirve para saber la longitudo del string, por ejemplo
len("Lucas")
# esto nos devolvera 5

# .lower() sirve para pasar el string a minusculas
"LUCAS".lower()
# esto nos devolvera lucas

# .upper() sirve para pasar el string a mayusculas
"lucas".upper()
# esto nos devolvera LUCAS

# .capitalize() sirve para poner la primera letra en mayuscula
"lucas".capitalize()
# esto nos devolvera Lucas

# .replace(x,y) sirve para reemplazar una parte del texto por otra, en el primer parametro debemos enviar la parte a reemplazar y en el segundo
# por lo que lo queremos reemplazar
string1 = "Lucas"
stringcambiado = string1.replace("Luc", "Ñuc")
# la variable stringcambiado será "Ñucas"

# .count(letra) sirve para contar la cantidad de veces que se repite el caracter que ingresamos como parametro dentro del string.
string = "mama"
cantidadDeRepeticion = string.count("a")
# esto nos devolvera 2 ya que la letra a se repite 2 veces

# .isnumeric() sirve para saber si lo que se almacena dentro del string es un numero o no, devuelve true o false, depende si lo es o no
numero = "10"
numero.isnumeric()
letra = "abc"
letra.isnumeric()
# la variable numero retornará True y la variable letra False, ya que lo que almacena no es un numero

# .isspace nos sirve para chequear si el string es un espacio en blanco, si lo es retorna True y si no lo es False
espacio = " "
espacio.isspace()
stringVacio = ""
stringVacio.isspace()

# En el caso de espacio devolverá True, en el caso de string vacio devolverá False, ya que no es un espacio

#.endswith(parametro) nos devuelve True en caso de que el parametro sea el final del strign.
print("lucas".endswith("a"))
#esto vevolvera True
"""
#4
def ingreseSuNombre():
    nombre= input("Ingrese su nombre:   ")
    for i in nombre:
        print(i)
ingreseSuNombre()

#5
def ingreseOracion():
    oracion= input("Ingrese oración:   ")
    if "ñ" in oracion and "hola" in oracion:
        resultado= "La oracion contiene la letra ñ y la palabra hola"
    else:
        resultado= "La oracion no contiene ni la letra ñ, ni la palabra hola"
    print(resultado)
ingreseOracion()

#6
def ingresePalabra():
    palabra= input("Ingrese palabra:    ")
    check4= True
    while check4:
        check1= palabra.isspace()
        check2= palabra.isnumeric()
        check3= palabra.count("ñ")
        if  check1 or  check2 or check3 < 1:
            resultado = "EL DATO INGRESADO NO ES CORRECTO"
            palabra= input("reingrese la palabra:    ")
        else: 
            resultado =(f"La cantidad de letras que tiene la palabra son {len(palabra)}")
            stringEditado= palabra.upper().replace('Ñ', 'N')
            check4= False
    print(resultado, stringEditado)
ingresePalabra()

#7
def devuelveCaracteres():
    palabra = input("Ingrese la palabra :   ")
    longitudPalabra= len(palabra)
    dosDigitos= palabra[0:2]
    tresUltimos= palabra[longitudPalabra-3: longitudPalabra]
    palabraInvertida= palabra[::-1]
    print(dosDigitos, longitudPalabra,tresUltimos,palabraInvertida)
devuelveCaracteres()

def cadena():
    numero= (input("Ingrese numero:  "))
    longitudNumero= len(numero)
    if longitudNumero < 4:
        resultado= numero
    else:
        contador=0
        numeroNuevo=""
        for i in range(longitudNumero-1,-1,-1):
            if contador < 3:
                numeroNuevo = numero[i] + numeroNuevo 
                contador +=1
                resultado= numeroNuevo
            elif contador == 3:
                numeroNuevo= numero[i] + "." + numeroNuevo
                contador = 1
                resultado= numeroNuevo
    print(resultado)
cadena()

def consonantes(t):
    texto=""
    for i in t:
        if i not in "aeiou":
         texto+=i
    return(texto)
consonantes('algoritmos')

def binario(nb):
    numeroInvertido= nb[::-1]
    sumador= 0
    for i in range(len(numeroInvertido)):
        sumador += (int(numeroInvertido[i]) * (2**i))
    return(sumador)




def test_ejercicio9():
    assert consonantes("algoritmos")=="lgrtms"
    assert consonantes("hola")=="hl"
    assert consonantes("tu mama")=="t mm"
    print("Pasó!!")
test_ejercicio9()

def test_ejercicio10():
    assert binario("101")== 5
    assert binario("1000")==8
    assert binario("11")== 3
    print("Pasó!!")
test_ejercicio10()
"""