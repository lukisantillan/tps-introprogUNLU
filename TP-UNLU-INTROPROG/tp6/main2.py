from trabajo_seis import (
    saludo_por_numero2, comparacion_de_resultados, numero_positivo, condicion_de_alumno, que_tipo_es,dia_de_la_semana)


def main():
    que_tipo_es("222")
    numero = int(input("Ingarese su numero.. "))
    saludo_por_numero2(numero)
    numero1 = int(input("Ingrese su numero.. "))
    numero2 = int(input("Ingrese su numero.. "))
    comparacion_de_resultados(numero1, numero2)
    numero_positivo(numero)
    nota1 = int(input("Ingrese la nota del primer parcial.. "))
    nota2 = int(input("Ingrese la nota del segundo parcial.. "))
    condicion_de_alumno(nota1, nota2)
    dia_de_la_semana()
main()
