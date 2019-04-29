# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:04:53 2019

@author: Administrador

Recomendador Vinos
"""
import math

#Catalogo de productos, estos estarán en una base de datos. 
#El formato es el sgte: Producto1 = [calificación característica 1, calificación característica 2, ..., "nombre"]

vino1 = [2,1,5,1,5, "Sta Rita"]
vino2 = [1,4,3,2,1, "Patacon"]
vino3 = [3,5,1,1,1, "Concha y Toro"]
vino4 = [5,5,4,5,5, "San Pedro"]
vino5 = [2,3,1,4,3, "Gallo"]

#Lista con todos los productos

vinos = [vino1, vino2, vino3, vino4, vino5]

#Set de preguntas hipotéticas, y sus respectivas opciones de respuesta

p1 = "¿Cómo te gusta el café?"
p2 = "¿Qué chocolate te gusta?"
p3 = "¿Algún jugo?"
p4 = "¿Para qué ocasión lo quieres?"
p5 = "¿Hace cuánto tomas vino?"

r1 = """ 1) Muy fuerte \n 2) Fuerte \n 3) Débil \n 4) Con mucha azúcar \n 5) No tomo"""
r2 = """ 1) Cacao Puro \n 2) Amargo \n 3) De leche \n 4) Blanco \n 5) No me gusta"""
r3 = """ 1) Naranja \n 2) Arandanos \n 3) Frutilla \n 4) Pomelo \n 5) Mmm no gracias"""
r4 = """ 1) Con amigos \n 2) Tarde con la polola \n 3) Solo leyendo un libro \n 4) Fiesta \n 5) No tengo idea"""
r5 = """ 1) Mucha experiencia \n 2) Me manejo \n 3) Normal \n 4) Prefiero no decir \n 5) No cacho niuna w..."""

setpyr = [[p1,r1], [p2,r2], [p3,r3], [p4,r4], [p5,r5]]

#Se crea lista, inicilamente vacía, con las respuestas del usuario

respuestadada=[]

#Comienza el test

print("Bienvenido!, contestando las siguientes preguntas podremos recomendarte algún vino:")

for object in setpyr:
    print(object[0])
    print(object[1])
    respuestadada.append(float(input("Elige un número ")))
    print(" \n")
print("Estamos calculando el mejor vino para ti")

import time
time.sleep(2)

distanciarespuestaacadavino = {}
for vino in vinos:
    distanciarespuestaacadavino[vino[5]] = 0
    
    
#distanciarespuestaacadavino = {"vino1":0, "vino2":0, "vino3":0, "vino4":0, "vino5":0}

vinosypuntajes={}

for vino in vinos:
    suma = 0
    #print(vino)
    for i in range(len(respuestadada)):
        distentrepuntos = (vino[i]-respuestadada[i])**2
        suma = suma+distentrepuntos
    distanciaentrevinos = math.sqrt(suma)
    #print(distanciaentrevinos)
    vinosypuntajes[vino[5]]=distanciaentrevinos
    
import operator

print("Listo!, te recomendamos el vino:")
print(min(vinosypuntajes.items(), key=operator.itemgetter(1))[0])
    

    
    


        
    
        


