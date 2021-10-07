# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados

while True:

    print ("ingrese primer numero\n")
    numero_1 = int (input())

    print ("ingrese segundo numero\n")
    numero_2 = int (input())
 
# Verifique si el numero_1 es mayor a 5
#   --> En caso afirmativo, verifique si el numero_2
#       es positivo
#       --> En caso afirmativo imprima en pantalla "Resp=1"
#       --> En caso negativo imprima en pantalla   "Resp=2"
#  --> En caso negativo (numero_1 no es mayor a 5)
#      verifique si el numero_2 es mayor a 5
#       --> En caso afirmativo imprima en pantalla "Resp=3"
#       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > 5:
        if numero_2 >= 1:
            print ("Resp=1")
        else :
            print ("Resp=2")
    elif numero_2 > 5:
        print ("Resp=3")
    else :
        print ("Resp=4")


# Verifique la calificación de un estudiante según su
# puntaje en un examen
    print ("ingrese puntaje\n")
    puntaje = int (input())

# Si el puntaje es mayor igual a 90 --> imprimir A
# Si el puntaje es mayor igual a 80 --> imprimir B
# Si el puntaje es mayor igual a 70 --> imprimir C
# Si el puntaje es mayor igual a 60 --> imprimir D
# Si el puntaje es menor a  60      --> imprimir F

# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados

    if puntaje >= 100 :
        print ("Su resultado fue", puntaje)
        print ("Resultado de la prueva:¨A+¨")
        print("Sobrepasaste mis espectativas :)")
    elif puntaje > 90 :
        print ("Su resultado fue", puntaje)
        print ("Resultado de la prueva:¨A¨")

    elif puntaje >= 80 :
        print ("Su resultado fue", puntaje)
        print ("Resultado de la prueva:¨B¨")

    elif puntaje >= 70 :
        print ("Su resultado fue", puntaje)
        print ("Resultado de la prueva:¨C¨")

    elif puntaje >= 60 :
        print ("Su resultado fue", puntaje)
        print ("Resultado de la prueva:¨D¨")

    elif (puntaje < 60) and (puntaje > 0) :
        print ("Su resultado fue", puntaje)
        print ("Resultado de la prueva:¨F¨")

    elif puntaje <= 0:
        print (puntaje, "no es valido")

    print ("""ingrese 1 para continuar
ingrese 2 para salir\n""")
    numero = int (input())

    if numero == 1 :
        print ("Gracias por continuar")
        continue
    elif numero == 2 :
        print ("Gracias por usar nuestra aplicacion")
        break




