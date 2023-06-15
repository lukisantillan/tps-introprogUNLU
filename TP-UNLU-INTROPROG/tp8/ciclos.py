#1
"""
def palabras():
    centinela = input("Ingrese una palabra(Ingrese [parar] para terminar):    ")
    while centinela != "parar":
        print(centinela)
        centinela = input("Ingrese una palabra(Ingrese [parar] para terminar):    ")
    print("--TERMINADO--")
palabras()


#2
def notas():
    acumulador = 0
    nota= 0
    centinela = int(input("Ingrese su calificación(-1 para terminar):   "))
    while centinela != -1:
        if centinela > -1 and centinela <= 10:
            acumulador += 1
            nota += centinela
        else: 
            print("Error. Vuelva a ingresar un valor valido")
        centinela = int(input("Ingrese su calificación(-1 para terminar):   "))
    if acumulador != 0:
        resultado = nota/acumulador
    else: 
        resultado = 0
    print(f"El promedio es {resultado}")
notas()


#3 
def numero():
    centinela= (input("Ingrese un numero(rango entre 1-100)"))
    while not centinela.isdigit() or int(centinela) < 1 or int(centinela) > 100:
        if not centinela.isdigit():
            resultado= "--EL DATO INGRESADO NO ES UN NUMERO--"
        elif int(centinela) < 1 or int(centinela) > 100:
            resultado= "--EL DATO INGRESADO ESTA FUERA DEL RANGO--"
        print(resultado)
        centinela= (input("Ingrese un numero(rango entre 1-100)"))
    print(f"El numero {centinela} es correcto!")
        
numero()

"""

#4
'''
import os
def programaParaMostrarCosas():
    condicion= True
    while condicion:
        print("********MI PROGRAMA********")
        print("1. SALUDAR")
        print("2. INFORMAR TEMPERATURA")
        print("3. MOSTRAR NOMBRE DE MATERIA")
        print("4. SALIR")
        centinela = int(input("SELECCIONE UNA OPCIÓN [1-4]:     "))
        if centinela == 1:
            resultado = "HOLA, BIENVENIDO AL PROGRAMA"
            centinela = (input("PRESIONE ENTER PARA LIMPIAR LA PANTALLA"))
            os.system("cls")
        elif centinela == 2:
            resultado ="LA TEMPERATURA ACTUAL ES 22 GRADOS"
            centinela = (input("PRESIONE ENTER PARA LIMPIAR LA PANTALLA"))
            os.system("cls")
        elif centinela == 3:
            resultado = "EL NOMBRE DE LA MATERIA ES : INTRODUCCION A LA PROGRAMACIÓN"
            centinela = (input("PRESIONE ENTER PARA LIMPIAR LA PANTALLA"))
            os.system("cls")
        elif centinela == 4:
            condicion = False
            resultado= "FINALIZÓ EL PROGRAMA"
        else:
            resultado = "INGRESASTE UN NUMERO INCORRECTO"
            centinela = (input("PRESIONE ENTER PARA LIMPIAR LA PANTALLA"))
            os.system("cls")
        print(resultado)
programaParaMostrarCosas()
'''

        

  