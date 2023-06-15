def edad():
    e= int(input("ingrese su edad   "))
    while int(e):
        if e > 18 and e < 60:
            resultado = (f"su edad es {e}")
        else:
            resultado= ("Ingreso un valor fuera del rango")
            e= int(input("ingrese su edad   "))
    while not int(e):
        resultado= "Ingreso un dato incorrecto"
        e= input("ingrese su edad   ")
    print(resultado)
edad()
