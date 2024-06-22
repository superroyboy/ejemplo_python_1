'''
 el objetivo es leer el archivo de datos
 FinalesLibertadores.csv 
 y para cada partido indicar el equipo ganador
 El "truco" es que 
 - hasta 1987 hubieron 3 partidos : ida, vuelta y desempate
 - hasta 2007 hubieron 2 partido : ida y vuelta
 - recientemente solo hay 1 partido (una final) 
'''

# abrir el archivo
# recorrer cada linea del archivo, mostrando a pantalla

import os
import time
import csv

def analiza1partido(marcador,e1,e2):
    #print("analizar un partido")

    g1 = int(marcador[0])
    g2 = int(marcador[2]) 
    
    if g1 > g2 :
        print(f'Ganador, {e1}')
        return e1
    elif g1 < g2 :
        print(f'Ganador {e2}')
        return e2
    else :  # g1 == g2
        #print('Empate') #...
        if "pen." in marcador :
            marca = marcador[-9:]
            w = analiza1partido(marca,e1,e2)
        return w
        
#fin def

def analiza2partidos(marcador1,marcador2,e1,e2):
    #print("analizar dos partidos")
    
    ge1p1 = int(marcador1[0])
    ge2p1 = int(marcador1[2]) 
    
    ge1p2 = int(marcador2[0])
    ge2p2 = int(marcador2[2]) 
    
    g1 = ge1p1 + ge1p2 
    g2 = ge2p1 + ge2p2 
    
    if g1 > g2 :
        print(f'Ganador, {e1}')
        return e1
    elif g1 < g2 :
        print(f'Ganador {e2}')
        return e2
    else :  # g1 == g2
        #print('Empate') #...
        if "pen." in marcador2 :
            marca = marcador2[-9:]
            w = analiza1partido(marca,e1,e2)
        return w
    
#fin def

def analiza3partidos(marcador1,marcador2,marcador3,e1,e2):
    #print("analizar tres partidos")
    if marcador3 != "" :
        w = analiza1partido(marcador3,e1,e2)
    else: #no hay tercer partido
        w = analiza2partidos(marcador1,marcador2,e1,e2)
    
    return w
#fin def


ganadores = []

os.system("cls")
datos="C:\\Users\\CETECOM\\Downloads\\FinalesLibertadores.csv"
with open(datos, "r", encoding="utf-8") as entrada:
    print("abrimos el archivo")
    contenido = csv.DictReader(entrada)
   
    for linea in contenido:
        #print(linea)
        #print("---------------------------")
        anio=int(linea['Año'])
        equipo1=linea['Equipo1']
        pais1 = linea ['Pais1']
        marc1=linea ['Marcador1']
        marc2 = linea ['Marcador2']
        marc3=linea ['Marcador3']
        equipo2=linea['Equipo2']
        pais2=linea['Pais2']
        
        print(anio , end= ': ')
        
        
        if anio < 1988 : # si es ANTERIOR a 1988
            ganador= analiza3partidos(marc1,marc2,marc3,equipo1,equipo2)
        else:
            if anio < 2019 :
                ganador= analiza2partidos(marc1,marc2,equipo1,equipo2)   
            else :
                ganador= analiza1partido(marc1,equipo1,equipo2)
            #fin if
        #fin if
        
        ganadores.append( {'Año':anio,'Ganador':ganador} ) 
        
        time.sleep(0)
        
    #fin for
#fin with
print("cerramos el archivo")  

import json

with open("C:\\Users\\CETECOM\\Downloads\\Ganadores.json","w") as salida:
    json.dump(ganadores,salida, indent=1)


print("fin")

 






