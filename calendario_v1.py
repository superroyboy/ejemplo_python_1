# --------------------------------------------------------------------

def bisiesto(A):
    
    '''
        para el año A retorna 1 si es bisiesto o 0 si es año normal
    '''
    
    if A%4==0 and A%100!=0 or A%400==0 :
        return 1
    else :
        return 0

# --------------------------------------------------------------------

def duracion(M,A):
    
    '''
        retorna la duración del mes M en días.
        para M==2 (febrero ) retorna 28 para un año normal
                                   o 29 para un año bisiesto
    '''

    if M==2 :
        return 28 + bisiesto(A)
    elif M==4 or M==6 or M==9 or M==11 :
        return 30
    else :
        return 31

# --------------------------------------------------------------------

def dias_acumulados(M,A):

    '''
        acumula los días transcurridos antes del primer día del mes
        para enero : 0 días
        para febrero : 31 días (los días de enero)
        para marzo : 59 días ( 31 días de enero + 28 días de febrero )
                   o 60 días ( 31 días de enero + 29 días de febrero en año bisiesto )
        y así sucesivamente para cualquier mes del año
    '''
    acum = 0
    for m in range(1,M):
        acum = acum + duracion (m,A)
    return acum

# --------------------------------------------------------------------

def dia_semana (D,M,A) :
    
    '''
        Permite determinar el día de la semana (lunes a domingo) para una fecha cualquiera (D/M/A)
        fuente : https://es.wikibooks.org/wiki/Algoritmia/Algoritmo_para_calcular_el_d%C3%ADa_de_la_semana
        con una pequeña corrección para que 0:lunes, 1:martes, 2:miercoles, etc. hasta 6:domingo
    '''

    DM = dias_acumulados(M,A)
    d = ((A-1)*365 + (A-1)//4 - ( 3*((A-1)//100+1)//4)+ DM + D) % 7
    
    # corrección : pasar el domingo al final de la semana
    if d == 0 :  
        return 6 # 6 : domingo 
    else :
        return d-1 # 0:lunes, 1:martes, 2:miercoles, 3:jueves, 4:viernes, 5:sabado

# --------------------------------------------------------------------

def nombre_mes(M):
    
    '''
        Devuelve el nombre del mes M , en español.
        Usa "if, elif, else" porque mis alumnos aun no conocen el concepto de arreglos
    '''
        
    if M==1 :
        return "Enero"
    elif M==2 :
        return "Febrero"
    elif M==3 :
        return "Marzo"
    elif M==4 :
        return "Abril"
    elif M==5 :
        return "Mayo"
    elif M==6 :
        return "Junio"
    elif M==7 :
        return "Julio"
    elif M==8 :
        return "Agosto"
    elif M==9 :
        return "Septiembre"
    elif M==10 :
        return "Octubre"
    elif M==11 :
        return "Noviembre"
    else : #M==12
        return "Diciembre"

# --------------------------------------------------------------------

def diames(D,M,A):
    
    '''
        para una fecha dada  D/M/A   (día/mes/año)
        retorna un texto con el mes completo en formato "calendario"
        destacando el día dentro del mes
        
    '''
    
    txt = '\n '+ nombre_mes(M) + ' ' + str(A) + '\n'
    txt = txt + ' lu  ma  mi  ju  vi  sa  do ' + '\n'
    c = dia_semana(1,M,A)
    txt = txt + ("    " * c )
    for i in range(1,duracion(M,A)+1):   
        d=str(i)    
        if i < 10 :      
            d = ' ' + d    
        if i == D :                      
            txt = txt + '[' + d + ']'    
        else :                           
            txt = txt + ' '+ d + ' '     
        if ( i+c ) % 7 == 0 : 
            txt = txt + '\n'  
    return txt 

# --------------------------------------------------------------------

def inicio_de_mes(c,s):

    '''
        genera la primera semana del mes considerando el corrimiento "c" 
        además usa el separador "s" que puede ser un tabulado ('\t') o un
        salto de línea ('\n') según corresponda.
        devuelve la primera linea, ejemplo : "       1  2  3 "
    '''
    
    txt = '   ' * c
    
    d = 1
    while d + c <= 7:
        txt = txt + ' ' + str(d) + ' '
        d = d + 1    
    
    txt = txt + s
    
    return txt

# --------------------------------------------------------------------
    
def imprime_semana(i,m,c,s):

    '''
        imprime una semana dentro del mes.
        i corresponde al lunes de esa semana
        m es el máximo de días o duración total de ese mes
        c es el corrimiento o desplazamiento de la primera semana
        s es el separador ya sea tabulado ('\t') o salto de linea ('\n')
    '''
    
    txt = ''
    
    linea_completa = False
    while linea_completa != True :
            
        d = str(i)
        if i < 10 :
            d = ' ' + d
        elif i > m :
            d = '  '
        
        if ( i + c ) % 7 == 0 :
            sep = s
            linea_completa = True
        else :
            sep = ' '

        txt = txt + d + sep    
        i = i + 1
        
    return txt

# --------------------------------------------------------------------
    
def unmes(M1,A1):

    '''
        imprime el mes/año dados en formato calendario
    '''
    
    # genera los encabezados, nombre del mes y de los días
    txt = '\n'+ nombre_mes(M1) + ' ' + str(A1) + '\n'
    txt = txt + 'lu ma mi ju vi sa do' + '\n'
    
    # genera la primera linea
    c1 = dia_semana(1,M1,A1) # calcula el corrimiento de la semana 1
    txt = txt + inicio_de_mes(c1,'\n')

    # genera el resto del mes, desde la segunda linea en adelante
    i = 7 - c1 + 1
    max1 = duracion(M1,A1)
    while i <= max1 :
        txt = txt + imprime_semana(i,max1,c1,'\n')
        i = i + 7 # pasa a la siguiente semana

    # retorna el mes completo
    return txt

# --------------------------------------------------------------------
    
def anio1(A) :
    '''
        imprime el Año dado en formato calendario
        un mes por vez
    '''
    año = ''
    for m in range(12):
        año = año + unmes(m+1,A) +'\n'
    return año

# --------------------------------------------------------------------
    
def dosmeses(M1,A1,M2,A2):
    '''
        imprime los mes/año dados en formato calendario
        uno junto al otro (izquierda - derecha)
    '''
    # genera los encabezados, nombre del mes y de los días
    txt = '\n'+ nombre_mes(M1) + ' ' + str(A1) + '\t\t'
    txt = txt + nombre_mes(M2) + ' ' + str(A2) + '\n'
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\n'
    
    # genera la primera linea de ambos meses (con corrimiento semana 1)
    c1 = dia_semana(1,M1,A1)
    c2 = dia_semana(1,M2,A2)
    txt = txt + inicio_de_mes(c1,'\t')
    txt = txt + inicio_de_mes(c2,'\n')

    # genera el resto del mes, desde la segunda linea en adelante
    i = 7 - c1 + 1
    j = 7 - c2 + 1
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    while i <= max1 or j <= max2 :
        txt = txt + imprime_semana(i,max1,c1,'\t')
        i = i + 7  # pasa a la siguiente semana, mes 1
        txt = txt + imprime_semana(j,max2,c2,'\n')
        j = j + 7  # pasa a la siguiente semana, mes 2
    
    # retorna el mes completo
    return txt

# --------------------------------------------------------------------
    
def anio2(A) :
    '''
        imprime el Año dado en formato calendario
        dos meses por vez (uno junto al otro)
    '''
    año = ''
    for i in range(1,13,2):
        año = año + dosmeses(i,A,i+1,A)
    return año

# --------------------------------------------------------------------
    
def tresmeses(M1,A1, M2,A2, M3,A3):
    '''
        imprime los mes/año dados en formato calendario
        uno junto al otro (izquierda - centro - derecha)
    '''
    # genera los encabezados, nombre del mes y de los días
    txt = '\n'+ nombre_mes(M1) + ' ' + str(A1) + '\t\t'
    txt = txt + nombre_mes(M2) + ' ' + str(A2) + '\t\t'
    txt = txt + nombre_mes(M3) + ' ' + str(A3) + '\n'
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\n'
    
    # genera la primera linea de cada uno de los meses (con corrimiento semana 1)
    c1 = dia_semana(1,M1,A1)
    c2 = dia_semana(1,M2,A2)
    c3 = dia_semana(1,M3,A3)
    txt = txt + inicio_de_mes(c1,'\t')
    txt = txt + inicio_de_mes(c2,'\t')
    txt = txt + inicio_de_mes(c3,'\n')

    # genera el resto del mes, desde la segunda linea en adelante
    i = 7 - c1 + 1
    j = 7 - c2 + 1
    k = 7 - c3 + 1
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    max3 = duracion(M3,A3)
    while i <= max1 or j <= max2 or k <= max3 :
        txt = txt + imprime_semana(i,max1,c1,'\t')
        i = i + 7 # pasa a la siguiente semana, mes 1
        txt = txt + imprime_semana(j,max2,c2,'\t')
        j = j + 7 # pasa a la siguiente semana, mes 2
        txt = txt + imprime_semana(k,max3,c3,'\n')
        k = k + 7 # pasa a la siguiente semana, mes 3
    
    # retorna el mes completo
    return txt

# --------------------------------------------------------------------
    
def anio3(A) :
    '''
        imprime el Año dado en formato calendario
        tres meses por vez (uno junto al otro)
    '''
    año = ''
    for i in range(1,13,3):
        año = año + tresmeses(i,A, i+1,A, i+2,A)
    return año

# --------------------------------------------------------------------
    
def cuatromeses(M1,A1, M2,A2, M3,A3, M4,A4):
    '''
        imprime los mes/año dados en formato calendario
        uno junto al otro (izquierda - centro - centro - derecha)
    '''
    # genera los encabezados, nombre del mes y de los días
    txt = '\n'+ nombre_mes(M1) + ' ' + str(A1) + '\t\t'
    txt = txt + nombre_mes(M2) + ' ' + str(A2) + '\t\t'
    txt = txt + nombre_mes(M3) + ' ' + str(A3) + '\t\t'
    txt = txt + nombre_mes(M4) + ' ' + str(A4) + '\n'
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\n'

     # genera la primera linea de cada uno de los meses (con corrimiento semana 1)
    c1 = dia_semana(1,M1,A1)
    c2 = dia_semana(1,M2,A2)
    c3 = dia_semana(1,M3,A3)
    c4 = dia_semana(1,M4,A4)
    txt = txt + inicio_de_mes(c1,'\t')
    txt = txt + inicio_de_mes(c2,'\t')
    txt = txt + inicio_de_mes(c3,'\t')
    txt = txt + inicio_de_mes(c4,'\n')

    # genera el resto del mes, desde la segunda linea en adelante
    i = 7 - c1 + 1
    j = 7 - c2 + 1
    k = 7 - c3 + 1
    l = 7 - c4 + 1
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    max3 = duracion(M3,A3)
    max4 = duracion(M4,A4)
    while i <= max1 or j <= max2 or k <= max3 or l <= max4 :
        txt = txt + imprime_semana(i,max1,c1,'\t')
        i = i + 7 # pasa a la siguiente semana, mes 1
        txt = txt + imprime_semana(j,max2,c2,'\t')
        j = j + 7 # pasa a la siguiente semana, mes 2
        txt = txt + imprime_semana(k,max3,c3,'\t')
        k = k + 7 # pasa a la siguiente semana, mes 3
        txt = txt + imprime_semana(l,max4,c4,'\n')
        l = l + 7 # pasa a la siguiente semana, mes 4

    # retorna el mes completo
    return txt

# --------------------------------------------------------------------
    
def anio4(A) :
    '''
        imprime el Año dado en formato calendario
        cuatro meses por vez (uno junto al otro)
    '''
    año = ''
    for i in range(1,13,4):
        año = año + cuatromeses(i,A, i+1,A, i+2,A, i+3,A)
    return año

# --------------------------------------------------------------------
    
def seismeses(M1,A1, M2,A2, M3,A3, M4,A4, M5,A5, M6,A6):
    
    '''
        imprime los mes/año dados en formato calendario
        uno junto al otro ( mes1 - mes2 - mes3 - mes4 - mes5 - mes6 )
    '''
    # genera los encabezados, nombre del mes y de los días
    txt = '\n'+ nombre_mes(M1) + ' ' + str(A1) + '\t\t'
    txt = txt + nombre_mes(M2) + ' ' + str(A2) + '\t\t'
    txt = txt + nombre_mes(M3) + ' ' + str(A3) + '\t\t'
    txt = txt + nombre_mes(M4) + ' ' + str(A4) + '\t\t'
    txt = txt + nombre_mes(M5) + ' ' + str(A5) + '\t\t'
    txt = txt + nombre_mes(M6) + ' ' + str(A6) + '\n'
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\t' 
    txt = txt + 'lu ma mi ju vi sa do\n'

    # genera la primera linea de cada uno de los meses (con corrimiento semana 1)
    c1 = dia_semana(1,M1,A1)
    c2 = dia_semana(1,M2,A2)
    c3 = dia_semana(1,M3,A3)
    c4 = dia_semana(1,M4,A4)
    c5 = dia_semana(1,M5,A5)
    c6 = dia_semana(1,M6,A6)
    txt = txt + inicio_de_mes(c1,'\t')
    txt = txt + inicio_de_mes(c2,'\t')
    txt = txt + inicio_de_mes(c3,'\t')
    txt = txt + inicio_de_mes(c4,'\t')
    txt = txt + inicio_de_mes(c5,'\t')
    txt = txt + inicio_de_mes(c6,'\n')

    #segundas lineas en adelante
    i = 7 - c1 + 1
    j = 7 - c2 + 1
    k = 7 - c3 + 1
    l = 7 - c4 + 1
    m = 7 - c5 + 1
    n = 7 - c6 + 1
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    max3 = duracion(M3,A3)
    max4 = duracion(M4,A4)
    max5 = duracion(M5,A5)
    max6 = duracion(M6,A6)
    while i <= max1 or j <= max2 or k <= max3 or l <= max4 or m <= max5 or n <= max6 :
        txt = txt + imprime_semana(i,max1,c1,'\t')
        i = i + 7
        txt = txt + imprime_semana(j,max2,c2,'\t')
        j = j + 7
        txt = txt + imprime_semana(k,max3,c3,'\t')
        k = k + 7
        txt = txt + imprime_semana(l,max4,c4,'\t')
        l = l + 7
        txt = txt + imprime_semana(m,max5,c5,'\t')
        m = m + 7
        txt = txt + imprime_semana(n,max6,c6,'\n')
        n = n + 7
    
    # retorna el mes completo
    return txt

# --------------------------------------------------------------------    

def anio6(A) :
    '''
        imprime el Año dado en formato calendario
        seis meses por vez (uno junto al otro, de izquierda a derecha)
    '''
    año = ''
    for i in range(1,13,6):
        año = año + seismeses(i,A, i+1,A, i+2,A, i+3,A, i+4,A, i+5,A)
    return año

# --------------------------------------------------------------------    

def anio(A,B) :
    '''
        según los meses hacia el lado B, imprime el año A
    '''

    if B == 1 :
        return anio1(A)
    elif B == 2 :
        return anio2(A)
    elif B == 3 :
        return anio3(A)
    elif B == 4 :
        return anio4(A)
    elif B == 6 :
        return anio6(A)
    else :
        return ""

# --------------------------------------------------------------------

# main

'''
MM = int(input("ingrese mes : "))
AA = int(input("ingrese año : "))
print(mes(MM,AA))
'''

'''
print(dosmeses(12,2023,1,2024))
'''

'''
AA = int(input("ingrese año : "))
print(anio1(AA))
print(anio2(AA))
print(anio3(AA))
print(anio4(AA))
print(anio6(AA))
'''

try :
    DD = int(input("ingrese día : "))
except :
    DD = 0

try :
    MM = int(input("ingrese mes : "))
except :
    MM = 5

try :
    AA = int(input("ingrese año : "))
except :
    AA = 2024

if DD > 0 :
    print(diames(DD,MM,AA))
else :
    print(unmes(MM,AA))

dummy =input("cualquier tecla para continuar...")

while True:
    
    try :
        AA = int(input("ingrese año : "))
    except :
        AA = 2024
        
    try :
        BB = int(input("Cuantos meses hacia el lado ? (1,2,3,4 o 6): "))
    except :
        BB = 3

    if BB >= 1 and BB <= 6 and BB != 5 :
        print(anio(AA,BB))
    else :
        break

print("bye")





