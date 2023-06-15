"""
#1
def grados():
    intentos = 1
    grados_check = True
    grado = int(input("Ingrese la cantidad de grados actuales [valores entre -18 y 50]: "))
    while grados_check:
        if grado > -18 and grado< 50:
            grados_check = False
            resultado = (f"La cantidad de grados que hace actualmente son {grado}")
        elif intentos < 10:
            intentos += 1
            grado= int(input("el numero ingresado no es del formato esperado, recuerde ingresar los grados entre el rango de -18 y 50:    "))
        elif intentos == 10:
            grados_check = False
            resultado= "SE ALCANZÓ EL MAXIMO DE INTENTOS"
    print(resultado)
grados()

#2
def edad():
    intentos = 1
    edad_check = True
    edad = int(input("Ingrese un valor de edad(18 años a 50 años): "))
    while edad_check:
        if edad > 18 and edad < 60:
            edad_check = False
            resultado = (f"La edad que usted tiene es {edad}")
        elif intentos < 10:
            intentos += 1
            edad= int(input(
                "el numero ingresado no es del formato esperado, recuerde ingresar solo el numero de la edad y con el rango entre 18-60:    "))
        elif intentos == 10:
            edad_check = False
            resultado= "SE ALCANZÓ EL MAXIMO DE INTENTOS"
    print(resultado)
edad()
"""
# 5

import os


def colorFavorito():
    color = input("INGRESE SU COLOR FAVORITO: ").upper()
    color_check = True
    chequeo2 = True
    while color_check:
        if color != 'AZUL' and color != 'ROJO' and color != 'VERDE':
            chequeo2 = True
            print('**DATO INVALIDO**')
            print(f'{1} REINTENTAR')
            print(f'{2} SALIR')
            opciones = int(input('INGRESE LA OPCION SOLICITADA: '))
            while chequeo2:
                if opciones == 2:
                    os.system("cls")
                    resultado = "SALISTE DEL PROGRAMA"
                    chequeo2 = False
                    color_check = False
                elif opciones == 1:
                    color = input("INGRESE SU COLOR FAVORITO: ").upper()
                    if color != 'AZUL' and color != 'ROJO' and color != 'VERDE':
                        chequeo2 = False
                        color_check= True
                    elif color == 'AZUL' or color == 'ROJO' or color == 'VERDE':
                        resultado = color
                        chequeo2 = False
                        color_check = False
                elif  opciones < 1 or opciones > 2:
                        chequeo2 = False
                        color_check= True
        else:
            resultado = color
            color_check = False
    os.system("cls")
    print(resultado)

colorFavorito()
