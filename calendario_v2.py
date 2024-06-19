# --------------------------------------------------------------------
dias_de_la_semana = 'lu ma mi ju vi sa do'

nombre_del_mes = [   "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio"
                     , "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"    ]

dias_de_duracion = [
                     [31,28,31,30,31,30,31,31,30,31,30,31] ,  # 0 : año normal 
                     [31,29,31,30,31,30,31,31,30,31,30,31]    # 1 : año bisiesto
                   ]

dias_transcurridos = [
                        [0,31,59,90,120,151,181,212,243,273,304,334,365] ,   # 0 : año normal
                        [0,31,60,91,121,152,182,213,244,274,305,335,366]     # 1 : año bisiesto 
                     ]

# --------------------------------------------------------------------

def bisiesto(A):
    return 1 if (A%4==0 and A%100!=0 or A%400==0) else 0

def duracion(M,A):
    return dias_de_duracion[bisiesto(A)][M-1]  

def nombre_mes(M):
    return nombre_del_mes[M-1]

def dia_semana (D,M,A) :
    DM = dias_transcurridos[bisiesto(A)][M-1]
    d = ((A-1)*365 + (A-1)//4 - ( 3*((A-1)//100+1)//4)+ DM + D) % 7
    return 6 if d==0 else d-1

# --------------------------------------------------------------------

def diames(D,M,A):
    
    c = dia_semana(1,M,A)
    X = dias_de_duracion[bisiesto(A)][M-1] + 1
    
    txt = '\n '+ nombre_del_mes[M-1] + ' ' + str(A) + '\n'
    txt = txt + ' lu  ma  mi  ju  vi  sa  do ' + '\n'
    txt = txt + ("    " * c )
    for i in range(1,X):      
        dia = f"[{i:2d}]" if i==D else f" {i:2d} "
        txt = txt + dia
        if (i+c)% 7==0 :
            txt = txt + '\n'
         
    return txt 

# --------------------------------------------------------------------

def inicio_de_mes(mes, año, columnas, fin):
    
    # genera los encabezados, nombre del mes y de los días
    if columnas==1:
        txt = '\n' + nombre_mes(mes) + ' ' + str(año) + '\n' 
        txt = txt + dias_de_la_semana + '\n'

    # genera la primera linea
    desplazamiento = dia_semana(1, mes, año) # calcula el deplazamiento de la semana 1
    txt = '   ' * desplazamiento
    for dia in range(1,8-desplazamiento):
        txt = txt + f' {dia} '
    txt = txt + fin    
    return txt

# --------------------------------------------------------------------
    
def imprime_semana(i,m,s):
    txt = ''
    for dia in range (i, i+7) :
        txt = txt + ( f"{dia:2d} " if dia <= m else "   " )
    txt = txt + s
    return txt

# --------------------------------------------------------------------
    
def unmes(M1,A1):

    '''
        imprime el mes/año dados en formato calendario
    '''
    
    txt = txt + inicio_de_mes(M1,A1,1,'\n')

    # genera el resto del mes, desde la segunda linea en adelante
    i = 7 - c1 + 1
    max1 = duracion(M1,A1)
    while i <= max1 :
        txt = txt + imprime_semana(i,max1,'\n')
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
    txt = txt + dias_de_la_semana + '\t' 
    txt = txt + dias_de_la_semana + '\n'
    
    # genera la primera linea de ambos meses (con corrimiento semana 1)
    txt = txt + inicio_de_mes(M1,A1,0,'\t')
    txt = txt + inicio_de_mes(M2,A2,0,'\n')

    # genera el resto del mes, desde la segunda linea en adelante
    i = 8 - dia_semana(1,M1,A1)
    j = 8 - dia_semana(1,M2,A2)
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    while i <= max1 or j <= max2 :
        txt = txt + imprime_semana(i,max1,'\t')
        i = i + 7  # pasa a la siguiente semana, mes 1
        txt = txt + imprime_semana(j,max2,'\n')
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
    txt = txt + dias_de_la_semana + '\t' 
    txt = txt + dias_de_la_semana + '\t' 
    txt = txt + dias_de_la_semana + '\n'
    
    # genera la primera linea de cada uno de los meses (con corrimiento semana 1)
    txt = txt + inicio_de_mes(M1,A1,0,'\t')
    txt = txt + inicio_de_mes(M2,A2,0,'\t')
    txt = txt + inicio_de_mes(M3,A3,0,'\n')

    # genera el resto del mes, desde la segunda linea en adelante
    i = 8 - dia_semana(1,M1,A1)
    j = 8 - dia_semana(1,M2,A2)
    k = 8 - dia_semana(1,M3,A3)
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    max3 = duracion(M3,A3)
    while i <= max1 or j <= max2 or k <= max3 :
        txt = txt + imprime_semana(i,max1,'\t')
        i = i + 7 # pasa a la siguiente semana, mes 1
        txt = txt + imprime_semana(j,max2,'\t')
        j = j + 7 # pasa a la siguiente semana, mes 2
        txt = txt + imprime_semana(k,max3,'\n')
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
    txt = txt + dias_de_la_semana + '\t' 
    txt = txt + dias_de_la_semana + '\t'  
    txt = txt + dias_de_la_semana + '\t'  
    txt = txt + dias_de_la_semana + '\n'

     # genera la primera linea de cada uno de los meses (con corrimiento semana 1)
    txt = txt + inicio_de_mes(M1,A1,0,'\t')
    txt = txt + inicio_de_mes(M2,A2,0,'\t')
    txt = txt + inicio_de_mes(M3,A3,0,'\t')
    txt = txt + inicio_de_mes(M4,A4,0,'\n')

    # genera el resto del mes, desde la segunda linea en adelante
    i = 8 - dia_semana(1,M1,A1)
    j = 8 - dia_semana(1,M2,A2)
    k = 8 - dia_semana(1,M3,A3)
    l = 8 - dia_semana(1,M4,A4)
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    max3 = duracion(M3,A3)
    max4 = duracion(M4,A4)
    while i <= max1 or j <= max2 or k <= max3 or l <= max4 :
        txt = txt + imprime_semana(i,max1,'\t')
        i = i + 7 # pasa a la siguiente semana, mes 1
        txt = txt + imprime_semana(j,max2,'\t')
        j = j + 7 # pasa a la siguiente semana, mes 2
        txt = txt + imprime_semana(k,max3,'\t')
        k = k + 7 # pasa a la siguiente semana, mes 3
        txt = txt + imprime_semana(l,max4,'\n')
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
    txt = txt + dias_de_la_semana + '\t' 
    txt = txt + dias_de_la_semana + '\t'  
    txt = txt + dias_de_la_semana + '\t'  
    txt = txt + dias_de_la_semana + '\t'  
    txt = txt + dias_de_la_semana + '\t'  
    txt = txt + dias_de_la_semana + '\n' 

    # genera la primera linea de cada uno de los meses (con corrimiento semana 1)
    txt = txt + inicio_de_mes(M1,A1,0,'\t')
    txt = txt + inicio_de_mes(M2,A2,0,'\t')
    txt = txt + inicio_de_mes(M3,A3,0,'\t')
    txt = txt + inicio_de_mes(M4,A4,0,'\t')
    txt = txt + inicio_de_mes(M5,A5,0,'\t')
    txt = txt + inicio_de_mes(M6,A6,0,'\n')

    #segundas lineas en adelante
    i = 8 - dia_semana(1,M1,A1)
    j = 8 - dia_semana(1,M2,A2)
    k = 8 - dia_semana(1,M3,A3)
    l = 8 - dia_semana(1,M4,A4)
    m = 8 - dia_semana(1,M5,A5)
    n = 8 - dia_semana(1,M6,A6)
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    max3 = duracion(M3,A3)
    max4 = duracion(M4,A4)
    max5 = duracion(M5,A5)
    max6 = duracion(M6,A6)
    while i <= max1 or j <= max2 or k <= max3 or l <= max4 or m <= max5 or n <= max6 :
        txt = txt + imprime_semana(i,max1,'\t')
        i = i + 7
        txt = txt + imprime_semana(j,max2,'\t')
        j = j + 7
        txt = txt + imprime_semana(k,max3,'\t')
        k = k + 7
        txt = txt + imprime_semana(l,max4,'\t')
        l = l + 7
        txt = txt + imprime_semana(m,max5,'\t')
        m = m + 7
        txt = txt + imprime_semana(n,max6,'\n')
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


print(dosmeses(12,2023,1,2024))

'''
AA = int(input("ingrese año : "))
print(anio1(AA))
print(anio2(AA))
print(anio3(AA))
print(anio4(AA))
print(anio6(AA))
'''

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

'''

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





