# -*- coding: utf-8 -*-
"""ACTIVIDAD 1 CLASE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1feGkjPH2GbzTVG83P4lUUpVXxYCbnBCW
"""

def palindromo (zen2):
    if zen2 == zen2[::-1]:
        print("es palindromo")
    else:
        print ("no es palindromo")

zen2 = "ana"
palindromo(zen2)

fac = 5


def factorial(fac):

    temp =1
    for i in range(1,fac,1):

        if i <fac:
            temp= temp* (i+1)
            #print (temp)
    return temp


factorial(fac)

def doble_factorial(n):
    if n <= 0:
        return 1

    resultado = 1
    for i in range(n, 0, -2):
        resultado *= i

    return resultado


numero =  -4
resultado = doble_factorial(numero)
print(f"El doble factorial de {numero} es {resultado}")

def lucas (n):

    if n == 0: #condición para cubrir la posibilidan n=0
        return 2

    if n == 1: #condición para cubrir la posibilidad n=1
        return 1

    else:      #cubre las demás posibilidades para n
        a,b = 2,1

        for i in range(2,n + 1):


            #tem=a
            #a=b
            #b=b+tem
            a,b = b , a+b # se le asigna a "a" el valor de "b" y a "b" el valor anterior de "a" mas el valor de "b"


        return b # se retorna la variable que contiene elvalor requerido




print(lucas(9))  # Ejemplo de llamada a la función con n = 9
print(lucas(10))  # Ejemplo de llamada a la función con n = 10
print(lucas(11))  # Ejemplo de llamada a la función con n = 11

def binomial(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print(binomial(5,3))