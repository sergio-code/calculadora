##########################
#Proyecto calculadora 1
#subir a Github
#realizado: 11/11/2022
#Programador: Sergio Depetris
############################
#este programa inicial realiza una secuencia de codigos que permiten al Operador mejorar su resultado de busqueda.

number1=int(input("agregar un numero:"))
number2=int(input("agregar otro numero:"))

eleccion = 0

while eleccion != 5:

    print("""
    indique la operacion a realizar: 

    1) suma
    2) resta
    3) multiplicacion
    4) division
    5) volver a inicio
    """) 
       
    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("resultado: ", number1,"+", number2,"=", number1+number2)

    if eleccion == 2:
        print("")
        print("resultado:", number1,"-", number2,"=", number1-number2)

    if eleccion == 3:
        print("")
        print("resultado:", number1,"*", number2,"=", number1*number2)

    if eleccion == 4:
        print("")
        print("resultado:", number1,"/", number2,"=", number1/number2)

    if eleccion == 5:
        print("Gracias Totales")

        break
