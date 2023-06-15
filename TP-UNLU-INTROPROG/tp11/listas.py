"""
def listaDeN():
    ingresarNumero=input("Ingrese un Numero(salir para terminar):   ").upper()
    listaDeNumeros= list()
    while ingresarNumero != "SALIR":
        if ingresarNumero.isdigit():
            listaDeNumeros.append(ingresarNumero)
            ingresarNumero=input("Ingrese un Numero(salir para terminar):   ").upper()
    print(listaDeNumeros)
listaDeN()


def numerosE(l,k):
    numerosEnteros= list()
    numerosMenores= list()
    numerosMayores= list()
    numerosIguales= list()
    numerosMultiplos= list()
    for i in range(len(l)):
        numerosEnteros.append(int(l[i]))
    for i in numerosEnteros:
        if i > k and i :
            numerosMayores.append(i)
        elif i < k and i :
            numerosMenores.append(i) 
        elif i == k and i :
            numerosIguales.append(i)
        if i % k == 0:
            numerosMultiplos.append(i)
        
    print(numerosMayores,numerosMenores,numerosIguales, numerosMultiplos)
numerosE([3, 6, 9, 12, 15, 18, 21, 4, 1], 3)

def listaInvertida(l):
    listaInver= list()
    longitud= len(l)
    for i in range(longitud-1,-1,-1):
        listaInver.append(l[i])
    print(listaInver)

L1=['Di', 'buen', 'día', 'a', 'papa']
listaInvertida(L1)

def listaInvertida(l):
    print(l[::-1])

L1=['Di', 'buen', 'día', 'a', 'papa']
listaInvertida(L1)

def cadenaAbuscar(c,l):
    listaElementos= list()
    for i in l:
        if c.lower() in i.lower():
            listaElementos.append(i)
    print(listaElementos)
cadenaAbuscar("cas",["Lucas Santillán","Juana Ricarda","Focas","Luciano", "Caracas"])
"""
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeroEnteroP(l):
    numerosEnteros= list()
    numerosPrimos= list()
    for i in range(len(l)):
        numerosEnteros.append(int(l[i]))
    for i in numerosEnteros:
        if es_primo(i):
            numerosPrimos.append(i)
    return(numerosPrimos)

def numeroEnteroS(l):
    numerosEnteros= list()
    sumatoria= 0
    for i in range(len(l)):
        numerosEnteros.append(int(l[i]))
    for i in numerosEnteros:
        sumatoria += i
    return(sumatoria)

def numeroEnteroF(l):
    numerosEnteros= list()
    factorial= 1
    for i in range(len(l)):
        numerosEnteros.append(int(l[i]))
    for i in numerosEnteros:
        factorial*=i
    return(factorial)

def test2a():
    assert numeroEnteroP([2, 3, 5, 7, 11, 13,10,8,4]) == [2, 3, 5, 7, 11, 13]
    assert numeroEnteroP([2,3,5,7,1]) == [2,3,5,7]
    print("Pasó")
test2a()

def test2b():
    assert numeroEnteroS([2, 3, 5, 7]) == 17
    assert numeroEnteroS([2,3]) == 5
    print("Pasó")
test2b()

def test2c():
    assert numeroEnteroF([2, 3, 5,7]) == 210
    assert numeroEnteroF([2,3,2]) ==12
    print("Pasó")
test2c()