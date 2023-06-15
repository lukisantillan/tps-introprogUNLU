def ingresaPeliculas(n):
    titulo= list()
    visuali= list()
    for i in range(0, n):
        pregunta1= input("Ingrese titulo: ")
        pregunta2= int(input("ingrese visitas:    "))
        titulo.append(pregunta1)
        visuali.append(pregunta2)
    return titulo,visuali

videos, cantidad= ingresaPeliculas()


def procesamiento(videos,cantidad):
    argentina= "No hay un video que se llame argentina"
    mayorV= -1
    mayorT= ""
    suma= 0
    for i in range(len(videos)):
        suma += cantidad[i]
        if cantidad[i] >= mayorV:
            mayorV = cantidad[i]
            mayorT= videos[i]
        if videos[i] == "argentina":
            argentina= "Existe el video"
    promedio= round(suma/len(cantidad), 2)
    return argentina,promedio,mayorT

a,p,m= procesamiento(videos,cantidad)

print(f"el promedio de visitas es {p}")
print(f"el titulo con mas visitas es {m}")
print(a)

def numeros(n):
    listaN=list()
    if n > 100:
        for i in range(100, n+1):
            if i%2== 0 and i%5==0:
                listaN.append(i)
                cantidad+= 1
        print(listaN)
        return(len(listaN))
       

def ingresaEmpleados(n):
    empleado= list()
    edad= list()
    for i in range(0, n):
        pregunta1= input("Ingrese empleado: ")
        pregunta2= int(input("ingrese edad:    "))
        empleado.append(pregunta1)
        edad.append(pregunta2)
    gustavo= 0
    mayorE= 0
    mayorN= ""
    for n in range(len(empleado)):
        if edad[i] >= mayorE:
            mayorE = edad[i]
            mayorN= empleado[i]
        if empleado[i] == "Gustavo":
            gustavo +=1
    if "Pedro" in empleado:
        print("Existe pedro")
    print(f"La cantidad de gustavos que hay es {gustavo}")
    return mayorN

