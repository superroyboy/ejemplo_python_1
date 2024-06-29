# import ...

# variables global

lista=[]

dic_autos={}

# funciones

def guardar():
    print("leer datos y guardar")
    
    patente = input('ingrese patente (4 letras y 2 numeros : ejemplo XXZZ12)')
    anio = int(input('ingrese año del vehiculo'))
    
    #opcion 1 : crear una tupla
    objeto =  (patente, anio)
    
    #opcion 2 : crear un diccionario
    #objeto = {'Patente':patente, 'Año': anio}
    
    lista.append(objeto)
    dic_autos[patente] = {'Año': anio}
#end def

def mostrar():
    print("mostrar todos los datos")
    
    for cosa in lista :
        print(cosa)
        
    
#end def

def buscar():
    print("buscar un dato y mostrar")
    patente_buscada = input('ingrese patente buscada')
    for cosa in lista :
        if cosa[0] == patente_buscada :
        #if cosa['Patente'] == patente_buscada :
            print(cosa)
            return
    print('no encontrada')    
    
    if patente_buscada in dic_autos:
        print(dic_autos[patente_buscada])
        
    
    
#end def

def salir():
    print("chao")
#end def



# principal

while True:
    # mostrar opciones
    print('''
          1.- Guardar
          2.- Mostrar todos
          3.- Buscar uno
          4.- Salir''')
    
    # escoger una
    try:
        op = int(input("ingrese opcion"))
    except:
        op = 0
    
    # hacer algo
    if op < 1 or op > 4 :
        print("opcion no valida")
    else:
        if op == 1 :
            guardar()
        elif op == 2 :
            mostrar()
        elif op == 3 :
            buscar()
        else :
            salir()
            break
        #end if    
    #end if
#end if