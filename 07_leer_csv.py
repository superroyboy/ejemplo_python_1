import csv

with open('C:\\Users\\Roy\\Desktop\\pythons\\FinalesChampions.csv', 'r', encoding='utf-8') as entrada :
    # fuente : https://es.uefa.com/uefachampionsleague/history/winners/finals/
    
    contenido=csv.DictReader(entrada)
    
    for linea in contenido :
        
        campeonato = linea['Torneo']
        equipo_local = linea['Equipo1']
        pais_local = linea['Pais1']
        resultado = linea['Marcador']
        equipo_visitante = linea['Equipo2']
        pais_visitante = linea['Pais2']
        estadio = linea['Estadio']
        ciudad = linea['Ciudad']
        pais = linea['Pais3']


        goles_local = int(resultado[0])
        goles_visita = int(resultado[2])

        print(campeonato, resultado, end='\t')

        if goles_local > goles_visita :
            print('Ganador', equipo_local)
        elif goles_local < goles_visita :
            print('Ganador', equipo_visitante)
        else:
            print('Empate en el tiempo reglamentario',end='\t')
            goles_local = int(resultado[5])
            goles_visita = int(resultado[7])
            if goles_local > goles_visita :
                print('Ganador', equipo_local)
            elif goles_local < goles_visita :
                print('Ganador', equipo_visitante)        

    #end for
    

#end with
print('fin')