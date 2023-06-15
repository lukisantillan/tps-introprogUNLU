#1 El minimo y maximo de iteraciones depende de los chequeos que nostros hagamos, si solo precisamos 5 libros, y esta puesto en las
# condiciones del programa, el minimo de iteraciones que puede hacer este programa es de 5 y el maximo de 200, si en ningun lado se especifica
# esta condicion de que sean 5, el maximo y minimo será iguales, y es 200, ya que el ciclo al empezar debera terminar tambien

#2 
def ingreseWeb(n):
    titulos=[]
    numeroDeInscriptos=[]
    for i in range(n):
        pregunta1=input('Titulo de webinar: ')
        pregunta2= int(input('Cantidad de inscriptos(ingrese solo numeros): '))
        titulos.append(pregunta1)
        numeroDeInscriptos.append(pregunta2)
    return titulos, numeroDeInscriptos

def procesamientoDeWebinars(list1,list2):
    sumaDeAlumnos= 0
    mayorCantidadDeAlumnos= 0
    nombreConMayorAlumnos = ''
    for i in range(len(list1)):
        sumaDeAlumnos += list2[i]
        if list2[i] >= mayorCantidadDeAlumnos:
            mayorCantidadDeAlumnos = list2[i]
            nombreConMayorAlumnos = list1[i]
    promedio = sumaDeAlumnos/len(list1)
    return nombreConMayorAlumnos, promedio

#3 
def producto(n,m):
    producto= 1
    for i in range(n,m+1):
        producto*=i
    print(producto)
#Recordar que para que salga bien necesito calcular los valores que necesito para las iteraciones, por que si tengo en cuenta solo las iteraciones
#no consigo el resultado, ya que el ultimo no me lo itera. 
def precioLibros(n):
    precio= []
    nombre= []
    for i in range(n):
        lib=int(input("Ingrese Precio del libro:    "))
        nom=input("Ingrese nombre del libro:    ")
        precio.append(lib)
    return precio,nombre

def procesamiento(l1,l2):
    librosMayorPrecio= []
    for i in range(3):
        if l2[i] > 300:
            librosMayorPrecio.append(l1[i])
    return librosMayorPrecio

def main():
    n=int(input('Ingrese cantidad(numero(:  )'))
    preci, nombr = precioLibros(n)
    libros = procesamiento(nombr,preci)
    print(libros)
main()