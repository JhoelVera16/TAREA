# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:54:01 2022

@author: vera1
"""

s=0#se inializa con la variable en 0
print()#salto de linea
print("Tablas de multiplicar")#mensaje principal, Tablas de multiplicar
x=int(input("Hasta que tabla desea reproducir: "))#solicita un dato para que funciones la tabla de multiplicar
y=int(input("Que rango de tabla desea ingresar: "))#solicita el dato del rango de la tabla
for n in range(1,x+1):#se define in rango
    print()#salto de linea
    print("La tabla del # ",n)#colocar el titulo de cada tabla
    par=0#aqui se inicia la variable par en 0
    impar=0#aqui se inicia la variable impar en 0
    for i in range(1,y+1):#se dfine rango donde la tabla debe multiplicar del 1 al 16
        r=i*n#resuelve la operacionde multiplicar
        s=s+r#realiza la operacion de sumar
        p=s/x#realiza la operacion de promedio
        print(i,"x",n,"=",r)#se imprime la tabla de multiplicar con su resultado
        if r%2==0:#aqui pregunta si el modulo al ralizar la operacion es igual a 0
            par+=1#si es verdadero se incrementa en 1 a la variable par
        else:#en tal caso que sea falso
            impar+=1#se incrementa en 1 la variable impar
    print()#salto de linea
    print("La suma es: ",s)#se imprime el valor de la suma 
    print("El promedio es: ",p)#se imprime el valor del promedio
    print("En la suma existen",par,"numeros pares" )#imprime los numeros que son pares
    print("En la suma existen",impar,"numeros impares" )#imprime los numeros que son impares
    
    
    