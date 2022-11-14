##########################
#Proyecto calculadora 1
#subir a Github
#realizado: 11/11/2022
#Programador: Sergio Depetris
############################
#este programa inicial realiza una secuencia de codigos que permiten al Operador mejorar su resultado de busqueda.

number1=float(input("agregar un numero:"))
number2=float(input("agregar otro numero:"))

eleccion = 0

while eleccion != 6:

    print("""
    indique la operacion a realizar: 

    1) suma
    2) resta
    3) multiplicacion
    4) division
    5) seguir operando
    6) volver a inicio
    """) 
       
    eleccion = float(input())

    if eleccion == 1:
        print(" ")
        print("resultado: ", number1,"+", number2,"=", number1+number2)
        numberanterior= number1+number2
        
    if eleccion == 2:
        print("")
        print("resultado:", number1,"-", number2,"=", number1-number2)
        numberanterior= number1-number2

    if eleccion == 3:
        print("")
        print("resultado:", number1,"*", number2,"=", number1*number2)
        numberanterior= number1*number2

    if eleccion == 4:
        print("")
        print("resultado:", number1,"/", number2,"=", number1/number2)
        numberanterior= number1/number2

    if eleccion == 5:
        print ("seguir operando") 
        number1 = numberanterior
        number2=float(input("agregar otro numero:"))

    if eleccion == 6:
        print("Gracias Totales")

        break
    continue


