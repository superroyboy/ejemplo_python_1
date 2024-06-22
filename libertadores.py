import os
import time
import csv

def unpartido(e1,e2,marcador):
    #print("1 partido",e1,marcador,e2, end=' : ')
    if "pen." in marcador :
        resultado=marcador[-9:]
    else:
        resultado=marcador[0:3]
    
    g1 = int(resultado[0])
    g2 = int(resultado[2])
    
    if g1 > g2 :
        print(e1) 
        return e1
    else :
        print(e2)
        return e2
    
    #end if
#fin def

def dospartidos(e1,e2,marcador1,marcador2):
    #print("2 partidos",e1,marcador1,marcador2,e2)
    if "pen." in marcador2 :
        w = unpartido(e1,e2,marcador2)
    else:
        
        g1 = int(marcador1[0]) + int(marcador2[0]) 
        g2 = int(marcador1[2]) + int(marcador2[2]) 
    
        if g1 > g2 :
            print(e1) 
            w=e1
        else :
            print(e2)
            w=e2
            
    return w
        
#fin def

def trespartidos(e1,e2,marcador1,marcador2, marcador3):
    #print("3 partidos",e1,marcador1,marcador2,marcador3,e2)
    if marcador3 != "" :
        w = unpartido(e1,e2,marcador3)
    else:
        w = dospartidos(e1,e2,marcador1,marcador2)
        
    return w
#fin def

Ganadores = []

os.system('cls')

with open('C:\\Users\\CETECOM\\Downloads\\FinalesLibertadores.csv','r',encoding='utf-8') as entrada:
    print('Abrimos el archivo')
    contenido = csv.DictReader(entrada)
    for linea in contenido:
        #print(linea)
        #print('----------------------------')
        
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
            w = trespartidos(equipo1,equipo2,marcador1,marcador2, marcador3)
        else:
            if año <2019:
                w = dospartidos(equipo1,equipo2,marcador1,marcador2)
            else:
                w = unpartido(equipo1,equipo2,marcador1)
            #fin if
        #fin if
        
        Ganadores.append ( { 'Año': año, 'Ganador': w } )
        
        time.sleep(0.5)

    #fin for
     
#fin with
print('Cerramos el archivo')

import json

with open('C:\\Users\\CETECOM\\Downloads\\GanadoresLibertadores.json','w',encoding='utf-8') as salida:
    json.dump(Ganadores,salida, indent=1)

print('***')








