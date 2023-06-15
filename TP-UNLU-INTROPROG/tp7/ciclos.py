# 1
'''
for i in range(1,101):
    print(i)

#2
for i in range(1,101):
    if i % 2 == 0 :
        print(i)

#3
def sumarNumerosDeTalAtal(n1,n2):
    contador = 0
    for i in range (n1,n2 +1):
        contador += i
    print(contador)

#4

def nota():
    notaEnviada= int(input("Ingrese la nota.. ))
    acumulador = 1
    for i in range(1, notaEnviada +1):
        acumulador*= i
    print (acumulador)
       

nota1= int(input("Ingrese nota:  "))
nota(nota1)

#5 

def numeroPosOneg():
    for i in range(1, 10+1):
        a = int(input("Ingrese n:  "))
        if a>0:
            resultado = "Positivo"
        elif a==0 :
            resultado="Igual a 0"
        else:
            resultado= "Negativo"
        print(resultado)
    

numeroPosOneg()


def numeroPosOneg_conCentinela():
    centinela= (input("Ingrese n(escriba: fin) para terminar :  "))
    while centinela != "fin":
        a = int(centinela)
        if a>0:
            resultado = "Positivo"
        elif a==0 :
            resultado="Igual a 0"
        else:
            resultado= "Negativo"
        print(resultado)
        centinela= (input("Ingrese n(escriba: fin) para terminar :  "))

numeroPosOneg_conCentinela()


#6

def ingreseNumeros():
    for i in range(1, 11):
        x = int(input("Ingrese el numero"))
        if i == 1:
            mayor = x
            posicionMayor = i
            posicionMenor= i
            menor = x
        if x > mayor:
            mayor = x
            posicionMayor = i
        elif x < menor:
            menor = x
            posicionMenor = i
    print(f"El mayor numero ingresado es {mayor} y lo ingresaste en la posicion: {posicionMayor} y el menor es : {menor} y lo ingresaste en la posicion {posicionMenor}")
ingreseNumeros()


# 7


def ingreseNumeros():
    numeros = []
    for i in range(10):
        num = int(input("Ingrese numero : "))
        numeros.append(num)
    numeroMasAlto = max(numeros)
    numeroMasBajo = min(numeros)
    posicionAlto = numeros.index(numeroMasAlto) + 1
    posicionBajo = numeros.index(numeroMasBajo) + 1
    print(f"El numero {numeroMasAlto} es el mayor y lo ingresaste en la posicion {posicionAlto}, El mas bajo es {numeroMasBajo} y lo pusiste en la posicion {posicionBajo}")


ingreseNumeros()


# 8


def ingresarMililitros():
    litros = 0
    for i in range(1, 8):
        numero = int(input("Ingrese el numero"))
        if i == 1:
            max = numero
        else:
            if numero > max:
                max = numero
                dia = i 
        litros +=  numero
    if dia == 1:
        nombreDia = "Domingo"
    elif dia==2 :
        nombreDia = "Lunes"
    elif dia== 3:
        nombreDia = "Martes"
    elif dia==4:
        nombreDia = "Miercoles"
    elif dia==5 :
        nombreDia = "Jueves"
    elif dia== 6:
        nombreDia = "Viernes"
    elif dia== 7:
        nombreDia = "Sabado"
    promedio = litros/7
    print(f"El dia con mas mililitros es  {nombreDia}")
    print(f"El promedio de mililitros es {int(promedio)}")
ingresarMililitros()


# 9


def nota(n1):
    acumulador = 1
    for i in range(1, n1 + 1):
        acumulador *= i
    return acumulador
 

def test_nota():
    assert nota(2) == 2
    assert nota(10) == 3628800
    assert nota(5) == 120
    print("Pasó!")
test_nota()
'''


def numeroPosOneg_conCentinela():
    centinela= (input("Ingrese n(escriba: fin) para terminar :  "))
    while centinela != "fin":
        a = int(centinela)
        if a>0:
            resultado = "Positivo"
        elif a==0 :
            resultado="Igual a 0"
        else:
            resultado= "Negativo"
        print(resultado)
        centinela= (input("Ingrese n(escriba: fin) para terminar :  "))

#numeroPosOneg_conCentinela()

def numeroPosOneg(x):
    if x>0:
            resultado = "Positivo"
    elif x==0 :
            resultado="Igual a 0"
    else:
            resultado= "Negativo"
    return resultado

def masNumeros():
    iteracion= "SI"
    while iteracion== "SI":
        print(numeroPosOneg_conCentinela())
        iteracion= input("Quiere continuar <SI-NO> :    ").upper()
masNumeros()
    
