#Crear una función adivinar que permita adivinar un número
#generado en forma aleatoria
#I El número debe estar entre 0 y 100
#I Este número se genera adentro de la función
#I Además debe recibir un parámetro que sea la cantidad de intentos y
#en caso de que esta cantidad de intentos sea superada el programa
#debe terminar con un mensaje
#I Si el usuario adivina antes de superar el número de intentos máximo,
#se debe imprimir un mensaje con el número de intentos en los que adivinó
#Después de crear la función, llamarla en el mismo archivo
#Ejecutar el script desde la consola
import random

def adivinar(a):
    num = random.randint(0,100)
    x=0
    while True:
        if x==a:
            print("Se te acabaron los intentos")
            break
        else :
            prueba=int(input("Ingrese numero:"))
            if prueba==num:
                print("ACERTASTE en" , x+1 , "intentos")
                break
            else:
                print("ERRASTE te quedan" , a-(x+1) , "intentos")
                x=x+1
                if prueba>num:
                    print("El numero es menor")
                else:
                    print("El numero es mayor")

intentos=int(input("Cuantos intentos necesitas?"))

adivinar(intentos)
