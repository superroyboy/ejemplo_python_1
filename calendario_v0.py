
def bisiesto(A):
    if A%4==0 and A%100!=0 or A%400==0 :
        return 1
    else :
        return 0

def duracion(M,A):
    if M==2 :
        return 28 + bisiesto(A)
    elif M==4 or M==6 or M==9 or M==11 :
        return 30
    else :
        return 31

def dias_acumulados(M,A):
    acum = 0
    for m in range(1,M):
        acum = acum + duracion (m,A)
    return acum

def dia_semana (D,M,A) :
    DM = dias_acumulados(M,A)
    d = ((A-1)*365 + (A-1)//4 - ( 3*((A-1)//100+1)//4)+ DM + D) % 7
    if d == 0 :  
        return 6 # pasa el domingo al final de la semana
    else :
        return d-1 # 0:lunes, 1:martes, 2:miercoles, 3:jueves, 4:viernes, 5:sabado

def nombre_mes(M):
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

def mes(M,A):
    txt = '\n'+ nombre_mes(M) + ' ' + str(A) + '\n'
    txt = txt + 'lu ma mi ju vi sa do' + '\n'
    c = dia_semana(1,M,A)    
    txt = txt + ("   " * c ) # desplazamiento primera linea
    for i in range(1,duracion(M,A)+1):
        d=str(i)
        if i < 10 :
            d = ' ' + d
        txt = txt + d + ' '
        if ( i+c ) % 7 == 0 :
            txt = txt + '\n'
    return txt

def anio(A) :
    txt = ''
    for m in range(12):
        txt = txt + mes(m+1,A) +'\n'
    return txt


def diames(D,M,A):
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
    

def dosmeses(M1,A1,M2,A2):
    
    # encabezados
    
    txt = '\n'+ nombre_mes(M1) + ' ' + str(A1) + '\t\t'
    txt = txt + nombre_mes(M2) + ' ' + str(A2) + '\n'
    
    txt = txt + 'lu ma mi ju vi sa do\t' + 'lu ma mi ju vi sa do\n'
    
    c1 = dia_semana(1,M1,A1)
    c2 = dia_semana(1,M2,A2)
    
    # primeras lineas
    
    txt = txt + ( "   " * c1 ) # desplazamiento 
    d1=1
    while d1+c1 <= 7:
        txt = txt + ' ' + str(d1) + ' '
        d1 = d1+1
    txt = txt + '\t'
    
    txt = txt + ( "   " * c2 ) # desplazamiento 
    d2=1
    while d2+c2 <= 7:
        txt = txt + ' ' + str(d2) + ' '
        d2=d2+1
    txt = txt + '\n'

    #segundas lineas en adelante
    
    i=d1
    j=d2
    
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    
    while i <= max1 or j <= max2 :

        linea_completa = False
        while linea_completa != True :
                
            d = str(i)
            if i < 10 :
                d = ' ' + d
            elif i > max1 :
                d = '  '
            
            if ( i + c1 ) % 7 == 0 :
                sep = '\t'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            i = i + 1
        
        linea_completa = False
        while not linea_completa :

            d = str(j)
            if j < 10 :
                d = ' ' + d
            elif j > max2 :
                d = '  '
            
            if ( j + c2 ) % 7 == 0 :
                sep = '\n'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            j = j + 1            

    return txt


def anio2(A) :
    año = ''
    for i in range(1,13,2):
        año = año + dosmeses(i,A,i+1,A)
    return año


def tresmeses(M1,A1, M2,A2, M3,A3):
    
    # encabezados
    
    txt = '\n'+ nombre_mes(M1) + ' ' + str(A1) + '\t\t'
    txt = txt + nombre_mes(M2) + ' ' + str(A2) + '\t\t'
    txt = txt + nombre_mes(M3) + ' ' + str(A3) + '\n'
    
    txt = txt + 'lu ma mi ju vi sa do\t' + 'lu ma mi ju vi sa do\t' + 'lu ma mi ju vi sa do\n'
    
    c1 = dia_semana(1,M1,A1)
    c2 = dia_semana(1,M2,A2)
    c3 = dia_semana(1,M3,A3)
    
    # primeras lineas
    
    txt = txt + ( "   " * c1 ) # desplazamiento 
    d1=1
    while d1+c1 <= 7:
        txt = txt + ' ' + str(d1) + ' '
        d1 = d1+1
    
    txt = txt + '\t' + ( "   " * c2 ) # desplazamiento 
    d2=1
    while d2+c2 <= 7:
        txt = txt + ' ' + str(d2) + ' '
        d2=d2+1
    
    txt = txt + '\t' + ( "   " * c3 ) # desplazamiento 
    d3=1
    while d3+c3 <= 7:
        txt = txt + ' ' + str(d3) + ' '
        d3=d3+1
    
    txt = txt + '\n'


    #segundas lineas en adelante
    
    i=d1
    j=d2
    k=d3
    
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    max3 = duracion(M3,A3)
    
    while i <= max1 or j <= max2 or k <= max3 :

        linea_completa = False
        while linea_completa != True :
                
            d = str(i)
            if i < 10 :
                d = ' ' + d
            elif i > max1 :
                d = '  '
            
            if ( i + c1 ) % 7 == 0 :
                sep = '\t'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            i = i + 1
            
        linea_completa = False
        while not linea_completa :

            d = str(j)
            if j < 10 :
                d = ' ' + d
            elif j > max2 :
                d = '  '
            
            if ( j + c2 ) % 7 == 0 :
                sep = '\t'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            j = j + 1
            
        linea_completa = False
        while not linea_completa :

            d = str(k)
            if k < 10 :
                d = ' ' + d
            elif k > max3 :
                d = '  '
            
            if ( k + c3 ) % 7 == 0 :
                sep = '\n'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            k = k + 1
            
    return txt


def anio3(A) :
    año = ''
    for i in range(1,13,3):
        año = año + tresmeses(i,A, i+1,A, i+2,A)
    return año


def cuatromeses(M1,A1, M2,A2, M3,A3, M4,A4):
    
    # encabezados
    
    txt = '\n'+ nombre_mes(M1) + ' ' + str(A1) + '\t\t'
    txt = txt + nombre_mes(M2) + ' ' + str(A2) + '\t\t'
    txt = txt + nombre_mes(M3) + ' ' + str(A3) + '\t\t'
    txt = txt + nombre_mes(M4) + ' ' + str(A4) + '\n'
    
    txt = txt + 'lu ma mi ju vi sa do\t' + 'lu ma mi ju vi sa do\t' + 'lu ma mi ju vi sa do\t' +'lu ma mi ju vi sa do\n'
    
    c1 = dia_semana(1,M1,A1)
    c2 = dia_semana(1,M2,A2)
    c3 = dia_semana(1,M3,A3)
    c4 = dia_semana(1,M4,A4)
    
    # primeras lineas
    
    txt = txt + ( "   " * c1 ) # desplazamiento 
    d1=1
    while d1+c1 <= 7:
        txt = txt + ' ' + str(d1) + ' '
        d1 = d1+1
    
    txt = txt + '\t' + ( "   " * c2 ) # desplazamiento 
    d2=1
    while d2+c2 <= 7:
        txt = txt + ' ' + str(d2) + ' '
        d2=d2+1
    
    txt = txt + '\t' + ( "   " * c3 ) # desplazamiento 
    d3=1
    while d3+c3 <= 7:
        txt = txt + ' ' + str(d3) + ' '
        d3=d3+1
    
    txt = txt + '\t' + ( "   " * c4 ) # desplazamiento 
    d4=1
    while d4+c4 <= 7:
        txt = txt + ' ' + str(d4) + ' '
        d4=d4+1
    
    txt = txt + '\n'


    #segundas lineas en adelante
    
    i=d1
    j=d2
    k=d3
    l=d4
    
    max1 = duracion(M1,A1)
    max2 = duracion(M2,A2)
    max3 = duracion(M3,A3)
    max4 = duracion(M4,A4)
    
    while i <= max1 or j <= max2 or k <= max3 or l <= max4 :

        linea_completa = False
        while linea_completa != True :
                
            d = str(i)
            if i < 10 :
                d = ' ' + d
            elif i > max1 :
                d = '  '
            
            if ( i + c1 ) % 7 == 0 :
                sep = '\t'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            i = i + 1
            
        linea_completa = False
        while not linea_completa :

            d = str(j)
            if j < 10 :
                d = ' ' + d
            elif j > max2 :
                d = '  '
            
            if ( j + c2 ) % 7 == 0 :
                sep = '\t'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            j = j + 1
            
        linea_completa = False
        while not linea_completa :

            d = str(k)
            if k < 10 :
                d = ' ' + d
            elif k > max3 :
                d = '  '
            
            if ( k + c3 ) % 7 == 0 :
                sep = '\t'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            k = k + 1
            
        linea_completa = False
        while not linea_completa :

            d = str(l)
            if l < 10 :
                d = ' ' + d
            elif l > max4 :
                d = '  '
            
            if ( l + c4 ) % 7 == 0 :
                sep = '\n'
                linea_completa = True
            else :
                sep = ' '

            txt = txt + d + sep    
            l = l + 1

    return txt

def anio4(A) :
    año = ''
    for i in range(1,13,4):
        año = año + cuatromeses(i,A, i+1,A, i+2,A, i+3,A)
    return año

# main

'''
MM = int(input("ingrese mes : "))
AA = int(input("ingrese año : "))
#cal = mes(MM,AA)
#print(cal)
print(mes(MM,AA))
'''


'''
AA = int(input("ingrese año : "))
print(anio(AA))
'''

print(dosmeses(12,2023,1,2024))

#print(anio2(2024))

#print(anio3(2024))

#print(anio4(2024))


'''
DD = int(input("ingrese día : "))
MM = int(input("ingrese mes : "))
AA = int(input("ingrese año : "))
print(diames(DD,MM,AA))
'''



while True:
    
    try :
        AA = int(input("ingrese año : "))
    except :
        AA = 2024
        
    try :
        B = int(input("Cuantos meses hacia el lado ? (1,2,3,4): "))
    except :
        B = 3

    if B == 1 :
        print(anio(AA))
    elif B == 2 :
        print(anio2(AA))
    elif B == 3 :
        print(anio3(AA))
    elif B == 4 :
        print(anio4(AA))
    else :
        break

print("bye")






