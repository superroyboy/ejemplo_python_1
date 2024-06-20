import os
import time
import csv

def unpartido(e1,e2,marcador):
    print("1 partido",e1,marcador,e2, end=' : ')
    goles1 = int(marcador[0])
    goles2 = int(marcador[2])
    if goles1 > goles2:
        print("Ganador",e1)
    else:
        if goles2 > goles1 :
            print("Ganador",e2)
        else:
            print("Empate") # nota , en este caso analizar penales
        #end if
    #end if
#fin def

def dospartidos(e1,e2,marcador1,marcador2):
    print("2 partidos",e1,marcador1,marcador2,e2)
#fin def

def trespartidos(e1,e2,marcador1,marcador2, marcador3):
    print("3 partidos",e1,marcador1,marcador2,marcador3,e2)
#fin def

os.system('cls')

with open('C:\\Users\\CETECOM\\Downloads\\FinalesLibertadores.csv','r',encoding='utf-8') as entrada:
    print('Abrimos el archivo')
    contenido = csv.DictReader(entrada)
    for linea in contenido:
        #print(linea)
        
        año=int(linea['Año'])
        equipo1=linea['Equipo1']
        pais1=linea['Pais1']
        marcador1=linea['Marcador1']
        marcador2=linea['Marcador2']
        marcador3=linea['Marcador3']
        equipo2=linea['Equipo2']
        pais2=linea['Pais2']
        
        print(año,end=': ')
        if año< 1988:
            trespartidos(equipo1,equipo2,marcador1,marcador2, marcador3)
        else:
            if año <2019:
                dospartidos(equipo1,equipo2,marcador1,marcador2)
            else:
                unpartido(equipo1,equipo2,marcador1)
            #fin if
        #fin if
        
        #time.sleep(1)
        
        
    #fin for    
#fin with
print('Cerramos el archivo')









