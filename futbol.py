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
    print("analizar un partido")
    goles1 = int(marcador[0])
    goles2 = int(marcador[2])
    if goles1 > goles2:
        print(f'Ganador, {e1}')
    else:
        print(f'Ganador {e2}')
    #fin if
#fin def

def analiza2partidos(marcador1,marcador2,e1,e2):
    print("analizar dos partidos")
#fin def

def analiza3partidos(marcador1,marcador2,marcador3,e1,e2):
    print("analizar tres partidos")
#fin def


os.system("cls")
with open("C:\\Users\\CETECOM\\Downloads\\FinalesLibertadores.csv", "r", encoding="utf-8") as entrada:
    print("abrimos el archivo")
    contenido = csv.DictReader(entrada)
    for line in contenido:
        #print(line)
        anio=int(line['Año'])
        equip1=line['Equipo1']
        #pais1 = line ['Pais1']
        marc1=line ['Marcador1']
        marc2 = line ['Marcador2']
        marc3=line ['Marcador3']
        equip2=line['Equipo2']
        #pais2=line['Pais2']
        print(anio , end= ': ')
        
        if anio <= 1987 :
            analiza3partidos(marc1,marc2,marc3,equip1,equip2)
        else:
            if anio <= 2018 :
                analiza2partidos(marc1,marc2,equip1,equip2)   
            else :
                analiza1partido(marc1,equip1,equip2)
            #fin if
        #fin if
        
        # time.sleep(1)
        
    #fin for
#fin with
print("cerramos el archivo")  

 






